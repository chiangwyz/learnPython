import numpy as np

a = [3, 4, 5]
b = [5]
c = [12]

bool_a_b = np.sum(a) == np.sum(b)
# bool_a_b = (np.sum(a) == np.sum(b))
print("bool_a_b =", bool_a_b)

bool_a_c = (np.sum(a) == np.sum(c))
print("bool_a_c =", bool_a_c)