import unittest
import uuid
import random

from server import GoodHasher


class GoodHasherTest(unittest.TestCase):
    def test_comparison(self):
        for seed in range(0, 7_777_777, 6666):
            hasher = GoodHasher(seed)

            for _ in range(1000):
                size = random.randint(3, 32)
                val = uuid.uuid4().hex[:size]
                hashed = hasher.hash(val)

                self.assertTrue(hasher.compare_with_hash(val, hashed))


if __name__ == '__main__':
    unittest.main()
