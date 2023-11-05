from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Homepage, name='events/Homepage'),
    path('events_list/', views.events_list, name='events/events_list'),
    path('createevent/', views.createevent, name='events/createevent'),
    path('AdminHome/', views.AdminHome, name='events/AdminHome'),
    path('UserHome/', views.UserHome, name='events/UserHome'),
    path('ServiceProviderHome/', views.ServiceProviderHome, name='events/ServiceProviderHome'),
    path('register/', views.register, name='events/register'),
    path('login/', auth_views.LoginView.as_view(template_name='events/login.html'), name='events/login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='events/logout.html'), name='events/logout'),
    path('adminlogin/', views.adminlogin, name='events/adminlogin'),
    path('adminlogout/', views.adminlogout, name='events/adminlogout'),
    path('serviceproviderlogin/', views.serviceproviderlogin, name='events/serviceproviderlogin'),
    path('serviceproviderlogout/', views.serviceproviderlogout, name='events/serviceproviderlogout'),
    path('index/', views.index, name='events/index'),
    path('eventsAvailable/', views.eventsAvailable, name='events/eventsAvailable'),
    path('payment/', views.payment, name='events/payment'),
    path('ContactUs/', views.ContactUs, name='events/ContactUs'),
   path('AboutUs/', views.AboutUs, name='events/AboutUs'),
    path('booking/<str:event_type>/', views.booking, name='events/booking'),
   path('addserviceprovider/', views.addserviceprovider, name='events/addserviceprovider'),

    # URL pattern for removing a service provider
    path('removeserviceprovider/', views.removeserviceprovider, name='events/removeserviceprovider'),
     path('myview/', views.myview, name='myview'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
