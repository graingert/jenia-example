from __future__ import annotations

from ..program import A


def test_foo(capsys):
    A().f()
    assert capsys.readouterr() == ("hello\n", "")
