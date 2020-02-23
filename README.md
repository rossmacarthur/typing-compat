<h1 align="center">typing-compat</h1>
<div align="center">
  <strong>Python typing compatibility library</a></strong>
</div>
<br />
<div align="center">
  <a href="https://github.com/rossmacarthur/typing-compat/actions?query=workflow%3Abuild">
    <img src="https://github.com/rossmacarthur/typing-compat/workflows/build/badge.svg?branch=master" alt="Build status" />
  </a>
  <a href="https://github.com/psf/black">
    <img src="https://img.shields.io/badge/code%20style-black-101010.svg" alt="Code style: black" />
  </a>
</div>
<br />

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
