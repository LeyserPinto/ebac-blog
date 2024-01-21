from django.db import models

STATUS = ((0, "Draft"), (1, "Publish"))

class Post(models.Model):
    title       = models.CharField(max_length = 200, null= True)
    slug        = models.SlugField(max_length = 200, null= True)
    author      = models.CharField(max_length = 100)
    description = models.CharField(max_length = 300)
    content     = models.TextField()
    categories  = models.CharField(max_length = 150)
    status      = models.IntegerField(choices=STATUS, default=0)
    created_on  = models.DateTimeField(auto_now_add=True)
    updated_on  = models.DateTimeField(auto_now=True)