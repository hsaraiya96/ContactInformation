from rest_framework import routers

from account.views import UserViewSet, UserContactViewSet

router = routers.SimpleRouter()
router.register(r'user', UserViewSet)
router.register(r'user_contact', UserContactViewSet)

urlpatterns = router.urls
