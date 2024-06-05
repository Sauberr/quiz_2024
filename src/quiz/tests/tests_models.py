from django.core.exceptions import ValidationError
from django.test import TestCase

from core.utils.samples import sample_question, sample_quiz
from quiz.models import Quiz


class TestQuizModel(TestCase):
    def setUp(self) -> None:
        self.question_count = 10
        self.test_quiz = sample_quiz(title='Test_Quiz')
        for i in range(self.question_count):
            sample_question(quiz=self.test_quiz, order_number=i)

    def tearDown(self) -> None:
        self.test_quiz.delete()

    def test_questions_count(self):
        self.assertEqual(self.question_count, self.test_quiz.questions_count())

    def test_title_limit(self):
        with self.assertRaises(ValidationError):
            sample_quiz(title="A" * 7000)

        self.assertEqual(Quiz.objects.count(), 1)

    def test_title(self):
        self.assertEqual(self.test_quiz.title, 'Test_Quiz')

    def test_description_limit(self):
        with self.assertRaises(ValidationError):
            sample_quiz(title='A', description='T' * 20000)

        self.assertEqual(Quiz.objects.count(), 1)

    def test_text_limit(self):
        with self.assertRaises(ValidationError):
            sample_question(quiz=self.test_quiz, order_number=1, text='A' * 20000)

        self.assertEqual(self.test_quiz.questions.count(), self.question_count)

