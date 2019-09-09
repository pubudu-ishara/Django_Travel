from django.shortcuts import render
from django.http import HttpResponse
from .models import PostDB

# Temp data


def home(request):
    return render(request, 'Travel/home.html')


def blog(request):
    context = {
        'postskey': PostDB.objects.all()
    }
    return render(request, 'Travel/blog.html', context, {'title': 'Blog'})


def aboutus(request):
    return render(request, 'Travel/about.html', {'title': 'AboutUs'})


def contact(request):
    return render(request, 'Travel/contact.html', {'title': 'Contact'})


def booking(request):
    return render(request, 'Travel/booking.html', {'title': 'Booking'})
# Create your views here.
