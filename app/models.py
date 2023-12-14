from django.db import models

class OptionChain(models.Model):
    id = models.AutoField(primary_key=True)
    OI_calls = models.IntegerField()
    CHNG_IN_OI_calls = models.DecimalField(max_digits=10, decimal_places=2)
    VOLUME_calls = models.IntegerField()
    IV_calls = models.DecimalField(max_digits=10, decimal_places=2)
    LTP_calls = models.DecimalField(max_digits=10, decimal_places=2)
    CHNG_calls = models.DecimalField(max_digits=10, decimal_places=2)
    BID_QTY_calls = models.IntegerField()
    BID_calls = models.DecimalField(max_digits=10, decimal_places=2)
    ASK_calls = models.DecimalField(max_digits=10, decimal_places=2)
    ASK_QTY_calls = models.IntegerField()
    STRIKE = models.DecimalField(max_digits=10, decimal_places=2)
    BID_QTY_puts = models.IntegerField()
    BID_puts = models.DecimalField(max_digits=10, decimal_places=2)
    ASK_puts = models.DecimalField(max_digits=10, decimal_places=2)
    ASK_QTY_puts = models.IntegerField()
    CHNG_puts = models.DecimalField(max_digits=10, decimal_places=2)
    LTP_puts = models.DecimalField(max_digits=10, decimal_places=2)
    IV_puts = models.DecimalField(max_digits=10, decimal_places=2)
    VOLUME_puts = models.IntegerField()
    CHNG_IN_OI_puts = models.DecimalField(max_digits=10, decimal_places=2)
    OI_puts = models.IntegerField()

    def __str__(self):
        return f"OptionChain ID: {self.id}"
