A pre-commit to find common security issues in your Python code using [bandit](//pypi.python.org/pypi/bandit).

You can check the [plugins list](/openstack/bandit/tree/master/bandit/plugins) & [examples](/openstack/bandit/tree/master/examples) for tangible use cases.


## Usage
```
-   repo: https://github.com/Lucas-C/pre-commit-hooks-bandit
    sha: v1.0.1
    hooks:
    -   id: python-bandit-vulnerability-check
```

You can also specify directories to check, a custom `.banditrc` file or the alerting level:
```
    -   id: python-bandit-vulnerability-check
        args: [--verbose, --ini, .banditrc, -ll, --recursive, src/lib]
```


## Alternative local hook
You'll need to `pip install bandit` beforehand:
```
-   repo: local
    hooks:
    -   id: python-bandit-vulnerability-check
        entry: bandit
        args: [--verbose, -lll, --recursive, .]
        language: system
        files: ''
```
