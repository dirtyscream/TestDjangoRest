from account.presentation.rest.api import AccountViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include, path

router = DefaultRouter()
router.register("accounts", AccountViewSet, basename="accounts")

urlpatterns = router.urls
