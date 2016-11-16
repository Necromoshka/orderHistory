from django.db import models

# Create your models here.

class userMainTeble(models.Model):
    fild_one=models.CharField(max_length=200, verbose_name='Текстовое поле')
    pub_date=models.DateTimeField('Дата публикации')
    class Meta:
        verbose_name="Тестовая запись"
        verbose_name_plural = "Тестовые записи"
