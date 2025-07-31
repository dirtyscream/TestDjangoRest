from django.contrib import admin
from django.urls import include, path
from account.presentation.rest.router import urlpatterns as account_router
from transaction.presentation.rest.router import urlpatterns as transaction_router
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(account_router)),
    path('api/', include(transaction_router)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
