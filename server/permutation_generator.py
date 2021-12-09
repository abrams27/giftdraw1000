import random


class PermutationGenerator:

    def __init__(self, seed):
        random.seed(seed)

    def permutate_without_identity(self, permutation):
        list_to_permutate = permutation.copy()
        random.shuffle(list_to_permutate)

        while self.has_identity(permutation, list_to_permutate):
            random.shuffle(list_to_permutate)

        return list_to_permutate

    @staticmethod
    def has_identity(perm1, perm2):
        for a, b in zip(perm1, perm2):
            if a == b:
                return True
        return False
