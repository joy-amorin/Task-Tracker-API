from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializer import TaskSerilizer

# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])

def task_list_create(request):

    if request.method == 'GET':
        tasks = Task.objects.filter(owner=request.user) #User tsks only
        serializer = TaskSerilizer(tasks, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TaskSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user) #Automatically assign owner
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])

def task_detail(request, pk):

    try:
        task = Task.objects.get(pk=pk, owner=request.user)
    except Task.DoesNotExist:
        return Response({'error': 'tarea no encontrada'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TaskSerilizer(task)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = TaskSerilizer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])

def delete_task(request, pk):
    try:
        task = Task.objects.get(pk=pk, owner=request.user)
    except Task.DoesNotExist:
        return Response({'error':'tarea no encontrada'}, status=status.HTTP_404_NOT_FOUND)
  
    task.delete()

    return Response({'mensaje': 'Tarea borrada exitosamente'},status=status.HTTP_204_NO_CONTENT)