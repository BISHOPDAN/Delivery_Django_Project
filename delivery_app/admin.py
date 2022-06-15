from django.contrib import admin
from .models import Shipment, ShippingTo, ShippingFrom, ShippingDocument, Tracking, Country, State, City





admin.site.register(Shipment)
admin.site.register(ShippingTo)
admin.site.register(ShippingFrom)
admin.site.register(ShippingDocument)
admin.site.register(Tracking)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)



