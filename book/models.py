from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
from django.db import models

# Create your models here.
# class Rating(models.Model):
#     rating = models.IntegerField()
#     userID = models.CharField(max_length=50)
#     usrrnme = models.CharField(max_length=50,null = True)
#     bookID = models.CharField(max_length=50)
#     comment = models.TextField()

class Rates(models.Model):
    rates = models.IntegerField()
    userID = models.CharField(max_length=50)
    bookID = models.CharField(max_length=50)
    usrrnme = models.CharField(max_length=50,null = True)
    comment = models.TextField()
# class Rate(models.Model):
#     rating = models.IntegerField()
#     userID = models.CharField(max_length=50)
#     bookID = models.CharField(max_length=50)
#     comment = models.TextField()



class Book(models.Model):
    Title = models.CharField(max_length = 120,null = False)
    Author = models.CharField(max_length = 120)
    Publisher = models.CharField(max_length = 120)
    Genre = models.CharField(max_length = 120)
    ISBN = models.CharField(max_length = 13,null = False) #as int was small, take as char
    Location = models.TextField()
    Available = models.BooleanField(default=True)
    Lost = models.BooleanField(default=False)
    Comments = models.TextField(null=True)
    SoftCopy = models.URLField(blank = True, max_length=200)

class Issue(models.Model):
    Book_state = [
        ('Requested', 'Requested'),
        ('Issued', 'Issued'),
        ('Returned', 'Returned'),
        ('Request Extension', 'Request Extension'),
        ('Extended Issue', 'Extended Issue'),
        ('Issued/Ext Denied', 'Issued/Ext Denied'),
        ('Rejected Issue', 'Rejected Issue'),
        ('NA', 'NA')
    ]
    Title = models.CharField(max_length = 120,null = False)
    BookID = models.IntegerField(null = False)
    User = models.CharField(max_length=50)
    DoI=models.DateField(auto_now_add=False)
    DoD=models.DateField(auto_now_add=False)
    State = models.CharField(
        max_length=50,
        choices = Book_state,
        default = 'Requested',
    )
    Comments = models.TextField(null=True)