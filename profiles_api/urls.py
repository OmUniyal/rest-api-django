from django.urls import path
from profiles_api import views

#imported for view set
from django.urls import include
from rest_framework.routers import DefaultRouter

#Registering router
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSets, base_name = 'hello-viewset')

# registering router for UserProfile view set
router.register('profile', views.UserProfileViewSet)

#registering router for User Profile Feed item
router.register('feed',views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view()),
    path('login/',views.UserLoginApiView.as_view()),  # added to connect UserLoginApiView class 
    path('', include(router.urls))
]