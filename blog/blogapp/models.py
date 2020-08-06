from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=200,blank=False)
    content = models.TextField(blank=False)
    imageurl = models.TextField(blank=False)
    pub_date = models.DateTimeField('date published', default=datetime.now, blank=True)
