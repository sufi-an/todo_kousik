from django.shortcuts import render
from datetime import datetime
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
# models
from core.models import User,Task

# Serializers
from core.serializers import UserSerializer,TaskSerializer
# Create your views here.
   
#---------
# User |
#---------

class UserList(APIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(detail=False, methods=['GET','POST'])
    def get(self,request):
        print(request)
        snippet = User.objects.all()
        serializer = self.serializer_class(snippet,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer= UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UserDetails(APIView):
    serializerClass = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    @action(detail=True, methods=['get','put','delete'])
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    def get(self, request,  format=None):
        snippet = self.get_object(request.query_params.get('id'))
        serializer = self.serializerClass(snippet)
        return Response(serializer.data)

    def put(self, request,  format=None):
        snippet = self.get_object(request.query_params.get('id'))
        serializer = self.serializerClass(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,  format=None):
        snippet = self.get_object(request.query_params.get('id'))
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

  
#---------
# Task |
#---------

class TaskList(APIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all()
    @action(detail=False, methods=['GET','POST'])
    def get(self, request, id, format=None):
       
        # snippet = self.get_object(request.query_params.get('id'))
        snippet = Task.objects.filter(user=id)
        serializer = self.serializer_class(snippet,many=True)
        print(serializer.data)
        return Response(serializer.data)
    def post(self,request,id):
        serializer= TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class TaskDetails(APIView):
    serializerClass = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    @action(detail=True, methods=['get','post','put','delete'])
    def get_object(self, pk,task):
        try:
            return Task.objects.get(user=pk,id=task)
        except Task.DoesNotExist:
            raise Http404
    
    def put(self, request, id,task ,format=None):
        snippet = self.get_object(id,task)
        serializer = self.serializerClass(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id,task, format=None):
        snippet = self.get_object(id,task)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
