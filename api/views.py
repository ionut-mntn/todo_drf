from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

from .models import Task
# Create your views here.

@api_view(['GET', 'POST'])
def apiOverview(request):
    # return JsonResponse("API BASE POINT", safe=False)
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>',
        'Delete': '/task-delete/<str:pk>'
    }
    # return Response("API BASE POINT", safe=False, context=api_urls)
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    print(f"request.data in taskCreate: {request.data}")
    serializer = TaskSerializer(data=request.data) # normally, we do request.POST, but since this is an API view, we have access to request.data!
    
    if serializer.is_valid():
        serializer.save()
        # return Response(serializer.data)
        
    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
    print(f"request.data in taskUpdate: {request.data}")
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data) # ca la forms! We set the instance and then update it!
    
    if serializer.is_valid():
        serializer.save()
        # return Response(serializer.data)
        
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    print(f"request.data in taskDelete: {request.data}")
    
    # ori asa:
    # SomeModel.objects.filter(id=id).delete()
    
    # ori dupa ce ne luam instanta
    task = Task.objects.get(id=pk)
    task.delete()
    
    return Response('Item successfully deleted!')
