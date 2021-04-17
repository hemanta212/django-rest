from rest_framework.routers import SimpleRouter
from .views import PostViewSet, UserViewSet

router = SimpleRouter()
router.register('user', UserViewSet, basename='user')
router.register('', PostViewSet, basename='post')

urlpatterns = router.urls
