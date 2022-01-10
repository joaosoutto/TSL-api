from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostList, PostDetail, UserPosts

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    path('my-posts/', UserPosts.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)