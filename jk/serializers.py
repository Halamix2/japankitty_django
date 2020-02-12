from rest_framework import serializers
from .models import User, Progress, Course, Text
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

class EditUserSerializer(serializers.ModelSerializer):
    new_username = serializers.CharField(required=False)
    new_email = serializers.EmailField(required=False)
    new_password = serializers.CharField(required=False)

    new_sex = serializers.CharField(required=False)
    new_surname = serializers.CharField(required=False)
    new_birthday = serializers.DateField(required=False)


    def validate(self, data):
        try:
            user = User.objects.filter(username=data.get('new_username'))
            if len(user) > 0:
                raise serializers.ValidationError(_("Username already exists"))
        except User.DoesNotExist:
            pass
        return data

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'new_password':
                instance.set_password(value)
            elif attr == 'new_name':
                setattr(instance, 'name', value)
            elif attr == 'new_email':
                setattr(instance, 'email', value)
            elif attr == 'new_sex':
                setattr(instance, 'sex', value)
            elif attr == 'new_surname':
                setattr(instance, 'surname', value)
            elif attr == 'new_birthday':
                setattr(instance, 'birthday', value)
        instance.save()
        return instance
    class Meta:
        model = User
        fields = ('new_username', 'new_email', 'new_password', 'new_sex', 'new_surname', 'new_birthday')


class EditUserSerializer(serializers.ModelSerializer):
    new_name = serializers.CharField(required=False)
    new_email = serializers.EmailField(required=False)
    new_password = serializers.CharField(required=False)

    new_sex = serializers.CharField(required=False)
    new_surname = serializers.CharField(required=False)
    new_birthday = serializers.DateField(required=False)

    def validate(self, data):
        try:
            user = User.objects.filter(username=data.get('new_username'))
            if len(user) > 0:
                raise serializers.ValidationError(_("Username already exists"))
        except User.DoesNotExist:
            raise serializers.ValidationError(_('User doesn\'t exist'))
        return data

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'new_password':
                instance.set_password(value)
            elif attr == 'new_name':
                setattr(instance, 'username', value)
            elif attr == 'new_email':
                setattr(instance, 'email', value)
            elif attr == 'new_sex':
                setattr(instance, 'sex', value)
            elif attr == 'new_surname':
                setattr(instance, 'surname', value)
            elif attr == 'new_birthday':
                setattr(instance, 'birthday', value)
        instance.save()
        return instance
    
    class Meta:
        model = User
        fields = ('new_name', 'new_email', 'new_password', 'new_sex', 'new_surname', 'new_birthday')

class ProgressSerializer(serializers.ModelSerializer):
    game = serializers.IntegerField()
    score = serializers.IntegerField()
    max_points = serializers.IntegerField()

    def validate(self, data):
        return data

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        user = validated_data.pop('user', None)

        setattr(instance, 'user', user)

        game = validated_data.pop('game', None)
        setattr(instance, 'game', game)

        category = validated_data.pop('category', None)
        setattr(instance, 'category', category)

        score = validated_data.pop('score', None)
        setattr(instance, 'score', score)

        max_points = validated_data.pop('max_points', None)
        setattr(instance, 'max_points', max_points)

        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = Progress
        fields = ('user', 'game', 'category', 'score', 'max_points')

class TextSerializer(serializers.ModelSerializer):
    offerDescription = serializers.CharField()
    offerOption1 = serializers.CharField()
    offerOption2 = serializers.CharField()
    offerOption3 = serializers.CharField()
    contactDescription = serializers.CharField()
    aboutCourse = serializers.CharField()

    def validate(self, data):
        return data
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr != 'id':
                setattr(instance, attr, value)
        instance.save()
        return instance
    
    class Meta:
        model = Text
        fields = ('offerDescription', 'offerOption1', 'offerOption2', 'offerOption3', 'contactDescription', 'aboutCourse')