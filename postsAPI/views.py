from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from postsAPI.serializers import PostSerializer,LikeSerializer,CommentSerializer
from posts.models import Post,Like,Comment

# Create your views here.

@api_view(['GET'])
def Allposts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Viewposts(request, pk):
    posts = Post.objects.get(id=pk)
    serializer = PostSerializer(posts, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def Createposts(request):
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['POST'])
def updateposts(request, pk):
    posts = Post.objects.get(id=pk)
    serializer = PostSerializer(instance=posts, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteposts(request, pk):
    posts = Post.objects.get(id=pk)
    posts.delete()

    return Response('Items deleted successfully!')

######################################################################################################

@api_view(['GET'])
def Alllikes(request):
    likes = Like.objects.all()
    serializer = LikeSerializer(likes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Viewlikes(request, pk):
    likes = Like.objects.get(id=pk)
    serializer = LikeSerializer(likes, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def Createlikes(request):
    serializer = LikeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['POST'])
def updatelikes(request, pk):
    likes = Like.objects.get(id=pk)
    serializer = LikeSerializer(instance=likes, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deletelikes(request, pk):
    likes = Like.objects.get(id=pk)
    likes.delete()

    return Response('Items deleted successfully!')

####################################################################################################

@api_view(['GET'])
def Allcomments(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Viewcomments(request, pk):
    comments = Comment.objects.get(id=pk)
    serializer = CommentSerializer(comments, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def Createcomments(request):
    serializer = CommentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['POST'])
def updatecomments(request, pk):
    comments = Comment.objects.get(id=pk)
    serializer = CommentSerializer(instance=comments, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deletecomments(request, pk):
    comments = Comment.objects.get(id=pk)
    comments.delete()

    return Response('Items deleted successfully!')