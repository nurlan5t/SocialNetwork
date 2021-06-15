from django.urls import path
from .views import *

urlpatterns = [
    path('posts/all', PostListView.as_view()),
    path('posts/create', CreatePostView.as_view()),
    path('likes/all', LikeAnalycticsView.as_view()),
    path('likes/create', CreateLikeView.as_view()),
]
