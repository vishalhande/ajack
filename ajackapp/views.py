from django.shortcuts import render
from .models import Content
from .serilizer import ContentSerilizer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,

# Create your views here.
class ContentView(ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerilizer
    permission_classes = [IsAuthenticated]
