import datetime

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from sql.models import Admin

class Employee(models.Model):
    Emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(
        max_length=150,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        
        verbose_name='emp_name'
    )
    job_position = models.CharField(
        max_length=150,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        
        verbose_name='job_post'
    )
    email = models.CharField(max_length=254, verbose_name='email address', blank=True)
    gender = models.CharField(verbose_name='Gender',max_length=10)
    age = models.IntegerField(default=0)
    contact_no = models.IntegerField(default=0)

    

class Duration(models.Model):
    time_id = models.AutoField(primary_key=True)
    emp_id = models.ForeignKey(Employee, on_delete=CASCADE)
    # status = models.BooleanField(default=True, help_text='Designates whether this user is on leave or work', verbose_name='active')
    entry_time = models.DateTimeField(default=timezone.now, verbose_name='Entry_TIME')
    exit_time = models.DateTimeField(default=timezone.now, verbose_name='Exit_TIME')
    duration = models.DateTimeField(default=timezone.now, verbose_name='Durationj')
   
class Leave(models.Model):
    leave_id = models.AutoField(primary_key=True)
    emp_id = models.ForeignKey(Employee, on_delete=CASCADE)
    # contact_no = models.ForeignKey(Employee, on_delete=CASCADE)
    date = models.DateTimeField(default=timezone.now, verbose_name='DATE')
    # email = models.ForeignKey(Employee, on_delete=CASCADE)



class Admin(models.Model):
    ad_emp_id = models.AutoField(primary_key=True)
    admin_username = models.CharField(
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[UnicodeUsernameValidator()],
        verbose_name='Admn_username'
    )

