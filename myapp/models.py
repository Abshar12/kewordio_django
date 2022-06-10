from django.db import models

class library (models.Model):
    book = models.CharField (max_length=30)
    author = models.CharField (max_length=30)
    quantity = models.IntegerField (max_length=50)
   

    def __str__(self):
        return self.book 
   
   
