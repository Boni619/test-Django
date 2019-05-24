
from django.http import HttpResponse


def home_page(request):
    return HttpResponse("<h1>Hello world</h1>")


def about(request):
    return HttpResponse("<h4>About us</h4>")


def contact(request):
     return HttpResponse("<h3>Contact us</h3>")
