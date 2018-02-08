import datetime

from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.views import APIView

from users.serializers import BlogsListSerializer
from blogs.models import Post
from blogs.serializers import PostsListSerializer, PostSerializer
from blogs.permissions import PostPermission


class BlogsListAPI(APIView):

    permission_classes = [IsAdminUser]

    def get(self, request):

        users = User.objects.all()
        query_params = request.query_params
        blog_name = query_params.get('blog_name', None)
        if blog_name is not None:
            users = users.filter(username__icontains=blog_name)
        order = query_params.get('order', 'ASC')
        if order == 'DESC':
            users = users.order_by('-username')
        else:
            users = users.order_by('username')

        paginator = PageNumberPagination()
        paginated_users = paginator.paginate_queryset(users, request)
        serializer = BlogsListSerializer(paginated_users, many=True)
        return paginator.get_paginated_response(serializer.data)


class PostsListAPI(ListCreateAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = (TokenAuthentication,)
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'summary']
    ordering_fields = ['title', 'publication_date']

    def get_queryset(self):
        now = datetime.datetime.now()
        user = self.request.user
        queryset = Post.objects.all()
        if user.is_authenticated and user.is_superuser:
            return queryset.order_by('-publication_date')
        else:
            return queryset.filter(publication_date__lte=now.strftime("%Y-%m-%d")).order_by('-publication_date')

    def get_serializer_class(self):
        return PostsListSerializer if self.request.method == 'GET' else PostSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)


class PostDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [PostPermission]
    authentication_classes = (TokenAuthentication,)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
