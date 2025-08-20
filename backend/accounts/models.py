from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = "ADMIN", "admin"
        MANAGER = "MANAGER", "manager"
        EMPLOYEE = "EMPLOYEE", "employee"
    
    role = models.CharField(max_length=20, choices=Roles, default=Roles.EMPLOYEE)

    def isAdmin(self):
        return self.role == self.Roles.ADMIN
    
    def isManager(self):
        return self.role == self.Roles.MANAGER
    
    def isEmployee(self):
        return self.role == self.Roles.EMPLOYEE

