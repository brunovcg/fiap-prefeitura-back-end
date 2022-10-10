from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import BuildingsSerializer
from .models import Buildings
from random import randint
from accounts.models import User


class OneBuildingsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, matricula=""):
      user_id = request.user.id
      building = get_object_or_404(Buildings, matricula=matricula)
      if user_id != building.user.id:
        return Response ( {'message' : 'User can only delete it owns buildings'}, status=status.HTTP_401_UNAUTHORIZED)
      building.delete()
      return Response({'message' : f"Building {matricula} deleted"},status=status.HTTP_200_OK)


    def patch(self, request, matricula=""):

      fields = ["tamanho", "endereco", "bairro"]

      if request.data == {}:
        return Response ( {'message': f'User need to set in request body at least one of the fields: {fields}' }, status=status.HTTP_400_BAD_REQUEST)

      for field in request.data:
        if field not in fields:
          return Response ( {'message': f'User can only change: {fields}, {field} not allowed' }, status=status.HTTP_400_BAD_REQUEST)

      user_id = request.user.id
      building = get_object_or_404(Buildings, matricula=matricula)
      if user_id != building.user.id:
        return Response ( {'message' : 'User can only delete it owns buildings'}, status=status.HTTP_401_UNAUTHORIZED)
      serialized = BuildingsSerializer(building, request.data, partial=True)
      if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_200_OK)


class BuildingsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

      user_id = request.user.id

      get_object_or_404(User, id= user_id)

      buildings = Buildings.objects.filter(user=user_id)
      serialized = BuildingsSerializer(buildings, many=True)

      return Response(serialized.data,status=status.HTTP_200_OK)

    def post(self, request):
      try:
        def generate_iptu():
          bairro = request.data["bairro"]
          tamanho = request.data["tamanho"]
          if (bairro == 1):
            return tamanho * 2
          if (bairro == 2):
            return tamanho * 2.5
          if (bairro == 3):
            return tamanho * 2.7
          else:
            return tamanho * 2.4
        
        def generateMatricula():
          genId = randint(100000,900000)
          exists = Buildings.objects.filter(matricula= genId).exists()
          if not exists:
            return genId
          else:
            generateMatricula()

        matricula = generateMatricula()

        input_data = {
          'matricula' : matricula,
          'iptu': generate_iptu() ,
          'user': request.user.id,
	        'tamanho' : request.data['tamanho'],
	        'endereco': request.data['endereco'],
	        'bairro' : request.data['bairro'],
        }

        serialized = BuildingsSerializer(data=input_data)
        if serialized.is_valid():
          serialized.save()
          return  Response(serialized.data, status=status.HTTP_201_CREATED)

        else:   
          return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
      except KeyError:
        missing = []
        check = [ 'tamanho', 'endereco', 'bairro']
        for data in check:
         if  data not in request.data:
           missing.append(data)
        return Response({'message': {'missing_fields' : missing}},status=status.HTTP_400_BAD_REQUEST)    

class NeighborhoodView(APIView):
    # TODO ROTA MOCKADA PARA POSTERIOR DESENVOLVIMENTO
    def get(self, request):
      neighborhood =[{'id' : 1, 'name' : 'Madalena'}, {'id' : 2, 'name' : 'Boa Viagem'}, {'id' : 3, 'name' : 'Casa Forte'}, {'id' : 1, 'name' : 'Torre'}]
      return Response( neighborhood,status=status.HTTP_200_OK)
   
