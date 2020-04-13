from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import RequestsClient
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from .models import Question
from .serializer import QuestionSerializer
from django.contrib.auth.models import User


# Include an appropriate `Authorization:` header on all requests.
        

class QuestionModelTests(APITestCase):
    
    def test_api_create(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test', password='test123')
        self.user.save()
        user = User.objects.get(username='test')
        self.client.force_authenticate(user=user)
        url = reverse('question-list')
        data =  {
        "created": "2020-04-02T19:51:15.127190-04:00",
        "modified": "2020-04-02T19:51:15.139109-04:00",
        "question_text": "qweqwe",
        "pub_date": "2020-04-01T22:26:17-04:00"
    }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Question.objects.count(), 1)

