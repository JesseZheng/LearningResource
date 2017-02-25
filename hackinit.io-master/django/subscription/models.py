from django.db import models

class SubscriptionEmailAddress(models.Model):
    email_address = models.EmailField(unique=True)

class SubscriptionCellphoneNumber(models.Model):
    cellphone_number = models.CharField(max_length=20, unique=True)
