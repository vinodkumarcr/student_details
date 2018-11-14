from django.db import models

class details(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=20)

    def __str__(self):
        return self.name
