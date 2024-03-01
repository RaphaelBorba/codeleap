from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Posts
from .serializers import PostSerializer

@api_view(["GET", "POST"])
def get_or_create(request):

    if request.method == "GET":
        app = Posts.objects.all()
        serializer = PostSerializer(app, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        isValid = serializer.is_valid()
        if isValid:
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        
def updatePost(request, post_id):
    try:
        post = Posts.objects.get(id=post_id)
    except Posts.DoesNotExist:
        return Response({"error": "Post not found"}, status=404)
    data = {
        'title': request.data.get('title'),
        'content': request.data.get('content')
    }
    serializer = PostSerializer(post, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)
    
def deletePost(request, post_id):
    try:
        post = Posts.objects.get(id=post_id)
    except Posts.DoesNotExist:
        return Response({"error": "Post not found"}, status=404)

    operation = post.delete()
    if operation:
        return Response()
    else:
        return Response("Fail in Delete!")
    

@api_view(["PATCH", "DELETE"])
def delete_or_update(request, post_id):
    if request.method == "PATCH":
        try:
            post = Posts.objects.get(id=post_id)
        except Posts.DoesNotExist:
            return Response({"error": "Post not found"}, status=404)
        data = {
            'title': request.data.get('title'),
            'content': request.data.get('content')
        }
        serializer = PostSerializer(post, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
    elif request.method == "DELETE":
        try:
            post = Posts.objects.get(id=post_id)
        except Posts.DoesNotExist:
            return Response({"error": "Post not found"}, status=404)

        operation = post.delete()
        if operation:
            return Response()
        else:
            return Response("Fail in Delete!")


