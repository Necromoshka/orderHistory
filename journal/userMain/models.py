from django.db import models

# Create your models here.

class userMainTeble(models.Model):
    fild_one=models.CharField(max_length=200)
    pub_date=models.DateTimeField('Дата публикации')
