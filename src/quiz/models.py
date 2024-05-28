from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=255)


class Quiz(models.Model):
    QUESTION_MAX_LIMIT = 20
    QUESTION_MIN_LIMIT = 3
    class LEVEL_CHOICES(models.IntegerChoices):
        BASIC = 0, 'Basic',
        MIDDLE = 1, 'Middle',
        ADVANCED = 2, 'Advanced',

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1024, blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='media/covers')
    category = models.ForeignKey('quiz.Category', related_name='quizzes', on_delete=models.CASCADE)
    level = models.PositiveSmallIntegerField(
        choices=LEVEL_CHOICES.choices, default=LEVEL_CHOICES.BASIC
    )

    def questions_count(self):
        return self.questions.count()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Result(BaseModel):
    quiz = models.ForeignKey('quiz.Quiz', related_name='results', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class Question(BaseModel):
    quiz = models.ForeignKey('quiz.Quiz', related_name='questions', on_delete=models.CASCADE)
    order_number = models.PositiveSmallIntegerField(validators=[MaxValueValidator(Quiz.QUESTION_MAX_LIMIT),
                                                                MinValueValidator(Quiz.QUESTION_MIN_LIMIT)])
    text = models.TextField(max_length=1024)


class Choice(BaseModel):
    question = models.ForeignKey('quiz.Question', related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)



