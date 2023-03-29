from django.db import models

# Create your models here.

DESIGNATION_CHOICES = (
("Front-end-developer", "Front-end-developer"),
("Back-end-developer", "Back-end-developer"),
("Team-Leader","Team-Leader"),
("Manager", "Manager"),
("Quality-Analyst", "Quality-Analyst"),
)

class Employee(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True, max_length=255, unique=True)
    address = models.CharField(blank = True, max_length=400)
    photo = models.ImageField(blank=True, upload_to='media/')
    designation = models.CharField(max_length=255, blank=True, default='Front-end-developer', choices= DESIGNATION_CHOICES)