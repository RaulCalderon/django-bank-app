from django.db import models

# Create a Client Model
class Client(models.Model):
    client_name = models.CharField(max_length=100)
    client_mail = models.EmailField(unique=True)

    def __str__(self):
        return self.client_name

# Create an Account Model
class Account(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='accounts')
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.account_number} - {self.client.client_name}"

# Create a Transfer Model
class Transfer(models.Model):
    account_origin = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transfers_sent')
    account_destination = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transfers_obtained')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account_origin} -> {self.account_destination} : ${self.amount}"

















