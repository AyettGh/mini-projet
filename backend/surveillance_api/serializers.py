<<<<<<< HEAD
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
=======
>>>>>>> d968a2574d3a78eb777d428b9fce10c5cae2e480
from rest_framework import serializers
from .models import Professor, Session, Formula

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = "__all__"

<<<<<<< HEAD
=======

>>>>>>> d968a2574d3a78eb777d428b9fce10c5cae2e480
class SessionSerializer(serializers.ModelSerializer):
    professor_1_name = serializers.CharField(source="professor_1.name", read_only=True)
    professor_2_name = serializers.CharField(source="professor_2.name", read_only=True)

    class Meta:
        model = Session
        fields = ["session_id", "date", "time", "professor_1_name", "professor_2_name"]

<<<<<<< HEAD
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
=======

class FormulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formula
        fields = ["formula"]
>>>>>>> d968a2574d3a78eb777d428b9fce10c5cae2e480
