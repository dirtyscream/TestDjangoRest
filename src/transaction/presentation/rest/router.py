from transaction.presentation.rest.api import TransactionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("transactions", TransactionViewSet, basename="transactions")

urlpatterns = router.urls
