from datetime import datetime

from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import *

class IsUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

def validate(serializer):
    if not serializer.is_valid():
        return Response(data={
            'message': 'Invalid input',
            'errors': serializer.errors
    }, status=status.HTTP_406_NOT_ACCEPTABLE)

def update_last_request(request):
    user = User.objects.get(id=request.user.id)
    user.last_activity=datetime.now()
    user.save()


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CreatePostView(APIView):
    allowed_methods = ['POST']
    serializer_class = PostCreateSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = (IsUser,)
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        validate(serializer)
        serializer.validated_data['user'] = request.user
        new_post = Post.objects.create(**serializer.validated_data)

        update_last_request(request)

        return Response(status=status.HTTP_200_OK, data=self.serializer_class(new_post).data)


class LikeAnalycticsView(generics.ListAPIView):
    serializer_class = LikeSerializer

    def get_queryset(self):
        queryset = Like.objects.all()
        params = self.request.query_params
        date_from = params.get('date_from', None)
        date_to = params.get('date_to', None)

        if date_from:
            queryset = queryset.filter(created__gte=date_from, like=1)
        if date_to:
            queryset = queryset.filter(created__lte=date_to, like=1)
        return queryset

class CreateLikeView(APIView):
    serializer_class = LikeCreateSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = (IsUser,)
    allowed_methods = ['POST']

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        validate(serializer)

        serializer.validated_data['user'] = request.user

        update_last_request(request)

        new_like = Like.objects.create(**serializer.validated_data)

        if new_like.like == 1:
            updateLike = Like.objects.filter(post=new_like.post,
                                             created__lt=new_like.created, user=new_like.user)
            updateLike.delete()

        elif new_like.like == 2:
            updateLike = Like.objects.filter(post=new_like.post, created__lt=new_like.created,
                                             user=new_like.user)
            updateLike.delete()

        return Response(status=status.HTTP_200_OK, data=LikeSerializer(new_like).data)
