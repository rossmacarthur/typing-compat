import doctest
import sys
import typing as ty

import pytest

from typing_compat import get_args, get_origin


@pytest.mark.skipif(sys.version_info < (3,), reason='requires Python 3')
def test_readme():
    failures, _ = doctest.testfile('README.md')
    assert not failures, 'doctests in README failed'


def test_get_origin():
    if hasattr(ty, 'Literal'):
        assert get_origin(ty.Literal[42]) is ty.Literal
    assert get_origin(int) is None
    assert get_origin(ty.ClassVar[int]) is ty.ClassVar
    assert get_origin(ty.Generic) is ty.Generic
    assert get_origin(ty.Generic[ty.T]) is ty.Generic
    assert get_origin(ty.Union[ty.T, int]) is ty.Union
    assert get_origin(ty.List[ty.Tuple[ty.T, ty.T]][int]) == list


def test_get_args():
    assert get_args(ty.Dict[str, int]) == (str, int)
    assert get_args(int) == ()
    assert get_args(ty.Union[int, ty.Union[ty.T, int], str][int]) == (int, str)
    assert get_args(ty.Union[int, ty.Tuple[ty.T, int]][str]) == (
        int,
        ty.Tuple[str, int],
    )
    assert get_args(ty.Callable[[], ty.T][int]) == ([], int)
    assert get_args(ty.List[ty.Tuple[ty.T, ty.T]][int]) == (ty.Tuple[int, int],)
    assert get_args(ty.Dict[int, ty.Tuple[ty.T, ty.T]][ty.Optional[int]]) == (
        int,
        ty.Tuple[ty.Optional[int], ty.Optional[int]],
    )
    assert get_args(ty.Union[int, ty.Callable[[ty.Tuple[ty.T, ...]], str]]) == (
        int,
        ty.Callable[[ty.Tuple[ty.T, ...]], str],
    )
