from django.db import models

class Post(models.Model):
    name        = models.CharField(max_length = 200)
    author      = models.CharField(max_length = 100)
    description = models.CharField(max_length = 300)
    content     = models.TextField()
    categories  = models.CharField(max_length = 150)
