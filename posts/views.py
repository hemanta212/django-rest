from django.contrib.auth.models import User
from rest_framework import viewsets
from .permissions import IsAuthorOrReadOnly
from .models import Post
from .serializers import PostSerializer, UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
