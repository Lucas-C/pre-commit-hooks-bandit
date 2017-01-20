from __future__ import absolute_import
from __future__ import unicode_literals

import sys

from pre_commit_hooks.bandit_analyzer import main as bandit


def test_this_repo(tmpdir):
    # an explicit output file is need with py.test to avoid a strange bug
    sys.argv = [sys.argv[0], '--verbose', '-lll', '--recursive', '.', '--output', str(tmpdir.join('output.txt'))]
    assert bandit() == 0

def test_medium_level_vulnerability_eval(tmpdir):
    eval_py = tmpdir.join('eval.py')
    eval_py.write('eval("1+1")')
    sys.argv = [sys.argv[0], '--verbose', '-ll', str(eval_py), '--output', str(tmpdir.join('output.txt'))]
    assert bandit() == 1
