from rest_framework import viewsets
from .models import Question,Choice
from .serializer import QuestionSerializer,ChoiceSerializer

class QuestionViewSet(viewsets.ModelViewSet):
	queryset = Question.objects.order_by('-pub_date')[:5]
	serializer_class = QuestionSerializer
class ChoiceViewSet(viewsets.ModelViewSet):
	queryset = Choice.objects.all()
	serializer_class = ChoiceSerializer