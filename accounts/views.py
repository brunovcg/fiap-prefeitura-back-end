from accounts.models import User
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from .serializers import UserSerializer, AllUserSerializer

class LoginView(APIView):

    def post(self, request):
        try:
          username= request.data['username']
          password = request.data['password']
          user = authenticate(username=username, password=password)

          if user:
              token = Token.objects.get_or_create(user=user)[0]

              user_logged = User.objects.get(username=username)


              return Response({'token': token.key, "id": user_logged.id, "username" : user_logged.username, "telefone" : user_logged.telefone, "email" : user_logged.email, "persona" : user_logged.persona }, status=status.HTTP_200_OK)
        except KeyError:
          return Response({"message": "missing cpf or password"}, status=status.HTTP_400_BAD_REQUEST)
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
            return Response({'message': 'User already exists'},status=status.HTTP_409_CONFLICT)

        except KeyError:
           missing = []
           check = ['username', 'email', 'password', 'telefone', 'name']

           for data in check:
            if  data not in request.data:
              missing.append(data)
           return Response({'message': {'missing_fields' : missing}},status=status.HTTP_400_BAD_REQUEST)

        serialized = UserSerializer(new_user)
        return Response(serialized.data, status=status.HTTP_201_CREATED)

class PersonasView(APIView):
  def get(self, request):
    persona = [{'id':1, 'name': 'Impostos' }, {'id':2, 'name': 'Notícias' }, {'id':3, 'name': 'Regulamentação' }]
    return Response(persona, status=status.HTTP_200_OK)


class UserView(APIView):
 def get(self,request):
   users = User.objects.all()
   serialized = AllUserSerializer(users, many=True)
   return Response(serialized.data,status=status.HTTP_200_OK)