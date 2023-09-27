from django.db import models

# Create your models here.
class Employee(models.Model):
    empid=models.IntegerField()
    empname=models.CharField(max_length=30)
    empsalary=models.IntegerField()
    empaddress=models.CharField(max_length=30)
    def __str__(self):
        return +str(self.id)+str(self.empid)+","+self.empname+","+str(self.empsalary)+","+self.empaddress