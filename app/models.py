from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class User(models.Model):

    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    dob = models.DateField()
    batch = models.IntegerField()
    department = models.CharField(max_length=30)
    adminPrivilege = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def get_name(self):
        return self.firstName + ' ' + self.lastName

    def __str__(self):
        return self.get_name()


class Login(models.Model):

    userName = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (self.userName + ' - ' + self.user.get_name())


class Poll(models.Model):

    question = models.CharField(max_length=300)
    options = ArrayField(base_field=models.CharField(max_length=50))
    active = models.BooleanField(default=True)
    startDate = models.DateField()
    endDate = models.DateField()
    # 0 - Project Vote, 1 - Admin Vote
    pollType = models.IntegerField()


class Project(models.Model):

    projectName = models.CharField(max_length=100)
    projectDescription = models.CharField(max_length=300)
    repo = models.CharField(max_length=300)
    contributors = models.ManyToManyField('app.User', related_name='projects')
    languages = ArrayField(base_field=models.CharField(max_length=20))
    frameworks = ArrayField(base_field=models.CharField(max_length=20))
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Votes(models.Model):

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.CharField(max_length=50)