from django.db import models

# Create your models here.

class CreditPayment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    card_number = models.CharField(max_length=16)
    cardholder_name = models.CharField(max_length=100)
    expiration_date = models.DateField()
    cvv = models.CharField(max_length=4)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CreditPayment {self.id} - {self.amount}"

class BankTransferPayment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    bank_account_number = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"BankTransferPayment {self.id} - {self.amount}"

class MobilePayment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    mobile_number = models.CharField(max_length=15)
    provider = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"MobilePayment {self.id} - {self.amount}"

class DebitPayment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    card_number = models.CharField(max_length=16)
    cardholder_name = models.CharField(max_length=100)
    expiration_date = models.DateField()
    cvv = models.CharField(max_length=4)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"DebitPayment {self.id} - {self.amount}"
