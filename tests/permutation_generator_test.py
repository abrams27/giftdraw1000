import unittest

from server.permutation_generator import PermutationGenerator


class PermutationGeneratorTest(unittest.TestCase):

    def test_should_return_permutation_without_identity(self):
        for seed in range(1_000_000):
            generator = PermutationGenerator(seed)
            perm = list(range(7))
            result = generator.permutate_without_identity(perm)

            self.validate_perm(perm, result)

    def validate_perm(self, perm1, perm2):
        for a, b in zip(perm1, perm2):
            self.assertNotEqual(a, b)


if __name__ == '__main__':
    unittest.main()
