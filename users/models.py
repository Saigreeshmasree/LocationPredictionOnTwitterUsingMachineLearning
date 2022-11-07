from django.db import models

# Create your models here.
class UserRegistrationModel(models.Model):
    name = models.CharField(max_length=100)
    loginid = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(unique=True, max_length=100)
    email = models.CharField(unique=True, max_length=100)
    locality = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.loginid

    class Meta:
        db_table = 'UserRegistrations'

class UserSearchTweetsLocationModel(models.Model):
    tweetid = models.IntegerField()
    username = models.CharField(max_length=250)
    userscreenname = models.CharField(max_length=250)
    tweettext = models.CharField(max_length=1500)
    createdat = models.DateTimeField()
    address = models.CharField(max_length=250,null=True)
    latitude = models.FloatField()
    longitude=models.FloatField()
    userloc = models.IntegerField()
    def __str__(self):
        return self.tweetid
    class Meta:
        db_table = "TweetsTable"

class UserAlgorithmResultsModel(models.Model):
    username = models.CharField(max_length=100)
    algorithmname = models.CharField(max_length=100)
    accuracy = models.FloatField()
    mae = models.FloatField()
    mse = models.FloatField()
    rmse = models.FloatField()
    r_squared = models.FloatField()
    cdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.id
    class Meta:
        db_table = "AlgorithmResults"
