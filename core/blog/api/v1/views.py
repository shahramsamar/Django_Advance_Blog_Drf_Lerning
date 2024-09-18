from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ...models import Post
from .serializers import PostSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

data = {
    'id':1,
    'title':'hello'
}

@api_view()
def post_list(request):
    post = Post.objects.filter(status=True)
    serializer = PostSerializer(post,many=True)
    return Response(serializer.data)

@api_view()
def post_detail(request,id):
    # try:
    #     post = Post.objects.get(pk=id)
    #     # print(post.__dict__)
    #     serializer = PostSerializer(post)
    #     # print(serializer.data)
    #     return Response(serializer.data)
    # except Post.DoesNotExist:
        # return Response({"detail":"post dose not exist"},status=status.HTTP_404_NOT_FOUND)
    
        post = get_object_or_404(Post,pk=id,status=True)
        serializer = PostSerializer(post)
        return Response(serializer.data)