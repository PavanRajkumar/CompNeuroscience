# Author : Pavan Rajkumar Magesh

import numpy as np
import pickle

FILENAME = 'pop_coding_3.4.pickle'

with open(FILENAME, 'rb') as f:
    data = pickle.load(f)

c = [data['c1'], data['c2'], data['c3'], data['c4']]
r = [data['r1'], data['r2'], data['r3'], data['r4']]

basis_vector = []
for rr, cc in zip(r, c):
    # Calculate the weighted basis vector
    nr = rr / rr.max()
    mean_vector = np.outer(nr, cc).mean(axis=0)

    # Normalize the vector
    mean_vector /= np.sqrt(np.inner(mean_vector, mean_vector))

    basis_vector.append(mean_vector)

print('Weighted basis vectors: %s' % basis_vector)

# Only take the first two, because the rest are nan
pop_vector = np.nansum(basis_vector, axis=0)
pop_vector /= np.sqrt(np.inner(pop_vector, pop_vector))

print('Population Vector (X, Y): %s' % pop_vector)
print('Population vector in polar coordinates: %f' % np.arctan(pop_vector[1]/pop_vector[0]))
