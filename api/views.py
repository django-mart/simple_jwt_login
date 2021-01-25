from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny

from django.contrib.auth.models import User

# Create your views here.
class Register(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        return Response(
            {
                "message": "try to access this as post api"
            },
            status=status.HTTP_200_OK
        )
    
    def post(self, request, format=None):
        try:
            userData = JSONParser().parse(request)
            
            user = User.objects.create_user(
                username=userData["username"],
                password=userData["password"]
            )
            user.save()

            return Response(
                {
                    "message": "new user created successfully"
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    "message": "error occured",
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
class HelloWorld(APIView):
    def get(self, request, format=None):
        return Response(
            {
                "message": "Hello world!!!"
            },
            status=status.HTTP_200_OK
        )