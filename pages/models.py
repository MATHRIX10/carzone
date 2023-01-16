from django.db import models

# Create your models here.




class Team(models.Model) :

    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    facebook = models.URLField(max_length=255)
    twitter = models.URLField(max_length=255)
    googleplus = models.URLField(max_length=255)
    createdate = models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return f'{self.firstname}-{self.lastname}'