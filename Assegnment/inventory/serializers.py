from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Inventory

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')
        
class InventorySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Inventory
        fields = ('author','product_id', 'product_name', 'vendor', 'mrp','batch_num','batch_date','quantity','status')
