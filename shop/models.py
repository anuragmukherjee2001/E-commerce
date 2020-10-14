from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    Product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.Product_name



class Contact(models.Model):
    msg_id = models.AutoField (primary_key = True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=13, default="")
    desc = models.CharField(max_length=5000, default="")
   

    def __str__(self):
        return self.name


class Orders(models.Model):
    order_id = models.AutoField(primary_key = True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=13, default="")
