# from rest_framework_simplejwt.serializers import (
#     TokenObtainPairSerializer,
#     TokenRefreshSerializer,
#     TokenVerifySerializer,
# )

# from rest_framework_simplejwt.state import token_backend

# class TokenSerializer(TokenObtainPairSerializer):

#     def validate(self, attrs):
#         data = super().validate(attrs)
#         refresh = self.get_token(self.user)
#         data['refresh'] = str(refresh)
#         data['access'] = str(refresh.access_token)
#         data["username"] = self.user.username
#         data["token_exp"] = refresh.access_token.payload["exp"]
#         return data

#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         return token

# class RefreshTokenSerializer(TokenRefreshSerializer):
#     def validate(self, attrs):
#         data = super(RefreshTokenSerializer, self).validate(attrs)
#         decoded_payload = token_backend.decode(data["access"], verify=True)
#         data["token_exp"] = decoded_payload["exp"]
#         return data
