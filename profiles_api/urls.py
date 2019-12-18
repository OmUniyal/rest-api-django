from django.urls import path
from profiles_api import views

#imported for view set
from django.urls import include
from rest_framework.routers import DefaultRouter

#Registering router
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSets, base_name = 'hello-viewset')

urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view()),
    path('', include(router.urls))
]