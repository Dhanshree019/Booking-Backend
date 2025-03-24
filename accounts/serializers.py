from rest_framework.serializers import ModelSerializer, SerializerMethodField

from accounts.models import CustomUser


# CustomUser model serializer
class CustomUserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        exclude = ('password', 'is_active', 'is_staff', 'is_superuser', 'user_permissions', 'groups')


