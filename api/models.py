from django.db import models

class Student_details(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    roll_no = models.IntegerField()
    email = models.EmailField()
    phone_no = models.CharField(max_length=30)
    class_name = models.IntegerField()
    section = models.CharField(max_length=20)
    dateofbirth = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    password = models.CharField(max_length=300)
    def __str__(self):
        return(f"First Name - {self.first_name}, Last_name - {self.last_name}, Email - {self.email}")
class Student_problems(models.Model):
    student = models.ForeignKey(Student_details, on_delete=models.CASCADE)
    problem_title = models.CharField(max_length=200)
    problem = models.TextField()
    
    
class Leader_login(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    dateofbirth = models.CharField(max_length=30)
    def __str__(self):
        return self.username
    