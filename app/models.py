#--------------------------------------Start-------------------------------------
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
STATE_CHOICES = (
    ("Dhaka", "Dhaka"),
    ("Khulna", "Khulna"),
    ("Barishal", "Barishal"),
    ("Chattogram", "Chattogram"),
    ("Rajshahi", "Rajshahi"),
    ("Rangpur", "Rangpur"),
    ("Sylhet", "Sylhet"),
    ("Mymensingh", "Mymensingh"),
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)
def __str__(self):
    return self(self.id)
CATEGORY_CHOICES = (
    ("M", "Services Hacking"),
    ("L", "Services Devlopment"),
    ("TW", "Viruse's"),
    ("BW", "Free Softwars"),
)
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to="productimg")
def __str__(self):
    return self(self.id)
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
def __str__(self):
    return self(self.id)
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
STATUS_CHOICES = (
    ("Accepted", "Accepted"),
    ("Packed", "Packed"),
    ("On The Way", "On The Way"),
    ("Cancel", "Cancel"),
)
class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
#-------------------------------------------End--------------------------------------------