# Release signing keys

Every release tag is an annotated, cryptographically signed Git tag. Tags are
signed with SSH keys, and `KEYS.asc` lists the trusted keys in OpenSSH
allowed-signers format. Verify a tag with Git 2.34 or later:

```sh
git fetch --tags --force
git -c gpg.ssh.allowedSignersFile=KEYS.asc tag -v v0.0.5
```

A good result names the principal `sebastian.rousseau@gmail.com` and one of
the fingerprints below. The release workflow checks tags against
`.github/allowed_signers`, which lists the same keys.

| Fingerprint | Host |
| :--- | :--- |
| `SHA256:f6FG+guRNtT3R36oQFS4oWCx1d10nm+BoaIL3Tkh1r4` | rousseau-mb-neo |
| `SHA256:kIOPAavp1TCEauTr1tTIN3cv+tSs6F9m/4lZjuM9tqk` | rousseau-mbp-m1 |
