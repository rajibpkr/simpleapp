from types import BuiltinMethodType
from django.db import models

# Create your models here.
class Article(models.Model): #model is represented by a class in djiango
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #add in thumbnail later
    #add in author later

    def __str__(self):
        return self.title #this will print article string title. otherwise it will not print name.
                          #Instead it will print like, Article object(1), Article object(2), and so on..
                    

    def snippet(self):
        return self.body[:50] + "..."
