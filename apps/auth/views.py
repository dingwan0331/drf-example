import json

import bcrypt

from django.views import View
from django.http  import JsonResponse

from apps.auth.models import User

class UserView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        username = data['username']
        password = data['password']
        email    = data['email']

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        dto = {
            'username': username,
            'password': hashed_password,
            'email' : email
        }

        print(User.objects.create(**dto))
        return JsonResponse({})