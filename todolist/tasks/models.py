import datetime
from django.utils import timezone
from django.db import models


# Create your models here.
class User(models.Model):
    UType_choices = [("admin", "admin"), ("user", "user")]
    UserID = models.IntegerField(primary_key=True)
    UEmail = models.EmailField(unique=True, null=False)
    UName = models.CharField(max_length=150)
    UPassword = models.CharField(max_length=150)
    UType = models.CharField(choices=UType_choices, max_length=150, null=False)

    def __str__(self):
        return self.UName


class List(models.Model):
    ListID = models.IntegerField(primary_key=True)
    LName = models.CharField(max_length=150)

    def __str__(self):
        return self.LName


class Task(models.Model):
    Repeat_choices = [
        ("Daily", "Daily"),
        ("Weekdays", "Weekdays"),
        ("Weekly", "Weekly"),
        ("Monthly", "Monthly"),
        ("Yearly", "Yearly"),
    ]
    Category_choices = [
        ("Blue", "Blue"),
        ("Green", "Green"),
        ("Orange", "Orange"),
        ("Purple", "Purple"),
        ("Red", "Red"),
        ("Yellow", "Yellow"),
    ]
    Priority_choices = [("High", "High"), ("Low", "Low")]

    TaskID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    TName = models.CharField(max_length=150)
    created_at = models.DateField(default=datetime.date.today())
    due_at = models.DateField(null=True)
    Repeat = models.CharField(choices=Repeat_choices, max_length=20, null=True)
    Priority = models.CharField(choices=Priority_choices, max_length=20, default="Low")
    Status = models.BooleanField(default=False)
    ListID = models.ForeignKey(List, on_delete=models.CASCADE)
    Category = models.CharField(choices=Category_choices, max_length=20, null=True)
    Description = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.TName
