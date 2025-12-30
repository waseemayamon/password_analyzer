name: Password Analyzer CI

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8

    - name: Lint with flake8
      run: |
        flake8 password_analyzer.py --max-line-length=100

    - name: Run basic execution test
      run: |
        python password_analyzer.py TestPass123!

