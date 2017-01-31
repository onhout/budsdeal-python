from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from user.models import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.


def login(request):
    return render(request, 'login.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        if pk == 'i':
            return Response(UserSerializer(request.user,
                                           context={'request': request}).data)
        return super(UserViewSet, self).retrieve(request, pk)
