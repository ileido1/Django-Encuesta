from rest_framework import viewsets
from .models import Question,Choice
from .serializer import QuestionSerializer

class QuestionViewSet(viewsets.ModelViewSet):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer