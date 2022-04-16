from django.shortcuts import render
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def index(request):

    #get all drinks serialized and return json
    if(request.method == 'GET'):
        drinks = Drink.objects.all()
        serializer = DrinkSerializers(drinks, many=True)
        return JsonResponse({"data":serializer.data}, safe=False)
    
    if(request.method == 'POST'):
        serializer = DrinkSerializers(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def drink_detail(request,id):

    try:
        drinks = Drink.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if(request.method == 'GET'):
        serializer = DrinkSerializers(drinks)
        return JsonResponse({"data":serializer.data}, safe=False)
    
    if(request.method == 'PUT'):
        serializer = DrinkSerializers(drinks,data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if(request.method == 'DELETE'):
        drinks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)