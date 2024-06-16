# Versioning

This package follows Semantic Versioning (SemVer) to ensure clear and predictable versioning for our users. The version format is `MAJOR.MINOR.PATCH`.

## Compatibility Table
|Package Version|Compatible Logto API Versions|
|---|---|
|`1.0.x`|`1.16 - 1.17`|

This table lists the known compatible versions of the Logto API. However, the package **might be compatible with other versions** of the Logto API that are not explicitly listed here. If you find compatibility with a version not listed, please let us know by opening an issue or contributing to our repository.

## Compatibility with Logto REST API
Our package is a wrapper around the Logto Management API, and its functionality is directly tied to specific versions of the Logto API. Below is our versioning strategy to help you understand the compatibility and expected changes:

- Patch Version (`x.y.z`):
    - Incremented for backward-compatible bug fixes or minor improvements in this package.
    - Indicates no changes in the Logto API version compatibility.

- Minor Version (`x.y.0`):
    - Incremented for backward-compatible new features or improvements.
    - May also be incremented when the Logto API introduces backward-compatible changes that our package supports.

- Major Version (`x.0.0`):
    - Incremented for backward-incompatible changes in this package.
    - Also incremented when adapting to breaking changes in the Logto API, indicating that the new package version may not be compatible with previous versions of the Logto API.

Specifying Dependencies
In your `setup.py` or `pyproject.toml`, we specify the compatible versions of the Logto API to ensure your project uses the correct versions:

```toml
# pyproject.toml
[tool.poetry.dependencies]
logto-admin = ">=1.0.0,<2.0.0"
```

```python
# setup.py
install_requires=[
    'logto-api-client>=1.17.0,<2.0.0'
]
```

## Example Scenarios

- If we add a new feature to the package that is backward-compatible and the Logto API remains at version `1.17.0`, the new package version will be `1.1.0`.
- If the Logto API is updated to version `1.18.0` with backward-compatible changes and our package starts utilizing these features, the new package version will be `1.2.0`.
- If the Logto API is updated to version `2.0.0` with breaking changes and our package adapts to these changes, the new package version will be `2.0.0`.

## Summary

We aim to make the versioning of our package as clear and predictable as possible. Please refer to the compatibility table above to understand which version of the Logto API our package supports. If you have any questions or encounter any issues, feel free to open an issue on our GitHub repository.