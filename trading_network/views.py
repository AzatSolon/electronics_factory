from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from trading_network.models import Contact, Network, Product, Factory
from trading_network.permissions import IsActive
from trading_network.serializers import (
    ContactSerializer,
    NetworkSerializer,
    ProductSerializer,
    FactorySerializer,
)


class FactoryViewSet(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    filter_fields = ["country"]

    def has_object_permission(self, request):
        return request.user.is_staff or request.user.is_superuser


class NetworkCreateAPIView(CreateAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [IsActive]


class NetworkListAPIView(ListAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [IsActive]


class NetworkRetrieveAPIView(RetrieveAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [IsActive]


class NetworkUpdateAPIView(UpdateAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [IsActive]

    def perform_update(self, serializer):
        if "debt_to_supplier" in serializer.validated_data:
            serializer.validated_data.pop("debt_to_supplier")
            raise Exception("В доступе отказано.")
        super().perform_update(serializer)


class NetworkDestroyAPIView(DestroyAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [IsActive]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActive]


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["country"]
    search_fields = ["country"]
    permission_classes = [IsActive]
