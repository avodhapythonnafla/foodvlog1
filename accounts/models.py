from django.db import models

# Create your models here.

class regs(models.Model):
    user_name=models.CharField(max_length=150)
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    email=models.CharField(max_length=250)
    password=models.CharField(max_length=150)
    last_login = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.user_name

