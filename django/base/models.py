from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    std = models.IntegerField()

    def __str__(self) -> str:
        return self.name

class Test(models.Model):
    subject = models.CharField(max_length=50)
    marks = models.IntegerField()

    def __str__(self) -> str:
        return self.subject

class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=14)
    bio = models.TextField(max_length=200)
    avatar = models.ImageField(null=True, blank=True) 
    # we can add this field for default picture -> default='static/images/image_name.png'

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

CHOICE = (
    ('Mumbai', 'Mumbai'),
    ('Pune', 'Pune'),
    ('Banglaore', 'Banglaore'),
    ('Hyderabad', 'Hyderabad'),
    ('Chennai', 'Chennai'),
    ('Mysore', 'Mysore'),
)


class StudentData(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    std = models.IntegerField()
    city = models.CharField(max_length=50, choices=CHOICE)
    marks = models.IntegerField()
    passout = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Post(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=300)
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

