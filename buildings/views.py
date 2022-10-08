from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import BuildingsSerializer
from .models import Buildings
from random import randint

class BuildingsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

      user_id= request.data['user']
      buildings = Buildings.objects.filter(user=user_id)
      serialized = BuildingsSerializer(buildings, many=True)

      return Response(serialized.data,status=status.HTTP_200_OK)


    def post(self, request):

      input_data = {
        'matricula' : randint(100000000000,999999999999),
        'user': request.data['user'],
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


    def delete(self, request):
      matricula = request.data['matricula']
      user_id = request.data['user']
      building = get_object_or_404(Buildings, matricula=matricula)

      if user_id != building.user.id:
        return Response ( {'message' : 'User can only delete it owns buildings'}, status=status.HTTP_401_UNAUTHORIZED)

      building.delete()
  
      return Response({'message' : f"Building {matricula} deleted"},status=status.HTTP_200_OK)


    def patch(self, request):
      matricula = request.data['matricula']
      user_id = request.data['user']

      building = get_object_or_404(Buildings, matricula=matricula)

      if user_id != building.user.id:
        return Response ( {'message' : 'User can only delete it owns buildings'}, status=status.HTTP_401_UNAUTHORIZED)

      serialized = BuildingsSerializer(building, request.data, partial=True)

      if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_200_OK)

class NeighborhoodView(APIView):

    def get(self, request):
      neighborhood = { 'data' : [{'id' : 1, 'name' : 'Madalena'}, {'id' : 2, 'name' : 'Boa Viagem'}, {'id' : 3, 'name' : 'Casa Forte'}, {'id' : 1, 'name' : 'Torre'}]}
      return Response( neighborhood,status=status.HTTP_200_OK)
   