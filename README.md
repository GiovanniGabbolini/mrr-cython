

mrr-cython
==========
![PY_PIC]
[![BUILD_STATUS_PIC]][BUILD_STATUS_LINK]

## Description
Fast implementation of the MRR ranking metric. Suitable to be used as custom metric in ranking algorithms, as they really ofter do not support it as a built-in ranking metric.

## Blazingly fast
The code is written in Cython and therefore can be used in Python natively, but still is fast as C code.

## Installation
You should build the Cython source code before using the function
Do it by:
<pre>
python setup.py build_ext --inplace
</pre>

## Example
See example.py for a complete example

#### License
Released under the MIT License

[DOI_PIC]: https://zenodo.org/badge/DOI/10.5281/zenodo.2583851.svg
[DOI_LINK]: https://doi.org/10.5281/zenodo.2583851
[LICENSE_PIC]: https://img.shields.io/github/license/bogliosimone/similaripy.svg
[LICENSE_LINK]: https://github.com/bogliosimone/similaripy/blob/master/LICENSE
[PYPI_PIC]: https://img.shields.io/pypi/v/similaripy.svg
[PYPI_LINK]: https://pypi.org/project/similaripy/
[PY_PIC]: https://img.shields.io/pypi/pyversions/similaripy.svg
[BUILD_STATUS_PIC]: https://travis-ci.org/bogliosimone/similaripy.svg?branch=master
[BUILD_STATUS_LINK]: https://travis-ci.org/bogliosimone/similaripy
