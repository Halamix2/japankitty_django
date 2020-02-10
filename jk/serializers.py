from rest_framework import serializers
from .models import User
from django.utils.translation import gettext_lazy as _

class RegisterSerializer(serializers.ModelSerializer):
    #confirm_password = serializers.CharField()
    email = serializers.EmailField()

    def validate(self, data):
        try:
            user = User.objects.filter(username=data.get('username'))
            if len(user) > 0:
                raise serializers.ValidationError(_("Username already exists"))
        except User.DoesNotExist:
            pass
        if not data.get('email'):
            raise serializers.ValidationError(_("Empty email"))

        if not data.get('password'):# or not data.get('confirm_password'):
            raise serializers.ValidationError(_("Empty password"))

        #if data.get('password') != data.get('confirm_password'):
        #    raise serializers.ValidationError(_("Password mismatch"))

        return data
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('username', 'email', 'password')#, 'confirm_password')
        #extra_kwargs = {'confirm_password': {'read_only': True}}