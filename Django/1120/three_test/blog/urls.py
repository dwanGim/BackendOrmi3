from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoticeViewSet, BlogPostViewSet

router = DefaultRouter()
router.register(r'notice', NoticeViewSet)
router.register(r'blog', BlogPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
