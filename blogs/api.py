from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import BlogsListSerializer

from users.serializers import UsersListSerializer


class BlogsListAPI(APIView):

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

