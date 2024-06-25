from django.urls import reverse
from rest_framework import serializers

from snippet.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'note', 'created_at', 'updated_at', 'user', 'tags']


class SnippetListSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'note', 'created_at', 'updated_at', 'user', 'tags', 'url']

    def get_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('snippet-detail', args=[obj.id]))
