from django.db import models

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=5)
    firstname = models.TextField()
    lastname = models.TextField()
    age = models.IntegerField()

class Service(models.Model):
    name = models.TextField(primary_key=True)
    website = models.URLField()
    ppm = models.FloatField() # price per month
    users = models.ManyToManyField(User, through='Subscription')

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True) # поле может быть пустым, если подписка еще действует
    active = models.BooleanField()

