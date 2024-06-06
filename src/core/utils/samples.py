from quiz.models import Category, Question, Quiz


def sample_quiz(title: str, **params) -> Quiz:
    default = {"description": "Test your knowledge", "category": Category.objects.create()}
    default.update(params)
    return Quiz.objects.create(title=title, **default)


def sample_question(quiz: Quiz, order_number: int, **params) -> Question:
    default = {
        "text": "What is the capital of France?",
    }
    default.update(params)
    return Question.objects.create(quiz=quiz, order_number=order_number, **default)
