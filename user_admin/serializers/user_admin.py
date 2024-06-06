from rest_framework import serializers
from ..models.user_admin import UserAdminModel

class UserAdminSerializer(serializers.ModelSerializer):
    class Meta: 
        model = UserAdminModel
        fields =  '__all__'