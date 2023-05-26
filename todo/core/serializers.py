
from core.models import User,Task
from rest_framework import serializers
from django.db import transaction
from dj_rest_auth.registration.serializers import RegisterSerializer
#from dj_rest_auth.serializers import LoginSerializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance




class CustomRegisterSerializer(RegisterSerializer):
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        #user.gender = self.data.get('gender')
        #user.phone_number = self.data.get('phone_number')
        user.save()
        return user

class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            
        )
        read_only_fields = ('id', 'email',)

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model=Task 
        fields='__all__'