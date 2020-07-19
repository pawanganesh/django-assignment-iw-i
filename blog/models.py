from django.db import models
from django.contrib.auth.models import User

import uuid


def image_path(_, imagename):
    print(imagename)
    extension = imagename.split('.')[-1]
    unique_id = uuid.uuid4().hex
    new_imagename = 'images/'+unique_id+'.'+extension
    return new_imagename


class Author(models.Model):
    name = models.CharField(max_length=180)
    email = models.EmailField()
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to=image_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
