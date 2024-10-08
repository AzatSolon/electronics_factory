from django.urls import path
from rest_framework.routers import DefaultRouter

from trading_network.apps import TradingNetworkConfig
from trading_network.views import (
    ContactViewSet,
    NetworkCreateAPIView,
    NetworkDestroyAPIView,
    NetworkListAPIView,
    NetworkRetrieveAPIView,
    NetworkUpdateAPIView,
    ProductViewSet,
)

app_name = TradingNetworkConfig.name

contact_router = DefaultRouter()
contact_router.register(r"contact", ContactViewSet, basename="contact")

product_router = DefaultRouter()
product_router.register(r"product", ProductViewSet, basename="product")

urlpatterns = (
    [
        path("", NetworkListAPIView.as_view(), name="network_list"),
        path("create/", NetworkCreateAPIView.as_view(), name="network_create"),
        path("<int:pk>/", NetworkRetrieveAPIView.as_view(), name="network_retrieve"),
        path("<int:pk>/update/", NetworkUpdateAPIView.as_view(), name="network_update"),
        path(
            "<int:pk>/delete/", NetworkDestroyAPIView.as_view(), name="network_delete"
        ),
    ]
    + contact_router.urls
    + product_router.urls
)
