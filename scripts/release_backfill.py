#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
# SPDX-License-Identifier: Apache-2.0 OR MIT
"""Package a release assets reproducibly."""
from __future__ import annotations
import argparse, gzip, hashlib, io, json, re, sys, tarfile, uuid
from pathlib import Path

NAMESPACE = "https://bankstatementparser.com/sbom.cdx.json"
LICENCE_FILES = ("LICENSE", "LICENSE-APACHE", "LICENSE-MIT")

def site_tree(src: Path) -> Path:
    for candidate in (src / "public", src / "site", src / "docs"):
        if (candidate / "index.html").is_file(): return candidate
    raise SystemExit(f"[backfill] no built site in {src}/public, site, or docs")

def serial_for(version: str) -> str:
    return f"urn:uuid:{uuid.uuid5(uuid.NAMESPACE_URL, f"{NAMESPACE}#{version}")}"

def sbom_for(site: Path, version: str) -> dict:
    path = site / "sbom.cdx.json"
    if path.is_file():
        sbom = json.loads(path.read_text(encoding="utf-8"))
        sbom.setdefault("serialNumber", serial_for(version))
    else:
        sbom = {
            "bomFormat": "CycloneDX", "specVersion": "1.5",
            "serialNumber": serial_for(version), "version": 1,
            "metadata": {"component": {
                "type": "application", "bom-ref": f"bankstatementparser.com@{version}",
                "name": "bankstatementparser.com", "version": version,
                "description": "Static documentation website compiled with Rust static-site-generator (ssg)."
            }}, "components": []
        }
    return sbom

def add(tar: tarfile.TarFile, path: Path, arcname: str, mtime: int) -> None:
    info = tar.gettarinfo(str(path), arcname)
    info.uid = info.gid = 0
    info.uname = info.gname = ""
    info.mtime = mtime
    if info.isfile():
        with path.open("rb") as handle: tar.addfile(info, handle)
    else: tar.addfile(info)

def package(src: Path, site: Path, out: Path, name: str, mtime: int) -> Path:
    raw = io.BytesIO()
    with tarfile.open(fileobj=raw, mode="w", format=tarfile.PAX_FORMAT) as tar:
        add(tar, site, "site", mtime)
        for path in sorted(site.rglob("*")):
            add(tar, path, "site/" + path.relative_to(site).as_posix(), mtime)
        for licence in LICENCE_FILES:
            if (src / licence).is_file(): add(tar, src / licence, licence, mtime)
    target = out / name
    with target.open("wb") as handle, gzip.GzipFile(fileobj=handle, mode="wb", mtime=0, filename="") as gz:
        gz.write(raw.getvalue())
    return target

def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", required=True, type=Path)
    parser.add_argument("--tag", required=True)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--mtime", type=int, default=0)
    args = parser.parse_args(argv)
    version = args.tag[1:]
    site = site_tree(args.src)
    args.out.mkdir(parents=True, exist_ok=True)
    archive = package(args.src, site, args.out, f"bankstatementparser-site-v{version}.tar.gz", args.mtime)
    sbom = args.out / f"bankstatementparser-site-v{version}.cdx.json"
    sbom.write_text(json.dumps(sbom_for(site, version), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    sums = "".join(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  ./{p.name}\n" for p in sorted((archive, sbom)))
    (args.out / "SHA256SUMS").write_text(sums, encoding="utf-8")
    print(f"[backfill] {args.tag}: {archive.name}, {sbom.name}, SHA256SUMS")
    return 0

if __name__ == "__main__": sys.exit(main(sys.argv[1:]))
