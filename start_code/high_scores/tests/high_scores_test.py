import unittest

from src.high_scores import latest, personal_best, personal_top_three, hi_to_low_scores

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):

    def setUp(self):

        self.list_1 = [34, 54, 765, 234, 1, 32, 764, 98, 901, 378, 811]

    # Tests
    # Test latest score (the last thing in the list)
    def test_latest(self):
        get_latest_score = latest(self.list_1)
        self.assertEqual(811, get_latest_score)
    # Test personal best (the highest score in the list)
    def test_personal_best(self):
        get_personal_best = personal_best(self.list_1)
        self.assertEqual(901, get_personal_best)
    # Test top three from list of scores
    def test_personal_top_three(self):
        get_personal_top_three = personal_top_three(self.list_1)
        self.assertEqual([901, 811, 765], get_personal_top_three)
    # Test ordered from highest tp lowest
    def test_high_score_to_low_score(self):
        get_hi_to_low_scores = hi_to_low_scores(self.list_1)
        self.assertEqual([901, 811, 765, 764, 378, 234, 98, 54, 34, 32, 1], get_hi_to_low_scores)
    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
