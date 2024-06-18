from django.shortcuts import render

from rest_framework import viewsets
from .models import Comment
from .permissions import IsOwerOrReader
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwerOrReader]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
