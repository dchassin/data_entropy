[[Data entropy]] - compute the entropy of a data set

# Synopsis

Python3:

~~~
data_entropy(data)
~~~

# Description

The data entropy estimate computes the actual and maximum possible entropy
of the data set given its size.  The actual entropy of a data set is 
computed as

$$
	\log(len(unique(data))) / \log(2)
$$

and the maximum possible entropy is

$$
	\log(len(data)) / \log(2)
$$

The values returned can be interpreted as the number of bits of resolution
observed in the data.  The actual number of bits cannot exceed the
resolution possible given the underlying representation. For example
8-bit data will never return a data entropy greater than 8, even when
the total entropy possible of a data set larger than 256 samples is larger
than 8. 

# Caveat

If a low resolution dataset has been filtered or subect to noise, then 
it may have a unique entropy that is higher than expected.  Similarly, if a
high resolution data has been filtered or subject to lossy compression, then
it may have a unique entropy that is lower than expected. This can be used
to detect whether a dataset has be subject to filtering, noise, or lossy
compression.

# Example

~~~
bash$ python3
Python 3.7.6 (default, Dec 30 2019, 19:38:36) 
[Clang 10.0.0 (clang-1000.11.45.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import data_entropy
>>> import numpy as np
>>> data_entropy.data_entropy(np.random.randint(0,256,1000000))
{'unique': 8.0, 'total': 19.931568569324174}
~~~
