# Models for OctoFit Tracker using Djongo (MongoDB)
from djongo import models

class User(models.Model):
    _id = models.ObjectIdField()
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    # Add more fields as needed
    class Meta:
        db_table = 'users'

class Team(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    members = models.ArrayField(model_container=User)
    class Meta:
        db_table = 'teams'

class Activity(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateTimeField()
    class Meta:
        db_table = 'activity'

class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'

class Workout(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout_type = models.CharField(max_length=50)
    details = models.JSONField()
    date = models.DateTimeField()
    class Meta:
        db_table = 'workouts'
