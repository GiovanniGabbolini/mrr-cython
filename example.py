from mrr import mrr
import numpy as np

# in this case, we have two queries, each of one composed of 3 elements,
# as indicated by the array groups.
# in label, we have the labels for any of the 3 documents in the two queries
# in prediction, we have the scores assigned by the algorithm to the documents 
label = np.array([0, 1, 0, 1, 0, 0], dtype=np.int32)
prediction = np.array([0.1, 0.2, 0.3, 1, 0.5, 0], dtype=np.float32)
groups = np.array([3,3], dtype=np.int32)

# as expected, this prints 0.75
print(mrr(memoryview(label),
	  memoryview(prediction),
          memoryview(groups),
          len(groups)))
