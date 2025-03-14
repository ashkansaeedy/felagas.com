from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    # def was_published_recenly(self):
    #     return self.pub_date >= timezone.now() -datetime.timedelta(days=1)

# class Answer(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     answer_text = models.IntegerField(default=0)
#     pub_date = models.DateTimeField('date published')

#     def __str__(self):
#         return self.answer_text
