from django.http import HttpResponse

# Create your views here.

def my_blog(request):
    return HttpResponse("Hello, Blog!")

def home(request):
    return HttpResponse("Welcome to the Home Page!")
