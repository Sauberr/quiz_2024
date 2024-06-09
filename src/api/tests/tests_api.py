from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED)
from rest_framework.test import APIClient

from core.utils.samples import sample_question, sample_quiz
from quiz.models import Category


class TestApi(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.quiz = sample_quiz(level=1, title="Tests", description="Tests")
        self.question = sample_question(quiz=self.quiz, order_number=1)

        self.user = get_user_model().objects.create(email="test_api@gmail.com")
        self.user.set_password("1234567890")
        self.user.save()

    def test_question_detail(self):
        self.client.force_authenticate(user=self.user)

        result = self.client.get(
            reverse("api:question_details", kwargs={"pk": self.quiz.pk, "order": self.question.order_number})
        )
        self.assertEqual(result.status_code, HTTP_200_OK)
        self.assertEqual(
            result.data,
            {
                "id": 1,
                "order_number": 1,
                "text": "What is the capital of France?",
                "choices": [],
            },
        )

    def test_question_detail_no_access(self):
        result = self.client.get(
            reverse("api:question_details", kwargs={"pk": self.quiz.pk, "order": self.question.order_number})
        )
        self.assertEqual(result.status_code, HTTP_401_UNAUTHORIZED)

    def test_quiz_list(self):
        result = self.client.get(reverse("api:quiz_list"))
        self.assertEqual(result.status_code, HTTP_200_OK)

    def test_create_category(self):
        self.user = get_user_model().objects.create_superuser(email="apitest@gmail.com", is_staff=True)
        self.user.set_password("1234567890")
        self.client.force_authenticate(user=self.user)
        payload = {
            "name": "Test Category",
        }
        result = self.client.post(reverse("api:category_create"), payload)
        self.assertEqual(result.status_code, HTTP_201_CREATED)

        category = Category.objects.get(id=result.data["id"])
        for k, v in payload.items():
            self.assertEqual(getattr(category, k), v)
        self.assertEqual(category.name, "Test Category")

    def test_delete_category(self):
        self.user = get_user_model().objects.create_superuser(email="apitest@gmail.com", is_staff=True)
        self.user.set_password("1234567890")
        self.client.force_authenticate(user=self.user)
        category = Category.objects.create(name="Test Category")
        result = self.client.delete(reverse("api:category_delete", kwargs={"pk": category.pk}))
        self.assertEqual(result.status_code, HTTP_204_NO_CONTENT)
        categories = Category.objects.filter(pk=category.pk)
        self.assertFalse(categories.exists())

    def test_category_create_url(self):
        result = self.client.get(reverse("api:category_create"))
        self.assertEqual(result.status_code, HTTP_401_UNAUTHORIZED)
