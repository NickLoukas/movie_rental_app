from datetime import datetime
from rest_framework import serializers
from movies.models import Movie, Order
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=100, style={"input_type":"password"})

    def create(self, validated_data):
        """The function called when you create a new User object/instance"""

        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'description', 'genre')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Order` instance, given the validated data.
        """
        now = datetime.now()
        created = instance.created.replace(tzinfo=None)
        returned = validated_data['returned'].replace(tzinfo=None)
        if instance.returned != validated_data['returned']:
            days = (returned - created).days
            if days == 0:
                instance.price = 1.0
            elif days<=3:
                instance.price = float(days)
            else:
                instance.price = float(3+(days-3)*0.5)
        elif validated_data['status'] == 'CLOSED' and instance.status != 'CLOSED':
            if not instance.returned:
                instance.returned = datetime.now()
            days = (instance.returned.replace(tzinfo=None) - created).days
            if days == 0:
                instance.price = 1.0
            elif days<=3:
                instance.price = float(days)
            else:
                instance.price = float(3+(days-3)*0.5)

        instance.status = validated_data.get('status', instance.status)
        instance.returned = validated_data.get('returned', instance.returned)
        instance.save()
        return instance
