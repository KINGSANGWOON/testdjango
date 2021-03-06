from django.db import models


class Question(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField()