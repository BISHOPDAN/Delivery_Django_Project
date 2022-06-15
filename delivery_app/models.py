from cgitb import text
from re import T
from tracemalloc import Trace
from django.db import models
import random


# Create your models here.
def generate_tracking_no(size=12, chars='012345678912'):
       return ''.join(random.choice(chars) for _ in range(size))

       


class Shipment(models.Model):
    name = models.CharField(max_length=100)
    shipping_type = models.CharField(max_length=100)
    container_no = models.IntegerField()
    length = models.IntegerField()
    width = models.IntegerField()
    heig = models.IntegerField()
    weig = models.IntegerField()
    goodsType = models.CharField(max_length=100, blank=True)
    additional_info	= models.CharField(max_length=100, blank=True)
    pickup_timestamp = models.DateTimeField(auto_now=True,null=True)
    arrival_timestamp = models.DateTimeField(auto_now=True,null=True)
    


    def __str__(self) -> str:
        return self.name

class ShippingDocument(models.Model):
    shipping_doc_id	= models.IntegerField()
    reference_no = models.IntegerField()
    doc_url	= models.CharField(max_length=100)
    document_name = models.CharField(max_length=100)
    shipment_id = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.document_name



class ShippingTo(models.Model):
    receiver_name = models.CharField(max_length=100)
    receiver_company = models.CharField(max_length=100)
    receiver_country = models.CharField(max_length=100)
    receiver_address =  models.CharField(max_length=100)
    receiver_address_2 =  models.CharField(max_length=100)
    receiver_address_3 =  models.CharField(max_length=100)
    postal_code = models.BigIntegerField(null = True)
    state =  models.CharField(max_length=100, blank=True)
    city =  models.CharField(max_length=100, blank=True)
    email =  models.CharField(max_length=100)
    phone_number = models.BigIntegerField(null = True)
    country_code = models.BigIntegerField(null = True)
    taxt_no = models.IntegerField(null=True)
    shipment = models.ForeignKey(Shipment, on_delete=models.SET_NULL, null=True)


    

    def __str__(self) -> str:
        return self.receiver_name
    
    

class ShippingFrom(models.Model):
    sender_name = models.CharField(max_length=100)
    sender_company = models.CharField(max_length=100)
    sender_country = models.CharField(max_length=100)
    sender_address =  models.CharField(max_length=100)
    sender_address_2 =  models.CharField(max_length=100)
    sender_address_3 =  models.CharField(max_length=100)
    postal_code = models.BigIntegerField(null= True)
    state =  models.CharField(max_length=100, blank=True)
    city =  models.CharField(max_length=100, blank=True)
    email =  models.CharField(max_length=100)
    phone_number = models.BigIntegerField(null = True)
    country_code = models.BigIntegerField(null= True)
    taxt_no = models.BigIntegerField(null= True)
    vat_no = models.IntegerField(null= True)
    shipment = models.ForeignKey(Shipment, on_delete=models.SET_NULL, null=True)


    def __str__(self) -> str:
        return self.sender_name





class Tracking(models.Model):
    tracking_no = models.CharField(max_length=12, default=generate_tracking_no(),unique=True)
    tracking_description = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True, blank=True)
    timestamps = models.DateTimeField(auto_now=True)
    quantity = models.CharField(max_length=100)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, null=True, related_name="shipment_key")
    shipping_to = models.ForeignKey(ShippingTo, on_delete=models.CASCADE, null=True, related_name="shippingto_key")
    shipping_from = models.ForeignKey(ShippingFrom, on_delete=models.CASCADE, null=True, related_name="shippingfrom_key")
    delivered = models.BooleanField(default=False)
    status = models.CharField(max_length=100, null=True)
    estdeliveryDate = models.CharField(max_length=100, null=True)


    def __str__(self) -> str:
        return self.tracking_description


    



    
    
class Country(models.Model):
    sortname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phoneCode = models.IntegerField()
    


    def __str__(self) -> str:
        return self.sortname



class State(models.Model):
    country = models.ForeignKey(Country, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    


    def __str__(self) -> str:
        return self.name


class City(models.Model):
    state = models.ForeignKey(State, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    


    def __str__(self) -> str:
        return self.name











        
    


    

        
    

