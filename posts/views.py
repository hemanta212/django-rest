from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .permissions import IsAuthorOrReadOnly, IsSelfOrReadOnly
from .models import Post
from .serializers import PostSerializer, UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly, permissions.IsAuthenticated)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsSelfOrReadOnly, permissions.IsAuthenticated)
    queryset = User.objects.all()
    serializer_class = UserSerializer
