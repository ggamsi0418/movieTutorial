from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=30)  # 영화 제목
    genre = models.CharField(max_length=15)  # 장르
    year = models.IntegerField()  # 제작 년도

    def __str__(self):
        return self.title  # admin 페이지에서 'title'이라고 명시된다.
