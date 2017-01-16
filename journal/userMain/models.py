from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class userMainTeble(models.Model):
    fild_one=models.CharField(max_length=200, verbose_name='Текстовое поле')
    pub_date=models.DateTimeField('Дата публикации')
    def __str__(self):
        return self.fild_one
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    class Meta:
        verbose_name="Тестовая запись"
        verbose_name_plural = "Тестовые записи"
