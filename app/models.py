from django.db import models

# Create your models here.
class jspider(models.Model):
    course_name = models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.course_name
    
    
class student(models.Model):
    course_name = models.ForeignKey(jspider,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mob = models.IntegerField()
    doj = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.name
    
