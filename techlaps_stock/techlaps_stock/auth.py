from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
import random
import string
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenObtainSerializer


class TokenSerializer(TokenObtainSerializer):
    def validate(self, attrs):

        data = super(TokenSerializer, self).validate(attrs)
        token, created = Token.objects.get_or_create(user=self.user)

        data.update({'user': self.user.username})
        data.update({'id': self.user.id})
        data.update({'first_name': self.user.first_name})
        data.update({'last_name': self.user.last_name})
        data.update({'is_staff': self.user.is_staff})
        data.update({'email': self.user.email})
        data.update({'token': token.key})
        # data.update({'created': created})

        return data


class TokenView(TokenViewBase):
    serializer_class = TokenSerializer


# @api_view(['POST'])
# def forgot_pasword(request):

#     if User.objects.filter(username=request.data["email"]).exists():
#         new_password = ''.join(random.choice(string.ascii_uppercase + string.digits)
#                                for _ in range(10))

#         print(User.objects.get(
#             username=request.data["email"]).set_password(new_password))

#         send_mail(request.data["email"], "Şifre Yenileme",
#                   f"Yeni şifreniz : {new_password}")
#         return success("New password has been sent to email adress.")
#     else:

#         return error("User does not exist!")
