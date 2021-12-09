from server import PermutationGenerator, GoodHasher


class RandomDrawer:

    def __init__(self, seed):
        self.permutation_generator = PermutationGenerator(seed)
        self.good_hasher = GoodHasher(seed)
        self.participants = []
        self.permutation = []

    def create_draw(self, participants):
        self.participants = participants
        self.permutation = self.permutation_generator.permutate_without_identity(participants)

        return list(map(lambda x: (x, self.good_hasher.hash(x)), participants))

    def get_recipient(self, participant_hash):
        for a, b in zip(self.participants, self.permutation):
            if self.good_hasher.compare_with_hash(a, participant_hash):
                return b

        return None
