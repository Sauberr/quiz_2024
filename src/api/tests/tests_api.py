from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework.test import APIClient

from core.utils.samples import sample_question, sample_quiz


class TestApi(TestCase):
    def setUP(self) -> None:
        self.client = APIClient()
        self.quiz = sample_quiz(level=1, title="Tests", description="Tests")
        self.question = sample_question(quiz=self.quiz, order_number=1)

        self.user = get_user_model().objects.create(email="test_api@gmail.com")
        self.user.set_password("1234567890")
        self.user.save()

    def test_question_detail(self):
        self.client.force_authenticate(user=self.user)

        result = self.client.get(
            reverse("api:question-details", kwargs={"pk": self.quiz.pk, "order": self.question.order_number})
        )
        self.assertEqual(result.status_code, HTTP_200_OK)
        self.assertEqual(
            result.data,
            {
                "id": 1,
                "order_number": 1,
                "text": "Test question",
                "choices": [],
            },
        )

    def test_question_detail_no_access(self):
        result = self.client.get(
            reverse("api:question-details", kwargs={"pk": self.quiz.pk, "order": self.question.order_number})
        )
        self.assertEqual(result.status_code, HTTP_401_UNAUTHORIZED)
