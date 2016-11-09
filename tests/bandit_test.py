from __future__ import absolute_import
from __future__ import unicode_literals

import sys

from pre_commit_hooks.bandit import main as bandit


def test_this_repo(tmpdir):
    output = tmpdir.join('output.txt')
    sys.argv = [sys.argv[0], '--verbose', '-lll', '--recursive', '.', '--output', str(output)]
    assert bandit() == 0
