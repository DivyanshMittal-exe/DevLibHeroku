from django.db import models
from datetime import datetime, timedelta
import datetime
from django.utils import timezone


# Create your models here.
class Issue(models.Model):
    Book_state = [
        ('Requested', 'Requested'),
        ('Issued', 'Issued'),
        ('Returned', 'Returned'),
        ('NA', 'NA')
    ]
    
    
    
    Title = models.CharField(max_length = 120,null = False)
    BookID = models.IntegerField(null = False)
    User = models.CharField(max_length=50)
    DoI=models.DateField(auto_now_add=True)
    DoD=models.DurationField(default = datetime.timedelta(days=7))
    state = models.CharField(choices = Book_state,default = 'Requested',max_length=9)
    Comments = models.TextField(null=True)