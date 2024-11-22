from rest_framework.templatetags.rest_framework import items
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from appfaceregister.api import serializer
from appfaceregister.models import Aluno, Professor
from appfaceregister.api.serializer import AlunoSerializer, ProfessorSerializer

class AlunoViewsSets (APIView):
    def get(self, request, id=None):
        if id:
            aluno= get_object_or_404(Aluno, id=id)
            serializer = AlunoSerializer(aluno)
            return Response(serializer.data)
        items = Aluno.objects.all()
        serializer = AlunoSerializer(items, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        item = get_object_or_404(Aluno, id = id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        item = get_object_or_404(Aluno, id = id)
        serializer = AlunoSerializer(item, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProfessorViewsSets(APIView):
    def get(self, request, id=None):
        if id:
            professor = get_object_or_404(Professor, id=id)
            serializer = ProfessorSerializer(professor)
            return Response(serializer.data)
        items = Professor.objects.all()
        serializer = ProfessorSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        item = get_object_or_404(Professor, id=id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        item = get_object_or_404(Professor, id=id)
        serializer = ProfessorSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

