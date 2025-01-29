from rest_framework import serializers
from ...models import User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions



class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=255, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'password', 'password1']
        # fields = '__all__' 

    def validate(self, value):
        if value.get("password") != value.get("password1"):
            raise serializers.ValidationError({"detail":"passwords doesn't match"}) 
        try:
            validate_password(value.get('password'))

        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"password":list(e.messages)})
        return super().validate(value)

    def create(self, validated_data):
        validated_data.pop('password1',None) 
        return User.objects.create_user(**validated_data)   