from django.db import models
import datetime

class Author(models.Model):
    name = models.CharField(max_length=100)   
    email = models.EmailField()

    def __str__(self):
        return self.name

class Magazine(models.Model):
    title = models.CharField(max_length=200)
   

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=200)
    categories =models.CharField(max_length=200,default='')
    content = models.TextField()
    publication_date = models.DateField(default=datetime.date.today)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    magazines = models.ManyToManyField(Magazine,default='')

    def __str__(self):
        return self.title
