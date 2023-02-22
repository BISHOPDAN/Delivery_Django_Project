from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


from delivery_app.models import (Shipment,
                                ShippingTo,
                                ShippingDocument,
                                ShippingFrom,
                                Tracking,
                                Country,
                                State,
                                City)
                                
                                
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user


class ShipmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Shipment
        fields = ['id','name', 
                'shipping_type', 'container_no',
                'length', 'width', 'heig', 'weig', 
                'goodsType', 'additional_info']

        


class ShippingToSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingTo
        fields= ['id',
            "receiver_name",
            "receiver_company",
            "receiver_country",
            "receiver_address",
            "receiver_address_2",
            "receiver_address_3",
            "postal_code",
            "state",
            "city",
            "email",
            "phone_number",
            "country_code",
            "taxt_no",
            "shipment"]


class ShippingDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingDocument
        fields= '__all__'


class ShippingFromSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ShippingFrom
        fields= ['id',
                'sender_name',
                'sender_company', 
                'sender_country',
                'shipment',
                'sender_address',
                'sender_address_2',
                'sender_address_3',
                'postal_code',
                'state',
                'city',
                'email',
                'phone_number',
                'country_code',
                'taxt_no',
                'vat_no']


class TrackingSerializer(serializers.ModelSerializer):
    shipments = serializers.SerializerMethodField()                        #(source="shipment_key.name")
    shippingtos = serializers.SerializerMethodField()
    shippingfroms = serializers.SerializerMethodField()
    
    class Meta:
        model = Tracking
        fields= ('id',
                'tracking_no', 
                'tracking_description', 
                'location', 'timestamps', 
                'quantity','delivered',
                'status', 'estdeliveryDate', 
                'shipment', 'shippingtos',
                'shipping_to', 'shipments',
                'shipping_from', 'shippingfroms')
                
                
       
        read_only_fields = ('tracking_no',)


    def get_shipments(self, obj):
        try:

            shipment = Shipment.objects.get(shipment_key__tracking_no=obj.tracking_no) 
            print(shipment)
            shipment_data = ShipmentSerializer(shipment, context=self.context, many=False).data
            return shipment_data
        except Shipment.DoesNotExist:
            return None
       


    def get_shippingtos(self, obj):
        try:
            shippingto =  ShippingTo.objects.get(shippingto_key__tracking_no=obj.tracking_no) 
            shippingto_data = ShippingToSerializer(shippingto, context=self.context, many=False).data
            return shippingto_data
        except ShippingTo.DoesNotExist:
            return None



    def get_shippingfroms(self, obj):
        try:
            shippingfrom =  ShippingFrom.objects.get(shippingfrom_key__tracking_no=obj.tracking_no) 
            shippingfrom_data = ShippingFromSerializer(shippingfrom, context=self.context, many=False).data
            return shippingfrom_data
        except ShippingFrom.DoesNotExist:
            return None

            
    
      

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields= '__all__'


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields= "__all__"


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields= ['id', 'name', 'state_id']





















# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user