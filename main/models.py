from django.db import models
from datetime import date

from django.db.models.deletion import CASCADE

class SecondPage(models.Model):
    today = date.today()
    d1 = today.strftime("%m/%d/%Y")
    docDate = models.DateField()
    docType = models.CharField(blank=False, max_length=4, default="?")
    companyCode = models.CharField(default="?", max_length=4, blank=True)
    postDate = models.DateField(blank=False, default=d1)
    period = models.IntegerField(blank=False, default="?")
    currency = models.CharField(default="?", max_length=3)
    transDate = models.DateField()
    reference = models.CharField(max_length= 100)
    docHeader = models.CharField(max_length= 100)
    partnerBArea = models.CharField(blank=True, max_length= 100)
    pstKey = models.CharField(blank=False, max_length=2)
    accountBottom = models.CharField(blank=False, max_length= 100)

    def __str__(self):
        return self.reference

class DebitEntry(models.Model):
    amount = models.IntegerField(blank=False)
    calculateTax = models.BooleanField(default=True)
    busArea = models.CharField(max_length=4)
    paytTerms = models.CharField(default="AR30", max_length=4)
    percent1 = models.IntegerField(blank=False, default=30)
    bLineDate = models.DateField(default=SecondPage.d1)
    discAmt = models.IntegerField(blank=True, null=True)
    discBase = models.IntegerField(blank=True, null=True)
    invoiceRef1 = models.CharField(blank=True, max_length=100)
    pmtBlock = models.CharField(blank=True, max_length=2)
    pmtMethod = models.CharField(blank=True, max_length=2)
    assignmentPg3 = models.CharField(blank=False, max_length=200)
    textPg3 = models.CharField(blank=False, max_length=200)
    pstKey = models.CharField(blank=False, max_length=2)
    accountBottom = models.CharField(blank=False, max_length= 100)

class CreditEntry(models.Model):
    amount = models.IntegerField(blank=False)
    taxCode = models.CharField(max_length=4, blank=True)
    taxJur = models.CharField(max_length=10, blank=True)
    busArea = models.CharField(blank=False, max_length=10)
    trdgPartBA = models.CharField(blank=True, max_length=4)
    costCenter = models.CharField(blank=True, max_length=10)
    order = models.CharField(blank=True, max_length=10)
    profitCenter = models.CharField(blank=True, max_length=10)
    wbsElement = models.CharField(blank=True, max_length=20)
    network1 = models.CharField(blank=True, max_length=10)
    purchasingDoc1 = models.CharField(blank=True, max_length=10)
    quantity1 = models.CharField(blank=True, max_length=5)
    assignment = models.CharField(blank=False, max_length=200)
    text = models.CharField(blank=False, max_length=200)
    pstKey = models.CharField(blank=True, max_length=2)
    accountBottom = models.CharField(blank=True, max_length= 100)

class Overview(models.Model):
    reference = models.CharField(max_length= 100, blank=False)
    trdgPartBA = models.CharField(blank=True, max_length=4)
    docHeader = models.CharField(max_length= 100, blank=False)
