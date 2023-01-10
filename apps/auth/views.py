import json

import bcrypt

from django.views import View
from django.http  import JsonResponse

from rest_framework.response import Response

from apps.auth.models      import User
from apps.auth.serializers import UserSerializer

class UserView(View):
    def get(self, reqeust):
        user_row   = User.objects.get(id=1)
        serializer = UserSerializer(user_row)

        return JsonResponse({'user': serializer.data})

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