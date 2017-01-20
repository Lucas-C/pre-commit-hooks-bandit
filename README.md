[![](https://travis-ci.org/Lucas-C/pre-commit-hooks-bandit.svg?branch=master)](https://travis-ci.org/Lucas-C/pre-commit-hooks-bandit)

A pre-commit to find common security issues in your Python code using [bandit](//pypi.python.org/pypi/bandit).

You can check the [plugins list](/openstack/bandit/tree/master/bandit/plugins) & [examples](/openstack/bandit/tree/master/examples) for tangible use cases.


## Usage
```
-   repo: https://github.com/Lucas-C/pre-commit-hooks-bandit
    sha: v1.0.2
    hooks:
    -   id: python-bandit-vulnerability-check
```

You can also specify a custom `.banditrc` file, directories to check, test IDs to skip or the alerting level:
```
    -   id: python-bandit-vulnerability-check
        args: [--verbose, --ini, .banditrc, -ll, --skip, "B321,B402", --recursive, src/lib]
```


## Alternative local hook
You'll need to `pip install bandit` beforehand:
```
-   repo: local
    hooks:
    -   id: python-bandit-vulnerability-check
        entry: bandit
        args: [-lll, --recursive, .]
        language: system
        files: ''
```
