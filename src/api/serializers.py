from rest_framework.serializers import CharField, ModelSerializer

from account.models import Customer
from quiz.models import Category, Choice, Question, Quiz


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            "first_name",
            "last_name",
            "email",
            "is_staff",
        )


class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = (
            "id",
            "text",
            "is_correct",
        )


class QuestionSerializer(ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = (
            "id",
            "order_number",
            "text",
            "choices",
        )


class QuizSerializer(ModelSerializer):
    level = CharField(source="get_level_display")

    class Meta:
        model = Quiz
        fields = (
            "id",
            "title",
            "description",
            "level",
            "questions_count",
        )


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
        )
