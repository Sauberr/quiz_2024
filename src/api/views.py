from django.contrib.auth import get_user_model
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from api.serializers import (CategorySerializer, CustomerSerializer,
                             QuestionSerializer, QuizSerializer)
from core.permission import IsSuperUser
from quiz.models import Category, Question, Quiz


class CustomerViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CustomerSerializer


class QuestionDetailView(RetrieveAPIView):
    serializer_class = QuestionSerializer

    def get_object(self):
        return Question.objects.get(quiz__pk=self.kwargs.get("pk"), order_number=self.kwargs.get("order"))


class QuizListView(ListAPIView):
    permission_classes = [AllowAny | IsSuperUser]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSuperUser]


class CategoryDeleteView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSuperUser]


class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSuperUser]


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny | IsSuperUser]
