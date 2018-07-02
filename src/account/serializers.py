#from django.contrib.auth.models import User, Group

from rest_framework import serializers
from account.models import Account, Employee
from django.contrib.auth.models import User

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = ('id', 'name', 'account')
        
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data): # **kwargs
       user = super(RegistrationSerializer, self).create(validated_data)
       user.set_password(validated_data['password'])
       user.save()
       return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('userprofile', {})

        instance = super(UserSerializer, self).update(instance, validated_data)

        if profile_data:
            profile.save()
        return instance


# class UserSerializer(serializers.ModelSerializer):
#     profile = ProfileSerializer()

#     def update(self, instance, validated_data):
#         '''
#         Override update method because we need to update
#         nested serializer for profile
#         '''
#         if validated_data.get('profile'):
#             profile_data = validated_data.get('profile')
#             profile_serializer = ProfileSerializer(data=profile_data)

#             if profile_serializer.is_valid():
#                 profile = profile_serializer.update(instance=instance.profile)
#                 validated_data['profile'] = profile

#         return super(UserSerializer, self).update(instance, validated_data)

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'first_name', 'last_name', 'profile')
