import unittest
import numpy as np

from gram import orthogonalization

class TestOrthogonalization(unittest.TestCase):
    def test_orthogonalization_vals(self):
        v1 = np.array([2, -2, 0, 0])
        v2 = np.array([1, 0, 1, 1])
        v3 = np.array([1, 0, 1, 0])

        u1 = np.array([2, -2, 0, 0])
        u2 = np.array([0.5, 0.5, 1, 1])
        u3 = np.array([0.2, 0.2, 0.4, -0.6])
        ortho_vectors = orthogonalization([v1, v2, v3])
        w1 = ortho_vectors[0].tolist()
        w2 = ortho_vectors[1].tolist()
        w3 = ortho_vectors[2].tolist()

        np.testing.assert_equal(u1, w1)
        np.testing.assert_equal(u2, w2)
        np.testing.assert_equal(u3, w3)

