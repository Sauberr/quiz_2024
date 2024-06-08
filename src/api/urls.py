from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from api.views import (CategoryCreateView, CategoryDeleteView,
                       CategoryListView, CategoryUpdateView, CustomerViewSet,
                       QuestionDetailView, QuizListView)

app_name = "api"

router = routers.DefaultRouter()
router.register("customer", CustomerViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Quiz API",
        default_version="v1",
        description="Quiz API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@admin.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[
        permissions.AllowAny,
    ],
)

urlpatterns = [
    path("", include(router.urls)),
    path("quiz/<int:pk>/question/<int:order>/", QuestionDetailView.as_view(), name="question_details"),
    path("qiuz/", QuizListView.as_view(), name="quiz_list"),
    path("auth/", include("djoser.urls.jwt")),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger_docs"),
    path("category/create/", CategoryCreateView.as_view(), name="category_create"),
    path("category/delete/", CategoryDeleteView.as_view(), name="category_delete"),
    path("category/update/", CategoryUpdateView.as_view(), name="category_update"),
    path("category/list/", CategoryListView.as_view(), name="category_list"),
]
