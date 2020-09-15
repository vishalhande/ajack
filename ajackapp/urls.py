from django.urls import path, include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('api/v1',views.ContentView)

urlpatterns = [
    path('', include(router.urls))
]