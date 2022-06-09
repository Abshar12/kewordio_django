from django.db import models

class library (models.Model):
    book = models.CharField (max_length=30)
    author = models.CharField (max_length=30)

    def __str__ (self):
        return self.book
        return self.author