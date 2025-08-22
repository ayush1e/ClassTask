from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
 

from .models import User
from django.contrib.auth.hashers import make_password, check_password

import jwt
from django.conf import settings
from datetime import datetime, timedelta


 



@csrf_exempt
def registration(request):
  if request.method == 'POST':
    # Handle registration logic here
    data = json.loads(request.body.decode('utf-8'))
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
      return JsonResponse({
        'message':'All fields are required',
        'success': 'failed',
        
      }, status=400)
    
    if User.objects.filter(username=username).exists():
      return JsonResponse({
        "message":"user already exist",
        "success": False
        }
      )
    
    user = User(username = username, email = email, password = make_password(password = password) )
    user.save()
    return JsonResponse({
      "message" : " User Created SuccessFully",
      "success" : True
    })

  else:
    return JsonResponse({
      'message':'request methode is not correct',
      'success': 'failed',
      
    }, status=400)
  

@csrf_exempt
def login(request):
  if request.method == 'POST':
    data = json.loads(request.body.decode('utf-8'))
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
      return JsonResponse({"message": "Username and password required", "success": False}, status=400)

    try:
      user = User.objects.get(username=username)
    except User.DoesNotExist:
      return JsonResponse({"message": "Invalid username or password", "success": False}, status=401)

    if not check_password(password, user.password):
      return JsonResponse({"message": "Invalid username or password", "success": False}, status=401)

    payload = {
      'id': user.id,
      'username': user.username,
      'exp': datetime.utcnow() + timedelta(hours=1)
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

    return JsonResponse({
      "message": "Login successfully",
      "token": token,
      "user": {
        "id": user.id,
        "username": user.username,
        "email": user.email
      },
      "success": True
    })
  else:
    return JsonResponse({
      "message": "Method is not POST",
      "success": False
    }, status=405)

 
def dashboard(request):
  return HttpResponse("<h1>dashboard Page</h1>") 