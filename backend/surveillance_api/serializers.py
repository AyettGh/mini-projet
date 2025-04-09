from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Professor, Session, Formula

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = "__all__"


class SessionSerializer(serializers.ModelSerializer):
    professor_1_name = serializers.CharField(source="professor_1.name", read_only=True)
    professor_2_name = serializers.CharField(source="professor_2.name", read_only=True)

    class Meta:
        model = Session
        fields = ["session_id", "date", "time", "professor_1_name", "professor_2_name"]

class FormulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formula
        fields = ["formula"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        return user

class FormulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formula
        fields = ["formula"]
