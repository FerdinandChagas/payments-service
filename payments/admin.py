from django.contrib import admin

from payments.models import BankTransferPayment, CreditPayment, DebitPayment, MobilePayment

# Register your models here.

admin.site.register(CreditPayment)
admin.site.register(BankTransferPayment)
admin.site.register(MobilePayment)
admin.site.register(DebitPayment)