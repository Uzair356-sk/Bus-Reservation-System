# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bus(models.Model):
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    rem = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.bus_name


# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     email = models.EmailField()
#     name = models.CharField(max_length=30)
#     password = models.CharField(max_length=30)

#     def __str__(self):
#         return self.email
import uuid

class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'
    PENDING ="P"

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),
                       (PENDING,"Pending"))
    email = models.EmailField()
    book_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=30)
    userid =models.DecimalField(decimal_places=0, max_digits=2)
    busid=models.DecimalField(decimal_places=0, max_digits=2)
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
    cost = models.DecimalField(max_digits=12,decimal_places=2)
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)

    def __str__(self):
        return self.email



STATUS_CHOICE=[
        ('PENDING','PENDING'),
        ('COMPLETED','COMPLETED'),
        ('FAILED','FAILED')
]
METHOD_CHOICE = [
        ('RAZORPAY','RAZORPAY'),
        ('COD','COD'),
        ('ShopEase_WALLET','ShopEase_WALLET')
]
class Payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    razorpay_order_id = models.CharField(max_length=25,blank=True,default="default")
    razorpay_payment_id = models.CharField(max_length=25,blank=True,default="default")
    payment_signature=models.CharField(max_length=128,default='default',blank=True)
    amount=models.DecimalField(decimal_places=2,max_digits=12)
    status=models.CharField(choices=STATUS_CHOICE,max_length=25)
    method=models.CharField(choices=METHOD_CHOICE,max_length=25)
    book=models.ForeignKey(Book,on_delete=models.DO_NOTHING)