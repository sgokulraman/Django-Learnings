from django.db import models

class Student_details(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length = 200)
    roll_no = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.IntegerField()
    class_name = models.IntegerField()
    section = models.CharField(max_length=20)
    dateofbirth = models.CharField(max_length=40)
    time = models.TimeField(auto_now=True)
    def __str__(self):
        return f"First name - {self.first_name},/n Last name - {self.last_name}/n Roll Number - {self.roll_no} /n class - {self.class_name} Mobile {self.phone_no} "
    