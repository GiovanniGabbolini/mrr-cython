# mrr-cython

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
