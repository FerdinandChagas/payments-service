from rest_framework.viewsets import ModelViewSet

from payments.models import CreditPayment, BankTransferPayment, MobilePayment, DebitPayment
from payments.api.serializers import CreditPaymentSerializer, BankTransferPaymentSerializer, MobilePaymentSerializer, DebitPaymentSerializer

class CreditPaymentViewSet(ModelViewSet):
    queryset = CreditPayment.objects.all()
    serializer_class = CreditPaymentSerializer

class BankTransferPaymentViewSet(ModelViewSet):
    queryset = BankTransferPayment.objects.all()
    serializer_class = BankTransferPaymentSerializer

class MobilePaymentViewSet(ModelViewSet):
    queryset = MobilePayment.objects.all()
    serializer_class = MobilePaymentSerializer

class DebitPaymentViewSet(ModelViewSet):
    queryset = DebitPayment.objects.all()
    serializer_class = DebitPaymentSerializer

