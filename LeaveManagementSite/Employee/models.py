from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from decimal import Decimal
    

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  

    def __str__(self):
        return self.title



class Application(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    reason = models.CharField(max_length=20, default='Pending')
    skills = models.TextField()
    status = models.CharField(max_length=20, default='Pending')  
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=1)  
    
    def __str__(self):
        return f'{self.name} - {self.status}'


class Payroll(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    total_pay = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    month = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        self.salary = Decimal(self.salary) if not isinstance(self.salary, Decimal) else self.salary
        self.deductions = Decimal(self.deductions) if not isinstance(self.deductions, Decimal) else self.deductions
        
        self.total_pay = self.salary - self.deductions
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee.username} - {self.month}"