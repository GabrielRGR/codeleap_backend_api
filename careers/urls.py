from rest_framework.routers import DefaultRouter
from .views import PostViewSet, LikesViewSet
from django.urls import path, include


router = DefaultRouter()
likes_router = DefaultRouter()

router.register(r'careers', PostViewSet, basename='career')
router.register(r'likes',LikesViewSet, basename='likes' )

urlpatterns = [
    path('', include(router.urls)),
]