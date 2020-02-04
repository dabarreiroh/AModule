from django.db import models
#from Analizer_module.procesor.database import Database
#from config import configfile as database

class Query(models.Model):
    urls = models.TextField()





class Patterns(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    asoc_clients = models.CharField(max_length=300)

# Create your models here.
