from django.db import models
from django.core import validators
from fruitipediaApp.fruits.validators import validate_name

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255, unique=True)

class Fruit(models.Model):
    name=models.CharField(max_length=30,
                          validators=[validators.MinLengthValidator(2),
                                      validate_name])

    Image_url=models.URLField()
    description=models.TextField()
    nutrition=models.TextField(null=True, blank=True)