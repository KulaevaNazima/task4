from django.db import models
from django.contrib.postgres.fields import ArrayField

class Course(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    category=models.ForeignKey('Category', on_delete=models.CASCADE)
    logo=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=255)

    imgpath=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Branch(models.Model):
    latitude=models.CharField(max_length=255)
    longitude=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    course=models.ForeignKey('Course', on_delete=models.CASCADE, related_name='branches')

    def __str__(self):
        return self.address

class Contact(models.Model):
    CHOICES=(
        ('1', 'Phone'),
        ('2', 'Facebook'),
        ('3', 'Email')
    )

    type=models.CharField(max_length=255, choices=CHOICES)
    value=models.CharField(max_length=255)
    course=models.ForeignKey('Course', on_delete=models.CASCADE, related_name='contacts')

    def __str__(self):
        return self.value
