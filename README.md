# Ex01 Django ORM Web Application
## Date: 23/11/2025

## AIM
To develop a Django Application to store and retrieve data from a E-Commerce Website Database for Amazon or Flipkart using Object Relational Mapping(ORM).




## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
models.py

from django.db import models
from django.contrib import admin
class product(models.Model):
    SI_NO=models.IntegerField()
    product_name=models.CharField(max_length=30)
    price=models.IntegerField()
    category=models.CharField(max_length=20)
    discription=models.CharField(max_length=30)
    brand=models.CharField(max_length=10)
    image_url=models.CharField(max_length=15)
    product_id=models.CharField(primary_key=True,max_length=20)
class product_admin(admin.ModelAdmin):list_display=["SI_NO","product_name","price","category","discription","brand","image_url","product_id"]

admin.py

from django.contrib import admin
from.models import product,product_admin
admin.site.register(product,product_admin)

```
## OUTPUT

![alt text](<Screenshot 2025-11-23 170453.png>)

## RESULT
Thus the program for creating E-commerce website database using ORM hass been executed successfully
