from django.db import models
#from preprocesor.database import Database
#from config import configfile as database

class Query(models.Model):
    #Database.__init__(self,database.Services)
    urls = models.CharField(max_length=300)
    public_id = models.CharField(max_length=10)
    def risk_measure(self):
        pass



class Analize(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    asoc_clients = models.CharField(max_length=300)
# Create your models here.
