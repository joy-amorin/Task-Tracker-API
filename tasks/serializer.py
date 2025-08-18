from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

class TaskSerilizer(serializers.ModelSerializer):

    class Meta:

        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'updated_at', 'owner']
        read_only_fields = ['id', 'created_at', 'updated_at', 'owner']

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):

        #created_user encrypting th e password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        return user