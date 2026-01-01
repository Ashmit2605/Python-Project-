from django.db import models

# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=100) #Name
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
