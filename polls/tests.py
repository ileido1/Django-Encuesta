from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Question
from .serializer import QuestionSerializer

class QuestionModelTests(APITestCase):

    def test_prueba(self):
        url = reverse('question-list')
        data = {"question_text": "sc",
        "pub_date": "2020-03-26T12:03:00-04:00",
        "owner": 3}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(Question.objects.count(), 1)
        # self.assertEqual(Question.objects.get().question_text, 'sc')