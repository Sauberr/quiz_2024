from django.contrib import admin

from quiz.models import Category, Choice, Question, Quiz, Result

admin.site.register([Quiz, Question, Category, Result, Choice])
