from rest_framework.serializers import ModelSerializer
from .models import Content,Categories



class CategoriesSerilizer(ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class ContentSerilizer(ModelSerializer):
    catref = CategoriesSerilizer(many = True)
    class Meta:
        model = Content
        fields =('title','body','summary','document','catref')


