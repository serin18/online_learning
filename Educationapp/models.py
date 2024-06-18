from django.db import models

# Create your models here.

class course_register(models.Model):
    full_name=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    phone=models.IntegerField()
    dob=models.CharField(max_length=25)
    photo=models.FileField()
    address = models.CharField(max_length=50)
    qualification = models.CharField(max_length=25)
    course = models.CharField(max_length=25)
    def __str__(self):
        return self.full_name


class python_book(models.Model):
    full_name=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    phone=models.IntegerField()
    dob=models.CharField(max_length=25)
    photo=models.FileField()
    address = models.CharField(max_length=50)
    qualification = models.CharField(max_length=25)
    payid = models.CharField(max_length=25)
    def __str__(self):
        return self.full_name

class DS_book(models.Model):
    full_name=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    phone=models.IntegerField()
    dob=models.CharField(max_length=25)
    photo=models.FileField()
    address = models.CharField(max_length=50)
    qualification = models.CharField(max_length=25)
    payid = models.CharField(max_length=25)
    def __str__(self):
        return self.full_name

class mernstack_book(models.Model):
    full_name=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    phone=models.IntegerField()
    dob=models.CharField(max_length=25)
    photo=models.FileField()
    address = models.CharField(max_length=50)
    qualification = models.CharField(max_length=25)
    payid = models.CharField(max_length=25)
    def __str__(self):
        return self.full_name

class DM_book(models.Model):
    full_name=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    phone=models.IntegerField()
    dob=models.CharField(max_length=25)
    photo=models.FileField()
    address = models.CharField(max_length=50)
    qualification = models.CharField(max_length=25)
    payid = models.CharField(max_length=25)
    def __str__(self):
        return self.full_name

class flutter_book(models.Model):
    full_name=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    phone=models.IntegerField()
    dob=models.CharField(max_length=25)
    photo=models.FileField()
    address = models.CharField(max_length=50)
    qualification = models.CharField(max_length=25)
    payid = models.CharField(max_length=25)
    def __str__(self):
        return self.full_name

class user_log(models.Model):
    user_name=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    photo = models.FileField()
    dob=models.CharField(max_length=25)
    status=models.CharField(max_length=25,default='pending')
    def __str__(self):
        return self.user_name

class tutor_log(models.Model):
    user_name=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    resume=models.FileField()
    status = models.CharField(max_length=25,default='pending')
    def __str__(self):
        return self.user_name

class trial(models.Model):
    full_name=models.CharField(max_length=25)
    course = models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    phone=models.IntegerField()
    date = models.CharField(max_length=25)
    payid = models.CharField(max_length=25)
    def __str__(self):
        return self.full_name

class class_link(models.Model):
    date=models.CharField(max_length=25)
    time = models.CharField(max_length=25)
    duration=models.CharField(max_length=25)
    subject=models.CharField(max_length=25)
    topic = models.CharField(max_length=25)
    def __str__(self):
        return self.date

class certificate(models.Model):
    email=models.CharField(max_length=25)
    sslc=models.FileField()
    plustwo = models.FileField()
    degree = models.FileField()
    def __str__(self):
        return self.email

class admin_login(models.Model):
    full_name=models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    pasw = models.CharField(max_length=25)
    def __str__(self):
        return self.full_name

class current_login(models.Model):
    email = models.CharField(max_length=25)
    def __str__(self):
        return self.email

class apply_job(models.Model):
    full_name = models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    resume=models.FileField()
    def __str__(self):
        return self.full_name

class interviewsave(models.Model):
    full_name = models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    qualification = models.CharField(max_length=25)
    course = models.CharField(max_length=25)
    def __str__(self):
        return self.full_name