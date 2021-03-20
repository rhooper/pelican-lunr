name: Semantic Release

on:
  push:
    branches:
      - master

jobs:
  release:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
      with:
        fetch-depth: 0

    - name: Python Semantic Release
      uses: relekang/python-semantic-release@master
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        pypi_token: ${{ secrets.PYPI_TOKEN }}
