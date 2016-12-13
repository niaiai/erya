from django.db import models


class jokeji(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    stype = models.IntegerField(default=1, max_length=1)

    def __str__(self):
        return self.question