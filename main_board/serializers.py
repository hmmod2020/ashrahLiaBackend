from rest_framework import serializers
from .models import *


class user_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model=user_info
        fields='__all__'
class order_upSerializer(serializers.ModelSerializer):
    class Meta:
        model=order_up
        fields='__all__'
