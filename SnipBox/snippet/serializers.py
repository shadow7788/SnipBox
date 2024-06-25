from django.urls import reverse
from rest_framework import serializers

from snippet.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'note', 'created_at', 'updated_at', 'user', 'tags']

