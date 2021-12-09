import unittest

from server import RandomDrawer


class RandomDrawerTest(unittest.TestCase):

    def test_should_create_a_draw(self):
        for seed in range(0, 7_777_777, 6666):
            random_drawer = RandomDrawer(seed)
            participants = ['user0', 'user1', 'user2', 'user3', 'user4']
            draw = random_drawer.create_draw(participants)

            recipients = list(map(lambda x: random_drawer.get_recipient(x[1]), draw))

            self.assertEqual(None, random_drawer.get_recipient("wronghash"))
            self.assertEqual(len(set(recipients)), len(recipients))
            for a, b in zip(participants, draw):
                self.assertNotEqual(a, b)


if __name__ == '__main__':
    unittest.main()
