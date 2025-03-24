from django.db import transaction

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
import rest_framework.status as HttpStatusCode

from accounts.models import CustomUser
from accounts.serializers import CustomUserSerializer


class LoginView(APIView):

    permission_classes = []
    authentication_classes = []

    @transaction.atomic
    def post(self, request):

        rd = request.data
        print("rd :: ", rd)

        user = CustomUser.objects.filter(phone_number=rd['phone_number']).first()
        if user == None:
            user = CustomUser.objects.create(phone_number=rd['phone_number'], full_name=rd['full_name'])

        token = RefreshToken.for_user(user)
        data = CustomUserSerializer(user).data

        return Response(
            {"success": True, "message": "User Login Success!", "data": data,
             "authToken": {
                'type': 'Bearer',
                'access': str(token.access_token),
                'refresh': str(token),
            }},
            status=HttpStatusCode.HTTP_400_BAD_REQUEST
        )












