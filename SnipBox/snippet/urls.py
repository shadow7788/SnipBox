from django.urls import path
from .views import SnippetListView

urlpatterns = [
    path('snippet/', SnippetListView.as_view(), name='snippets'),
]
