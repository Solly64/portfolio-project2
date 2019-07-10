from django.db import models
from django_pandas.managers import DataFrameManager

# Create your models here.
class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    #first_name =
    #last_name =
    #email =

    def __str__(self):
        return self.item + '|' + str(self.completed)
