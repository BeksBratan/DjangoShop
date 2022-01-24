from multiprocessing import AuthenticationError
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response



@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        user = authenticate(**request.data)
        # username = request.data['username']         **********************
        # password = request.data['password']                Второй варик
        # user = authenticate(username=username, password=password)   ***************
        if user:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return Response(data={'token': token.key})
        return Response(data={'user not found'}, status=404)

from django.contrib.auth.models import User
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        User.objects.create_user(username=username, password=password)
        return Response(data={'user create'}, status=201)
