from django.db import models

class Bond(models.Model):
    isin = models.CharField(max_length = 12)
    size = models.IntegerField()
    currency = models.CharField(max_length = 3)
    maturity = models.DateField(auto_now = False)
    lei = models.CharField(max_length = 20)
    legal_name = models.CharField(max_length = 100, blank = True)

    def __str__(self):
        return "Legal name: " + legal_name + ", Currency: " + currency
