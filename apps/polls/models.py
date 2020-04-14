import datetime
from django.db import models
from django.utils import timezone


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides selfupdating ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Question(TimeStampedModel):
        question_text = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')
        # owner = models.ForeignKey('auth.User', related_name='questions', on_delete=models.CASCADE)
        def __str__(self):
            return self.question_text
        def was_published_recently(self):
            now = timezone.now()
            return now - datetime.timedelta(days=1) <= self.pub_date <= now

    
class Choice(TimeStampedModel):
    question = models.ForeignKey(Question, related_name='choices',on_delete = models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
