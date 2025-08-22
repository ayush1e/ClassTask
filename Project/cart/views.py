from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
 

# Create your views herd

def dataview(request):
  data = {
       'user' : 'Ayush Yadav',
       'age' : 25,
       'password' : 'your_password_here'
  }

  return JsonResponse(data)

def index(request):
  return HttpResponse( 
  "<h1 style='color: blue;'>Hello, world!</h1>"
  )