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
		fields = ['question','choice_text','votes']

class ResultsSerializer(serializers.ModelSerializer):
    # choices = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='choice_text'
    #  )
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['question_text','choices']

class UserSerializer(serializers.ModelSerializer):
    # question = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username']