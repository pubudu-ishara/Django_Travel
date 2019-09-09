from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='travel-home'),
    path('blog/', views.blog, name='travel-blog'),
    path('aboutus/', views.aboutus, name='travel-aboutus'),
    path('contact/', views.contact, name='travel-contact'),
    path('booking/', views.booking, name='travel-booking'),
]
