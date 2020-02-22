# typing-compat

Python typing compatibility library.

In Python >=3.8 the `typing.get_origin` and `typing.get_args` functions are
provided. This library aims to bring the identical behaviour of these functions
to other versions of Python.

## Getting started

```bash
pip install typing-compat
```

## Usage

```python
>>> from typing import List, Tuple, TypeVar
>>> from typing_compat import get_args, get_origin
>>> T = TypeVar('T')

>>> tp = List[Tuple[T, T]][int]

>>> get_args(tp)
(typing.Tuple[int, int],)

>>> get_origin(tp)
<class 'list'>

```

## License

This library is licensed under either of

- Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE) or
  https://www.apache.org/licenses/LICENSE-2.0)
- MIT License ([LICENSE-MIT](LICENSE-MIT) or
  https://opensource.org/licenses/MIT)

at your option.
