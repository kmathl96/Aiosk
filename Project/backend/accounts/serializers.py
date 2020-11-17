from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phoneNum', 'point')

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ('id', 'code', 'user')

class Class5Serializer(serializers.ModelSerializer):
    class Meta:
        model = Class5
        fields = ('id', 'user', 'letter')