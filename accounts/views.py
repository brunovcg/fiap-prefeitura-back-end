from accounts.models import User
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from .serializers import UserSerializer

class LoginView(APIView):

    def post(self, request):

        username= request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)

        if user:
            token = Token.objects.get_or_create(user=user)[0]

            user_logged = User.objects.get(username=username)


            return Response({'token': token.key,  "username" : user_logged.username, "telefone" : user_logged.telefone, "email" : user_logged.email })

        return Response({"message": "wrong cpf or password"}, status=status.HTTP_401_UNAUTHORIZED)


class SignupView(APIView):

    def post(self, request):     

        try:
            new_user =  User.objects.create_user(
                username = request.data["username"],
                email = request.data["email"],
                password = request.data["password"],
                telefone = request.data["telefone"],
                name = request.data["name"],
            )

        except IntegrityError:
            return Response({"User already exists"},status=status.HTTP_409_CONFLICT)

        serialized = UserSerializer(new_user)

        return Response(serialized.data, status=status.HTTP_201_CREATED)