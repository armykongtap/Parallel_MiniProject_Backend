from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import LoginViewSet, GroupViewSet, JoinViewSet, GetUserViewSet, DeleteGroupViewSet

router = DefaultRouter()
router.register(r'login', LoginViewSet, basename='login')
router.register(r'group', GroupViewSet, basename='group')
router.register(r'join', JoinViewSet, basename='join_group')
router.register(r'getuser', GetUserViewSet, basename='get_users_group')
router.register(r'delete', DeleteGroupViewSet, basename='delete_group')

urlpatterns = router.urls