from rest_framework import generics
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http.response import JsonResponse
from .serializers import UserSerializer
from django.core.mail import send_mail

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
        
        try:
            username=request.data['username']
            email=request.data['email']
            send_mail(
                f'Your account was created!',
                f'Hello, {username}! \n Welcome to The Silver Wall! \n Now you can login with your email ({email}) and your password to post a lot in our Wall! \n Best regards, The Silver Wall.',
                f'Welcome to TSW! <joaosouttowallapp@gmail.com>',
                [request.data['email']],
                fail_silently=False,
            )
        except:
            print('Error sending email')
        
        return JsonResponse({"success": f"User {request.data['username']} created!"}, status=201)

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer