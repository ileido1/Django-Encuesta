from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import RequestsClient
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from .models import Question,Choice
from .serializer import QuestionSerializer
from django.contrib.auth.models import User


# Include an appropriate `Authorization:` header on all requests.
        

class QuestionModelTests(APITestCase):
    
    # aqui debo crear el setup de la instancia question pero no estoy muy claro como hacerlo todavia para no repetir codigo
    
    def test_api_create(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test', password='test123')
        self.user.save()
        user = User.objects.get(username='test')
        self.client.force_authenticate(user=user)
        url = reverse('question-list')
        pub = {'pub_date': '2020-04-11T20:11:05-04:00', 'question_text': 'prueba'}
        response = self.client.post(url, pub , format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_api_list(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test', password='test123')
        self.user.save()
        user = User.objects.get(username='test')
        self.client.force_authenticate(user=user)
        url = reverse('question-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_api_update(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test', password='test123')
        self.user.save()
        user = User.objects.get(username='test')
        self.client.force_authenticate(user=user)
        url = reverse('question-list')
        pub = {'pub_date': '2020-04-11T20:11:05-04:00', 'question_text': 'prueba'}
        response = self.client.post(url, pub , format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = {'pub_date': '2020-04-11T20:11:05-04:00', 'question_text': 'bienvenido'}
        url = reverse('question-detail',kwargs={"pk": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data["question_text"],"prueba")
        response = self.client.put(url,data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_api_delete(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test', password='test123')
        self.user.save()
        user = User.objects.get(username='test')
        self.client.force_authenticate(user=user)
        url = reverse('question-list')
        pub = {'pub_date': '2020-04-11T20:11:05-04:00', 'question_text': 'prueba'}
        response = self.client.post(url, pub , format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        url = reverse('question-detail',kwargs={"pk": 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_api_vote(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test', password='test123')
        self.user.save()
        user = User.objects.get(username='test')
        self.client.force_authenticate(user=user)
        url = reverse('question-list')
        pub = {'pub_date': '2020-04-11T20:11:05-04:00', 'question_text': 'prueba'}
        response = self.client.post(url, pub , format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        url = reverse('choice-list')
        data= {"choice_text": "prueba","votes": 0,"question": 1}
        response = self.client.post(url, data , format='json')

        url = reverse('choice-vote',kwargs={"pk": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data["status"],"choice set")  

    
        