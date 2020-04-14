from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Question,Choice
from .serializer import QuestionSerializer,ChoiceSerializer,UserSerializer,ResultsSerializer
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


from django.contrib.auth.models import User


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.order_by('-pub_date')[:5]
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

class ResultsViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = ResultsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def vote(self, request, pk=None):
        choice = self.get_object()
        choice.votes += 1
        choice.save()
        return Response({'status': 'choice set'})
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]
	
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
