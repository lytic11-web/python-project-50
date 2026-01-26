### Hexlet tests and linter status:
[![Actions Status](https://github.com/lytic11-web/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/lytic11-web/python-project-50/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=lytic11-web_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=lytic11-web_python-project-50)
[![Python CI](https://github.com/lytic11-web/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/lytic11-web/python-project-50/actions/workflows/pyci.yml)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=lytic11-web_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=lytic11-web_python-project-50)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=lytic11-web_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=lytic11-web_python-project-50)

### Description
This project is a difference generator (diff) for configuration files (JSON, YAML). It supports multiple output formats: stylish, plain, and json.

### Built with

| Tool | Description |
|------|-------------|
| [uv](https://github.com/astral-sh/uv) | An extremely fast Python package and project manager, written in Rust |
| [pytest](https://github.com/pytest-dev/pytest) | A mature full-featured Python testing tool |
| [ruff](https://github.com/astral-sh/ruff) | An extremely fast Python linter and code formatter, written in Rust |


### Installation

#### Clone the repository
```bash
git clone https://github.com/lytic11-web/python-project-50.git
cd python-project-50
```
####  Install dependencies
```bash
make install
```
###  Usage
```bash
gendiff [--format FORMAT] filepath1 filepath2
```
###  Options
```bash
 --format, -f - output format (stylish, plain, json). Default: stylish
```
###  Examples

#### Stylish format (default)
```bash
uv run gendiff tests/test_data/nested/file1.json tests/test_data/nested/file2.json
```

#### Plain format
```bash
uv run gendiff --format plain tests/test_data/nested/file1.json tests/test_data/nested/file2.json
```

#### JSON format
```bash
uv run gendiff --format json tests/test_data/flat/file1.json tests/test_data/flat/file2.json
```
###  Supported formats

####  Output formats:

- stylish - formatted output with indentation (default)
- plain - flat text format with change descriptions
- json - structured JSON output

####  Input file formats:

- JSON (.json)
- YAML (.yml, .yaml)

### Running tests

```bash
# Run all tests
make test

# Run tests with coverage
make test-coverage

# Run linter
make lint

# Run all checks (tests + lint)
make check

# Format code
make format

# Build package
make build
```

###  License

This project is part of the Hexlet Python Developer course.


### Demo

- [Comparison](https://asciinema.org/a/ASIrCBXGMmiDIYUd)
- [Comparison.yml](https://asciinema.org/a/ul3zYRrAPbzO6ELl)
- [Comparison.tree.json](https://asciinema.org/a/Nsy7UZPGfnfUTiqd)
- [Comparison.format.plain](https://asciinema.org/a/M1gR0CeuC5JzwJL0)
- [Comparison.format.json](https://asciinema.org/a/TxouT8yniSStfbVX)
