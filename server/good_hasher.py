import hashlib


class GoodHasher:

    def __init__(self, seed):
        self.seed = seed

    def compare_with_hash(self, val, hash_to_compare):
        return hash_to_compare == self.hash(val)

    def hash(self, val):
        val_with_seed = "{}-{}-{}".format(self.seed * 21, val, self.seed * 37).encode()
        return hashlib.sha512(val_with_seed).hexdigest()
