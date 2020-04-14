from rest_framework import serializers
from .models import Question,Choice
from django.contrib.auth.models import User



class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = '__all__'
class ChoiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Choice
		fields = '__all__'

class ResultsSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['question_text','pub_date','choices']

class UserSerializer(serializers.ModelSerializer):
    # question = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username']