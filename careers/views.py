#from django.shortcuts import render
from rest_framework. viewsets import ModelViewSet
from .models import PostModel, LikesModel
from .serializers import PostSerializer, LikesSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class PostViewSet(ModelViewSet):
    queryset= PostModel.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_datetime', 'title']
    ordering = ['-created_datetime']

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):

        post = self.get_object()
        user = request.data.get("username")

        if not user:
            return Response({"detail": "Campo 'username' é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)

        if LikesModel.objects.filter(username=user, post_id=post).exists():
            return Response({"detail": "Você já curtiu esse post."},status=status.HTTP_400_BAD_REQUEST)

        LikesModel.objects.create(username=user, post_id=post)
        post.likes +=1
        post.save()

        return Response({'status': 'liked', 'likes': post.likes}, status=status.HTTP_200_OK)
    
class LikesViewSet(ModelViewSet):
    queryset = LikesModel.objects.all()
    serializer_class = LikesSerializer
