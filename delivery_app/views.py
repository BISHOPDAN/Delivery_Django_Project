from urllib import response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
import random
from rest_framework import generics, permissions
#from rest_framework import viewsets+
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .models import Shipment, ShippingTo, ShippingFrom,Tracking, Country, State, City
from .serializers import ShipmentSerializer, ShippingToSerializer,ShippingFromSerializer, CountrySerializer, StateSerializer, CitySerializer, UserSerializer, TrackingSerializer
                                    


#from rest_framework.authentication import TokenAuthentication

# Create your views here.
#class UserViewSet(viewsets.ModelViewSet):
    #queryset = User.objects.all()
    #serializer_class=UserSerializer
"""
class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    #permission_classes = (AllowAny,)
    serializer_class = UserSerializer


    def get(self,request,*args,**kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

#Class based view to register user
"""


class ShipmentViews(APIView):
    def post(self, request, *args, **kwargs):
        
        serializer = ShipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = serializer.data
            response['shipment_id'] = serializer.data.get('id')
            print(response)
            

            return Response({"status": "true", "shipment": response}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "shipment": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    #permission_classes = [IsAuthenticated]
    def get(self, request, id=None):
        if id:
            item = Shipment.objects.get(id=id)
            serializer = ShipmentSerializer(item)
            response = serializer.data
            response['shipment_id'] = serializer.data.get('id')
            print(response)
            return Response({"status": "true", "shipment": response}, status=status.HTTP_200_OK)

        items = Shipment.objects.all()
        serializer = ShipmentSerializer(items, many=True)
        response = serializer.data
        return Response({"status": "true", "shipment": response}, status=status.HTTP_200_OK)




class ShippingToViews(APIView):
    def post(self, request):
        serializer = ShippingToSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = serializer.data
            response['shipping_to_id'] = serializer.data.get('id')
            return Response({"status": "true", "shippingto": response}, status=status.HTTP_200_OK)
        else:
            return Response({"shippingto": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    #permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            item = ShippingTo.objects.get(id=id)
            serializer = ShippingToSerializer(item)
            response = serializer.data
            response['shipping_to_id'] = serializer.data.get('id')
            print(response)
            return Response({"status": "true", "shippingto": response}, status=status.HTTP_200_OK)

        items = ShippingTo.objects.all()
        serializer = ShippingToSerializer(items, many=True)
        return Response({"shippingto": serializer.data}, status=status.HTTP_200_OK)




class ShippingFromViews(APIView):
    def post(self, request):
        serializer = ShippingFromSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = serializer.data
            response['shipping_from_id'] = serializer.data.get('id')
            # Shipment.objects.get(pk=request.data.)
            # ShippingTo.objects.filter()
            return Response({"status": "true", "shippingFrom": response}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "true", "shippingFrom": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    #permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            item = ShippingFrom.objects.get(id=id)
            serializer = ShippingFromSerializer(item)
            response['shipping_to_id'] = serializer.data.get('id')
            print(response)
            return Response({"status": "true", "shippingFrom": response}, status=status.HTTP_200_OK)

        items = ShippingFrom.objects.all()
        serializer = ShippingFromSerializer(items, many=True)
        return Response({"status": "true", "shippingFrom": serializer.data}, status=status.HTTP_200_OK)



class TrackingViews(APIView):
    def post(self, request):
        #
        # shipment_id = Shipment.objects.get(id=1)
        serializer = TrackingSerializer(data=request.data)
        #for m in Shipment.objects.all():
            #m.shipment_key.all()
        if serializer.is_valid():
            serializer.save()
            response = serializer.data
            response['tracking_id'] = response.pop('id')     #213634222610
            response['shipment_id'] = response.pop('shipment')
            response['shipping_to_id'] = response.pop('shipping_to')
            response['shipping_from_id'] = response.pop('shipping_from')
            return Response({"status": "true", "tracking":response}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "true", "tracking": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, tracking_no):
        try:
            item = Tracking.objects.filter(tracking_no=tracking_no).first()
            serializer = TrackingSerializer(item)
            response = serializer.data
            response ['tracking_id']= serializer.data.get('id')
            response['shipment_id'] = serializer.data.get('shipment')
            response['shipping_to_id'] = serializer.data.get('shipping_to')
            response['shipping_from_id'] = serializer.data.get('shipping_from')
            print(response)
            return Response({"status": "true", "trackingJson": serializer.data}, status=status.HTTP_200_OK)
            
        except Tracking.DoesNotExist:
            return Response("Tracking Number is invalid or incorrect, status=status.HTT_404_NOT_FOUND")


      
class CountryViews(APIView):
    def get(self, request, id=None):
        if id:
            item = Country.objects.get(id=id)
            serializer = CountrySerializer(item)
            return Response({"status": "true", "countries": serializer.data}, status=status.HTTP_200_OK)

        items = Country.objects.all()
        serializer = CountrySerializer(items, many=True)
        return Response({"countries": serializer.data}, status=status.HTTP_200_OK)


class StateViews(APIView):
    def get(self, request):
     # Get list of states in a country
        country_id = self.request.query_params.get('country')
        items = State.objects.filter(country=country_id)   
        serializer = StateSerializer(items, many=True)
        return Response({"states": serializer.data}, status=status.HTTP_200_OK)



class CityViews(APIView):
    def get(self, request):
     # Get list of cities in a state
        state_id = self.request.query_params.get('state')
        items = City.objects.filter(state=state_id)   
        serializer = CitySerializer(items, many=True)
        return Response({"cities": serializer.data}, status=status.HTTP_200_OK)


"""
class StateListView(generics.ListAPIView):
    serializer_class = StateSerializer
    #permission_classes = (permissions.AllowAny,)

    # Get list of states in a country
    def get_queryset(self):
        country_id = self.request.query_params.get('country')
        return State.objects.filter(country=country_id)
"""


"""
class CityListView(generics.ListAPIView):
    serializer_class = CitySerializer
    #permission_classes = (permissions.AllowAny,)

    # Get list of states in a country
    def get_queryset(self):
        state_id = self.request.query_params.get('state')
        return City.objects.filter(state=state_id)
"""

"""
class ShippingToViewSet(viewsets.ModelViewSet):
    queryset=ShippingTo.objects.all()
    serializer_class=ShippingToSerializer


class ShippingDocumentViewSet(viewsets.ModelViewSet):
    queryset=ShippingDocument.objects.all()
    serializer_class=ShippingDocumentSerializer


class ShippingFromViewSet(viewsets.ModelViewSet):
    queryset=ShippingFrom.objects.all()
    serializer_class=ShippingFromSerializer


class TrackingViewSet(viewsets.ModelViewSet):
    queryset=Tracking.objects.all()
    serializer_class=TrackingSerializer




class CountryViewSet(viewsets.ModelViewSet):
    queryset=Country.objects.all()
    serializer_class=CountrySerializer


class StateViewSet(viewsets.ModelViewSet):
    queryset=State.objects.all()
    serializer_class=StateSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset=City.objects.all()
    serializer_class= CityToSerializer


"""








"""
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer,RegisterSerializer
from rest_framework.authentication import TokenAuthentication


# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer
"""


from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
})



from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)









def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()