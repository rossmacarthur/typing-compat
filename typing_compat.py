import collections
import typing


__all__ = ['get_args', 'get_origin']
__title__ = 'typing-compat'
__version__ = '0.1.0'
__url__ = 'https://github.com/rossmacarthur/typing-compat'
__author__ = 'Ross MacArthur'
__author_email__ = 'ross@macarthur.io'
__description__ = 'Python typing compatibility library'


try:
    # Python >=3.8 should have these functions already
    from typing import get_args as _get_args
    from typing import get_origin as _get_origin
except ImportError:
    if hasattr(typing, '_GenericAlias'):  # Python 3.7

        def _get_origin(tp):
            """Copied from the Python 3.8 typing module"""
            if isinstance(tp, typing._GenericAlias):
                return tp.__origin__
            if tp is typing.Generic:
                return typing.Generic
            return None

        def _get_args(tp):
            """Copied from the Python 3.8 typing module"""
            if isinstance(tp, typing._GenericAlias):
                res = tp.__args__
                if (
                    get_origin(tp) is collections.abc.Callable
                    and res[0] is not Ellipsis
                ):
                    res = (list(res[:-1]), res[-1])
                return res
            return ()

    else:  # Python <3.7

        def _get_origin(tp):
            """Emulate the behaviour of Python 3.8 typing module"""
            if isinstance(tp, typing._ClassVar):
                return typing.ClassVar
            elif isinstance(tp, typing._Union):
                return typing.Union
            elif isinstance(tp, typing.GenericMeta):
                if hasattr(tp, '_gorg'):
                    tp = tp._gorg
                    if hasattr(tp, '__mro__'):
                        for t in tp.__mro__:
                            if t.__module__ == 'builtins' and t is not object:
                                return t
                    return tp
                else:
                    while tp.__origin__ is not None:
                        tp = tp.__origin__
                    return tp

        def _normalize_arg(args):
            if isinstance(args, tuple) and len(args) > 1:
                base, rest = args[0], tuple(_normalize_arg(arg) for arg in args[1:])
                if isinstance(base, typing.CallableMeta):
                    return typing.Callable[list(rest[:-1]), rest[-1]]
                elif isinstance(base, (typing.GenericMeta, typing._Union)):
                    return base[rest]
            return args

        def _get_args(tp):
            """Emulate the behaviour of Python 3.8 typing module"""
            if isinstance(tp, typing._ClassVar):
                return (tp.__type__,)
            elif hasattr(tp, '_subs_tree'):
                tree = tp._subs_tree()
                if isinstance(tree, tuple) and len(tree) > 1:
                    if isinstance(tree[0], typing.CallableMeta) and len(tree) == 2:
                        return ([], _normalize_arg(tree[1]))
                    return tuple(_normalize_arg(arg) for arg in tree[1:])
            return ()


def get_origin(tp):
    """
    Get the unsubscripted version of a type.

    This supports generic types, Callable, Tuple, Union, Literal, Final and
    ClassVar. Returns None for unsupported types.

    Examples:

        get_origin(Literal[42]) is Literal
        get_origin(int) is None
        get_origin(ClassVar[int]) is ClassVar
        get_origin(Generic) is Generic
        get_origin(Generic[T]) is Generic
        get_origin(Union[T, int]) is Union
        get_origin(List[Tuple[T, T]][int]) == list
    """
    return _get_origin(tp)


def get_args(tp):
    """
    Get type arguments with all substitutions performed.

    For unions, basic simplifications used by Union constructor are performed.

    Examples:

        get_args(Dict[str, int]) == (str, int)
        get_args(int) == ()
        get_args(Union[int, Union[T, int], str][int]) == (int, str)
        get_args(Union[int, Tuple[T, int]][str]) == (int, Tuple[str, int])
        get_args(Callable[[], T][int]) == ([], int)
    """
    return _get_args(tp)
