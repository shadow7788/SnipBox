from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from snippet.models import Tag, Snippet
from snippet.serializers import SnippetSerializer


# Create your views here.

class SnippetListView(APIView):
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        snippet_data = make_data(request)
        snippet_serializer = self.serializer_class(data=snippet_data)
        if snippet_serializer.is_valid():
            snippet = snippet_serializer.save()
            return Response(self.serializer_class(snippet).data, status=status.HTTP_201_CREATED)

        return Response(snippet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def make_data(request):
    tags_data = request.data.pop("tags", [])
    snippet_data = request.data
    snippet_data["user"] = request.user.id
    snippet_data["tags"] = []
    for tag_title in tags_data:
        tag, created = Tag.objects.get_or_create(title=tag_title)
        snippet_data["tags"].append(tag.id)
    return snippet_data
