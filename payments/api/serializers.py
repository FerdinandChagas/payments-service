from rest_framework.serializers import ModelSerializer

from payments.models import CreditPayment, BankTransferPayment, MobilePayment, DebitPayment

class CreditPaymentSerializer(ModelSerializer):
    class Meta:
        model = CreditPayment
        fields = '__all__'

class BankTransferPaymentSerializer(ModelSerializer):
    class Meta:
        model = BankTransferPayment
        fields = '__all__'

class MobilePaymentSerializer(ModelSerializer):
    class Meta:
        model = MobilePayment
        fields = '__all__'

class DebitPaymentSerializer(ModelSerializer):
    class Meta:
        model = DebitPayment
        fields = '__all__'