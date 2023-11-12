<!-- markdownlint-disable MD033 MD041 -->

<img
  align="right"
  alt="Logo of Bank Statement Parser"
  height="261"
  src="https://kura.pro/bankstatementparser/images/logos/bankstatementparser.webp"
  width="261"
  />

<!-- markdownlint-enable MD033 MD041 -->

# bankstatementparser.com - Official Website 🌏

Welcome to the repository for [bankstatementparser.com][00], the digital presence of
Bank Statement Parser, a Python library built for Finance and Treasury Professionals.

## Quick Start Guide

Setting up and running the website locally is easy and quick with the
[Shokunin Static Site Generator (SSG)][00].

### Prerequisites

Ensure you have the **Rust toolchain** installed. If not, follow the guide on
the [Rust website][01] to set it up.

### Installation & Usage

1. Install Shokunin SSG:

```shell
cargo install ssg
```

2. Clone the repository

```shell
git clone https://github.com/sebastienrousseau/bankstatementparser.github.io.git
```

3. Change into the repository directory:

```shell
cd bankstatementparser.github.io
```

4. Generate the static site for bankstatementparser.com:

```shell
ssg -n=docs -c=_posts -t=_layouts -o=output -s=public
```


[00]: https://bankstatementparser.com "Bank Statement Parser Official Website"
[01]: https://www.rust-lang.org/learn/get-started "Rust Getting started guide"
