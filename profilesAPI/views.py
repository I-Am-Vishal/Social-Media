from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from profilesAPI.serializers import ProfileSerializer,RelationshipSerializer
from profiles.models import Profile,Relationship

# Create your views here.

@api_view(['GET'])
def Allprofiles(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Viewprofiles(request, pk):
    profiles = Profile.objects.get(user=pk)
    serializer = ProfileSerializer(profiles, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def Createprofile(request):
    serializer = ProfileSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['PUT'])
def updateprofile(request, pk):
    profiles = Profile.objects.get(user=pk)
    serializer = ProfileSerializer(instance=profiles, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteprofile(request, pk):
    profiles = Profile.objects.get(user=pk)
    profiles.delete()

    return Response('Items deleted successfully!')

#########################################################################################

@api_view(['GET'])
def Allrelationship(request):
    relationships = Relationship.objects.all()
    serializer = RelationshipSerializer(relationships, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Viewrelationship(request, pk):
    relationships = Relationship.objects.get(id=pk)
    serializer = RelationshipSerializer(relationships, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def Createrelationship(request):
    serializer = RelationshipSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['POST'])
def updaterelationship(request, pk):
    relationships = Relationship.objects.get(id=pk)
    serializer = RelationshipSerializer(instance=relationships, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleterelationship(request, pk):
    relationships = Relationship.objects.get(id=pk)
    relationships.delete()

    return Response('Items deleted successfully!')

#########################################################################################