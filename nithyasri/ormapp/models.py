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

