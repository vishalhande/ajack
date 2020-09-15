from django.shortcuts import render
from .models import Content, Categories
from .serilizer import ContentSerilizer, CategoriesSerilizer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# Create your views here.
class ContentView(ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerilizer
    permission_classes = [IsAuthenticated,IsAdminUser]

class CategoriesSerilizer(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerilizer
    permission_classes = [IsAuthenticated,IsAdminUser]
