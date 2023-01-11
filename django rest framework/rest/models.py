from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.FloatField()

    def __str__(self):
        return f"{self.id} || {self.name}"

class Person(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    add = models.TextField()

    def __str__(self):
        return self.name


CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class Singer(models.Model):
    singer_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=200,choices=CHOICES)

    def __str__(self) -> str:
        return self.singer_name

class Song(models.Model):
    song_name = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='extra')
    durantion = models.IntegerField()

    def __str__(self) -> str:
        return self.song_name

'''
to access singer from song object then we can access like this ->
 song_obj.singer.singer_name/gender 
but to access song from singer object then we can use this -> related_name='extra'
 singer_obj.extra.song_name/duration 

'''

class Code(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Anime(models.Model):
    name = models.CharField(max_length=100)
    ratings = models.IntegerField()
    desc = models.TextField(max_length=200)

    def __str__(self) -> str:
        return self.name
    


