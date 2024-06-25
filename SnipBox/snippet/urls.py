from django.urls import path
from .views import SnippetListView, SnippetDetailView

urlpatterns = [
    path('snippet/', SnippetListView.as_view(), name='snippets'),
    path('snippet/<int:id>/', SnippetDetailView.as_view(), name="snippet-detail"),
]
