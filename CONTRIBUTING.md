# Contributing to WholeTroutMedia Open-Source Reference Micro-Tools

Thank you for contributing. Every tool in this repository is self-contained, uses only the Python standard library, and ships with a deterministic `verify_app.py` check.

## Local Setup

Requires Python 3.10 or newer with no external packages:

```bash
git clone https://github.com/WholeTroutMedia/open-source-micro-tools.git
cd open-source-micro-tools
for script in apps/*/verify_app.py; do python3 "$script"; done
```

## Pull Request Checklist

1. Keep changes scoped to a single micro-application or issue.
2. Avoid adding third-party runtime dependencies; stick to the Python standard library.
3. Add or update assertions in the matching `apps/<slot>/verify_app.py` script so your change is covered end to end.
4. Run all verification scripts locally and confirm every suite exits with code `0`.
5. Keep pull request descriptions short and clear: state what changed, why, and how you tested it.

## Finding Something to Work On

Browse issues labeled `good first issue` or `help wanted`, or open an issue describing a bug or feature before starting a large refactor.

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](./LICENSE).
