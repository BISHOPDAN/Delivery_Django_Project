from django.urls import path, include
#from .import views 
from .views import CityViews, ShipmentViews, ShippingFromViews, ShippingToViews, TrackingViews, CountryViews, StateViews, CityViews
from .views import RegisterAPI
from .views import LoginAPI
from knox import views as knox_views




"""
from .views import UserDetailAPI,RegisterUserAPIView
urlpatterns = [
  path("get-details",UserDetailAPI.as_view()),
  path('register',RegisterUserAPIView.as_view()),
]
"""


urlpatterns = [
    
    path('auth/', include('rest_framework.urls')),
    path('shipment/', ShipmentViews.as_view()),
    path('shippingto/', ShippingToViews.as_view()),
    path('shippingfrom/', ShippingFromViews.as_view()),
    path('track/<int:tracking_no>', TrackingViews.as_view()),
    path('track/', TrackingViews.as_view()),
    path('country/', CountryViews.as_view()),
    path('states/', StateViews.as_view(), name='states'),
    path('cities/', CityViews.as_view(), name='cities'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
  
]



