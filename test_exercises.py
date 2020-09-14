import unittest
import exercises

class TestAlgorithmExercises(unittest.TestCase):

    def test_sumUpToK(self):
        # When
        subject = exercises.sumUpToK([1, 2], 100)
        subject2 = exercises.sumUpToK([1, 99], 100)
        subject3 = exercises.sumUpToK([], 100)
        subject4 = exercises.sumUpToK([5, 4, 1, -3, 6], 7)

        # Then
        self.assertFalse(subject)
        self.assertTrue(subject2)
        self.assertFalse(subject3)
        self.assertTrue(subject4)

    def test_firstRepeatingCharacter(self):
        self.assertTrue(True)