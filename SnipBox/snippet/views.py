from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from snippet.models import Tag, Snippet
from snippet.serializers import SnippetSerializer, SnippetListSerializer


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

    def get(self, request):
        snippet_list = Snippet.objects.filter(user=request.user, status=1)
        print(snippet_list)
        data = SnippetListSerializer(snippet_list, context={'request': request}, many=True).data
        return Response({
            "count": len(data),
            "data": data
        })


class SnippetDetailView(APIView):
    def get(self, request, id):
        try:
            snippet = Snippet.objects.get(id=id, user=request.user, status=1)
            return Response(SnippetSerializer(snippet).data)
        except ObjectDoesNotExist:
            return Response({"message": "Snippet Not Found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            snippet = Snippet.objects.get(id=id, user=request.user, status=1)
            snippet_data = make_data(request)
            serializer = SnippetSerializer(snippet, data=snippet_data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({"message": "Snippet Not Found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            snippet = Snippet.objects.get(id=id, user=request.user, status=1)
            snippet.status = 0
            snippet.save()
            return HttpResponseRedirect(reverse('snippets'))
        except ObjectDoesNotExist:
            return Response({"message": "Snippet Not Found"}, status=status.HTTP_404_NOT_FOUND)


def make_data(request):
    tags_data = request.data.pop("tags", [])
    snippet_data = request.data
    snippet_data["user"] = request.user.id
    snippet_data["tags"] = []
    for tag_title in tags_data:
        tag, created = Tag.objects.get_or_create(title=tag_title)
        snippet_data["tags"].append(tag.id)
    return snippet_data
