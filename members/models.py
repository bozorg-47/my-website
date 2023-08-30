from django.db import models

class Question_f(models.Model):
  question = models.CharField(max_length=255,null=True)
  correct_answer = models.CharField(max_length=255,null=True)
  answer1 = models.CharField(max_length=255,null=True)
  answer2 = models.CharField(max_length=255,null=True)
  answer3 = models.CharField(max_length=255,null=True)
  answer4 = models.CharField(max_length=255,null=True)

class Question_g(models.Model):
  question = models.CharField(max_length=255,null=True)
  correct_answer = models.CharField(max_length=255,null=True)
  answer1 = models.CharField(max_length=255,null=True)
  answer2 = models.CharField(max_length=255,null=True)
  answer3 = models.CharField(max_length=255,null=True)
  answer4 = models.CharField(max_length=255,null=True)

