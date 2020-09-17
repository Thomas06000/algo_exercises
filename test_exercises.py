import unittest
import exercises

class TestAlgorithmExercises(unittest.TestCase):

    def test_sumUpToK(self):
        subject = exercises.sumUpToK([1, 2], 100)
        subject2 = exercises.sumUpToK([1, 99], 100)
        subject3 = exercises.sumUpToK([], 100)
        subject4 = exercises.sumUpToK([5, 4, 1, -3, 6], 7)

        self.assertFalse(subject)
        self.assertTrue(subject2)
        self.assertFalse(subject3)
        self.assertTrue(subject4)

    def test_firstRepeatingCharacter(self):
        subject = exercises.firstRepeatingCharacter(str= "inside code")
        subject2 = exercises.firstRepeatingCharacter(str= "toulouse")
        subject3 = exercises.firstRepeatingCharacter(str= "azerty")
        subject4 = exercises.firstRepeatingCharacter(str= "mississipi")

        self.assertEqual(subject, "i")
        self.assertEqual(subject2, "o")
        self.assertEqual(subject3, "\0")
        self.assertEqual(subject4, "s")

    def test_generateMatchingParenthesis(self):
        subject = exercises.generateMatchingParenthesis(3)
        self.assertTrue(subject)