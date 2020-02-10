from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
#from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from login.models import Example2
from login.serializer import Example2Serializers

class CustonAuthToken(ObtainAuthToken):
    
    def post(self, request, * args, **kwars):
        serializer = self.serializer_class (data = request.data, 
                                            context = {
                                                    'request': request, 
                                                    }
                                            )
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })

class ExampleList2(APIView):
    def get(self,request , formar=None):
        print("Metodo get filter")
        queryset = Example2.objects.filter(delete = False)
        serializer = Example2Serializers(queryset , many = True)
        return Response(serializer.data)