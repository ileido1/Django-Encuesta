
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import QuestionViewSet,ChoiceViewSet
from rest_framework import permissions

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'questions', views.QuestionViewSet)
router.register(r'choices', views.ChoiceViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'results', views.ResultsViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
]