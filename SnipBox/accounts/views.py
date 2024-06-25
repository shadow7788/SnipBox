from django.contrib.auth import authenticate, login
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.serializers import UserRegisterSerializer


# Create your views here.


class UserRegisterView(APIView):
    serializer_class = UserRegisterSerializer

    # Register user with username and password
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            user.set_password(request.data["password"])
            user.save()
            return Response({"message": "User Created"}, status=status.HTTP_201_CREATED)
        except KeyError:
            return Response({"message": "Required fields missing"}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    def post(self, request):
        try:
            user = authenticate(username=request.data["username"], password=request.data["password"])
            if user is not None:
                login(request, user)
                refresh = RefreshToken.for_user(user)
                return Response(
                    {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),

                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"message": "Invalid credentials"},
                    status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response({"message": "Required fields missing"}, status=status.HTTP_400_BAD_REQUEST)
