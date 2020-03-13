"""Data Entropy Analysis Tools
"""
import numpy as np
import random

def data_entropy(data):
	"""Estimate the data entropy

	Parameters:
		data (np.array) - data samples

	Returns:
		dict
			unique - actual entropy of data set
			total - maximum possible entropy of data set

	The data entropy estimate computes the actual and maximum possible entropy
	of the data set given its size.  The actual entropy of a data set is 
	computed as

		log(len(unique(data))) / log(2)

	and the maximum possible entropy is

		log(len(data)) / log(2)

	The values returned can be interpreted as the number of bits of resolution
	observed in the data.  The actual number of bits cannot exceed the
	resolution possible given the underlying representation. For example
	8-bit data will never return a data entropy greater than 8, even when
	the total entropy possible of a data set larger than 256 samples is larger
	than 8. 

	Note: If a low resolution dataset has been filtered or subect to noise, then 
	it may have a unique entropy that is higher than expected.  Similarly, if a
	high resolution data has been filtered or subject to lossy compression, then
	it may have a unique entropy that is lower than expected. This can be used
	to detect whether a dataset has be subject to filtering, noise, or lossy
	compression.
	"""
	unique = len(np.unique(data))
	length = len(data)
	return {"unique" : np.log(unique)/np.log(2), "total": np.log(length)/np.log(2)}

def selftest():
	N = 10000
	
	print(f"N samples........... {N}")
	data = np.random.randint(0,256,N)
	entr = data_entropy(data)
	print("8 bit data clean.... %.1f / %.1f" % (entr["unique"],entr["total"]))

	data = np.random.normal(0,0.01,N) + data
	entr = data_entropy(data)
	print("8 bit data noisy.... %.1f / %.1f" % (entr["unique"],entr["total"]))

	data = np.random.randint(0,65536,N)
	entr = data_entropy(data)
	print("16 bit data clean... %.1f / %.1f" % (entr["unique"],entr["total"]))

	data = np.random.normal(0,0.01,N) + data
	entr = data_entropy(data)
	print("16 bit data noisy... %.1f / %.1f" % (entr["unique"],entr["total"]))

if __name__ == '__main__':
	selftest()