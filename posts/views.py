from rest_framework import generics, permissions, authentication
from .serializers import PostSerializer
from .models import Post
from .permissions import IsOwnerOrReadOnly

    
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication]
    
class UserPosts(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication]
    
    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(owner=user)
