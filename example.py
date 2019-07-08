from mrr import mrr
import numpy as np

label = np.array([0, 1, 0, 1, 0, 0], dtype=np.int32)
prediction = np.array([0.1, 0.2, 0.3, 1, 0.5, 0], dtype=np.float32)
groups = np.array([3,3], dtype=np.int32)

print(mrr(memoryview(label),
	  memoryview(prediction),
          memoryview(groups),
          len(groups)))
