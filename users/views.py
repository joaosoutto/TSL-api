from rest_framework import generics
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http.response import JsonResponse
from .serializers import UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def post(self, request):     
        try:
            User.objects.create_user(
                username=request.data['username'],
                email=request.data['email'],
                password=request.data['password'],
            )
        except IntegrityError:
            return JsonResponse({"Error": True}, status=409)
        
        return JsonResponse({"success": f"User {request.data['username']} created!"}, status=201)

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer