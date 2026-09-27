# Release signing keys

Every release tag is an annotated, cryptographically signed Git tag. Verify a tag with:

```sh
git fetch --tags --force
git tag -v v0.0.1
```
