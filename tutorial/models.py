from django.db import models

# Create your models here.
class employee(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    department = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'

    
    def __str__(self):
        return self.firstname