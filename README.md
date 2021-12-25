# pdoc sample

## setup

```sh
poetry install
```

## Generate documents

Docs will be generated automatically via GitHub Actions.<br>
If you do it manually, please run the below command.

```sh
poetry run pdoc --html -o docs --force main.py
```
