
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

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


