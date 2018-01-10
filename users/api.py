from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer


class HelloWorld(APIView):
    def get(self, request):
        return Response(['hello', 'world'])

    def post(self, request):
        return Response(request.data)

    def put(self, request):
        return Response(request.data)


class UsersListAPI(APIView):

    def get(self, request):
        users = User.objects.all()   # users es un objeto que hay que convertir al formato de salida
        serializer = UserSerializer(users, many=True)
        # El serializador obtiene un diccionario por cada usuario de la lista
        return Response(serializer.data)
