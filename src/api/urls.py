from django.urls import include
from rest_framework import routers
from django.urls import path

from api.views import CustomerViewSet, QuestionDetailView, QuizListView

app_name = 'api'

router = routers.DefaultRouter()
router.register('customer', CustomerViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('quiz/<int:pk>/question/<int:order>/', QuestionDetailView.as_view(),
         name='question_details'),
    path('qiuz/', QuizListView.as_view(), name='quiz_list'),
]