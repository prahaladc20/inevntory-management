from django.shortcuts import render
from rest_framework import status

from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import (IsAuthenticated,AllowAny)
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authentication import TokenAuthentication
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from . import serializers

from .models import Inventory 
from django.contrib.auth.models import User
from .serializers import InventorySerializer,UserSerializer
from .permissions import IsLoggedInUserOrAdmin,IsAdminUser



class UserViewSet(viewsets.ModelViewSet):
	print("123654895555555555555")
	queryset = User.objects.all()
	serializer_class = serializers.UserSerializer
	# authentication_classes = (SessionAuthentication, BasicAuthentication)
 
	# permission_classes = (ReadOnly, )
	print(serializer_class, "serializer_class")
	# authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated, )

	def get_permissions(self):
		permission_classes = []
		if self.action == 'create':
			permission_classes = [AllowAny]
		elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
			permission_classes = [IsLoggedInUserOrAdmin]
		elif self.action == 'list' or self.action == 'destroy':
			permission_classes = [IsAdminUser]
		return [permission() for permission in permission_classes]

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class InventoryList(APIView):
	print("lllllllllllllllllllllllll")
	# queryset = Inventory.objects.all()
	# serializer_class = InventorySerializer
	permission_classes = (IsAuthenticated,)
	# authentication_classes = (SessionAuthentication, BasicAuthentication)
 

	@csrf_exempt
	def get(self, request, format=None):
		print("lllllllllllllllllllllllll",request.user.groups.values_list('name',flat = True))

		# if (request.user.groups.filter(name = 'Store Manager').exists()) or (request.user.groups.filter(name = 'Store Assistant').exists() and request.user.groups.filter(name = 'Store Manager').exists()):
		# 	result = Inventory.objects.filter(status=0)
		# else:
		# 	result = Inventory.objects.filter(status=1)
		result = Inventory.objects.all()
		print(result)
		# serializer_class = serializers.InventorySerializer
		serializers = InventorySerializer(result,many=True)

		return Response(serializers.data)	

	def post(self,request,format=None):
		print("lllllllllllllllllllllllll+++",request.data)

		if (request.user.groups.filter(name = 'Store Manager').exists()) or (request.user.groups.filter(name = 'Store Assistant').exists() and request.user.groups.filter(name = 'Store Manager').exists()):
			request.data['status'] = 1
			print("LLLLLLLLLL",request.data)
			
		else:
			request.data['status'] = 0
		serializer = InventorySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class InventoryDetail(APIView):
	print("lllllllllllllllllllllllll")
	# queryset = Inventory.objects.all()
	# serializer_class = InventorySerializer

	def get_object(self, pk):
		print("PPPPPPPPPPPP")
		try:
			return Inventory.objects.get(pk=pk)
		except Inventory.DoesNotExist:
			raise Http404


	def get(self, request, pk, format=None):
		print("lllllllllllllllllllllllll")
		result = Inventory.objects.all()
		print(result)
		# serializer_class = serializers.InventorySerializer
		serializers = InventorySerializer(result,many=True)

		return Response(serializers.data)	

	def post(self,request,*args,**kwargs):
		print("lllllllllllllllllllllllll+++",request.data)

		serializer = InventorySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, pk, format=None):
		snippet = self.get_object(pk)
		if (request.user.groups.filter(name = 'Store Manager').exists()) or (request.user.groups.filter(name = 'Store Assistant').exists() and request.user.groups.filter(name = 'Store Manager').exists()):
			request.data['status'] = 1
		else:
			request.data['status'] = 0
		serializer = InventorySerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		snippet = self.get_object(pk)
		snippet.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


# class InventoryPostSet(viewsets.ModelViewSet):
#     print("lllllllllllllllllllllllll")
#     queryset = Inventory.objects.all()
#     serializer_class = InventorySerializer


#     def post(self,request,*args,**kwargs):
#     	print("llllllllllllpostttlllllllllllll+++")
#     	result = Inventory.objects.all()
#     	print(result)
    	
#     	serializers = InventorySerializer(result,many=True)

#     	return Response(serializers.data)	
