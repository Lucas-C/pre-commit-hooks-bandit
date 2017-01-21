[![](https://travis-ci.org/Lucas-C/pre-commit-hooks-bandit.svg?branch=master)](https://travis-ci.org/Lucas-C/pre-commit-hooks-bandit)

A pre-commit hook to find common security issues in your Python code using [bandit](//pypi.python.org/pypi/bandit).

You can check the [plugins list](/openstack/bandit/tree/master/bandit/plugins) & [examples](/openstack/bandit/tree/master/examples) for tangible use cases.


## Usage
```
-   repo: https://github.com/Lucas-C/pre-commit-hooks-bandit
    sha: v1.0.2
    hooks:
    -   id: python-bandit-vulnerability-check
```

You can also specify a custom `.banditrc` file, specific directories to check, test IDs to skip or the alerting level :
```
    -   id: python-bandit-vulnerability-check
        args: [--verbose, --ini, .banditrc, -ll, --skip, "B321,B402", --recursive, src/lib]
```

The default arguments are defined [here](https://github.com/Lucas-C/pre-commit-hooks-bandit/blob/master/hooks.yaml#L6) and indicate to check for high-severity issues in all the repo files recursively.

Note that `pre-commit` will pass to `bandit` the list of all staged files that match the `files` regular expression in `.pre-commit-config.yaml`.

If you want to execute `bandit` only on modified Python files, you'll need:

- to target the Python files / directories with the `files` field in `.pre-commit-config.yaml`
- to override the `args` field so it does not include `--recursive`

```
    -   id: python-bandit-vulnerability-check
        args: []
        files: .py$
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
