from django.db import models

# Create your models here.
class Department(models.Model):
    Department = models.TextField(max_length=512,null=False,blank=False)
    Course = models.TextField(max_length=1000,null=False,blank=False)

    def set(self,dept,course):
        self.Department = dept
        self.Course = course
