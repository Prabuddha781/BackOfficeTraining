from django import forms
from .models import Overview, SecondPage, DebitEntry, CreditEntry

class DateInput(forms.Form):
    input_type = 'date'

class TransactionsForms(forms.Form):
    transactionCode = forms.CharField(max_length=4, required=True, label=False)

class SecondPageForm(forms.ModelForm):
    class Meta:
        model = SecondPage
        fields = ['docDate', 'docType', 'companyCode', 'postDate', 'period', 'currency', 'transDate', 'reference', 'docHeader', 'partnerBArea', 'pstKey', 'accountBottom']
        widgets = {
            'docDate': forms.DateInput(attrs={'id':'docDateInput', 'label': "Document Date"}),
            'docType': forms.TextInput(attrs={'id':'docTypeInput', 'label':"Document Type"}),
            'companyCode': forms.TextInput(attrs={'id': 'companyCodeInput', 'label':"Company Code"}),
            'postDate': forms.DateInput(attrs={'id':'postDateInput', 'label':"Posting Date"}),
            'period': forms.TextInput(attrs={'id':'periodInput', 'label':'period'}),
            'currency': forms.TextInput(attrs={'id': 'currencyInput', 'required':'True', 'label':'Currency'}),
            'transDate': forms.DateInput(attrs={'id':'transDateInput', 'label': "Translatn Date"}),
            'reference': forms.TextInput(attrs={'id': 'referenceInput', 'required':'True', 'label':'Reference'}), 
            'docHeader': forms.TextInput(attrs={'id': 'docHeaderInput', 'label':'Document Header'}),
            'partnerBArea': forms.TextInput(attrs={'id': 'partnerBusAreaInput', 'disabled': 'DISABLED', 'label':'Partner Business Area'}),
            'pstKey': forms.TextInput(attrs={'id': 'pstKey', 'label':"Posting Key"}),
            'accountBottom': forms.TextInput(attrs={'id': 'accountBottom', 'label':"Account"})
        }



class DebitEntryForm(forms.ModelForm):
    class Meta:
        model = DebitEntry
        fields = ['amount', 'calculateTax', 'busArea', 'paytTerms', 'percent1', 'bLineDate', 'discAmt', 'discBase', 'invoiceRef1', 'pmtBlock', 'pmtMethod', 'assignmentPg3', 'textPg3', 'pstKey', 'accountBottom']
        widgets = {
            'amount': forms.TextInput(attrs={'id':'amountPg3Input', 'label': "Amount"}),
            'calculateTax': forms.CheckboxInput(attrs={'id': 'calculateTaxInput', 'label':'Calculate Tax'}),
            'busArea': forms.TextInput(attrs={'id':'busAreaInput', 'label':"Bus. Area"}),
            'paytTerms': forms.TextInput(attrs={'id': 'paytTermsInput', 'label':"Payt Terms", "class": "text-muted"}),
            'percent1': forms.TextInput(attrs={'id':'percent1Input', 'label':"Days/Percent", "class": "text-muted"}),
            'bLineDate': forms.TextInput(attrs={'id':'bLineDateInput', 'label':'Bline Date'}),
            'discAmt': forms.TextInput(attrs={'id': 'discAmtInput', 'label':'Disc. Amount'}),
            'discBase': forms.TextInput(attrs={'id': 'discBaseInput', 'label':'Disc. Base'}), 
            'invoiceRef1': forms.TextInput(attrs={'id': 'invoiceRefInput1', 'label':'Invoice ref.'}),
            'pmtBlock': forms.TextInput(attrs={'id': 'pmtBlockInput', 'label':'Pmnt Block'}),
            'pmtMethod': forms.TextInput(attrs={'id': 'pmtMethodInput', 'label':"Pmnt Method"}),
            'assignmentPg3': forms.TextInput(attrs={'id': 'assignmentPg3Input', 'label':"Assignment"}),
            'textPg3': forms.TextInput(attrs={'id': 'textPg3Input', 'label':"Text"}),
            'pstKey': forms.TextInput(attrs={'id': 'pstKey', 'label':"Posting Key"}),
            'accountBottom': forms.TextInput(attrs={'id': 'accountBottom', 'label':"Account"})
        }

class CreditEntryForm(forms.ModelForm):
    class Meta:
        model = CreditEntry
        fields = ['amount', 'taxCode', 'taxJur', 'busArea', 'trdgPartBA', 'costCenter', 'order', 'profitCenter', 'wbsElement', 'network1', 'purchasingDoc1', 'quantity1', 'assignment', 'text', 'pstKey', 'accountBottom']
        widgets = {
            'amount': forms.TextInput(attrs={'id': 'amountInput', 'label':"Amount"}),
            'taxCode': forms.TextInput(attrs={'id': 'taxCodeInput', 'label':"Tax Code"}),
            'taxJur': forms.TextInput(attrs={'id': 'taxJurInput', 'label':"Tax Jur."}),
            'busArea': forms.TextInput(attrs={'id': 'busAreaInput', 'label':"Business Area"}),
            'profitCenter': forms.TextInput(attrs={'id': 'profitCenterInput', 'label':"ProfitCenter"}),
            'costCenter': forms.TextInput(attrs={'id': 'costCenterInput', 'label':"Cost Center"}),
            'trdgPartBA': forms.TextInput(attrs={'id': 'trdgPartBAInput', 'label':"Trdg part. BA"}),
            'order': forms.TextInput(attrs={'id': 'orderInput', 'label':"Order"}),
            'wbsElement': forms.TextInput(attrs={'id': 'wbsElementInput', 'label':"WBS ELement"}),
            'network1': forms.TextInput(attrs={'id': 'networkInput1', 'label':"Network"}),
            'purchasingDoc1': forms.TextInput(attrs={'id': 'purchasingDocInput1', 'label':"Purchasing Doc."}),
            'quantity1': forms.TextInput(attrs={'id': 'quantityInput1', 'label':"Quantity"}),
            'assignment': forms.TextInput(attrs={'id': 'assignmentInput', 'label':"Assignment"}),
            'text': forms.TextInput(attrs={'id': 'textInput', 'label':"Text"}),
            'pstKey': forms.TextInput(attrs={'id': 'pstKey', 'label':"Posting Key"}),
            'accountBottom': forms.TextInput(attrs={'id': 'accountBottom', 'label':"Account"})
        }

lastSecondPage = SecondPage.objects.last()
lastCreditEntry = CreditEntry.objects.last()

class OverviewForm(forms.ModelForm):
    class Meta:
        model = Overview
        fields = ['reference', 'trdgPartBA', 'docHeader']
        widgets = {
            'reference': forms.TextInput(attrs={'id': 'referenceInput', 'label':"Reference", 'value': lastSecondPage.reference.upper()}),
            'trdgPartBA': forms.TextInput(attrs={'id': 'tradingPartInput', 'label':"Trading Part BA", 'value': lastCreditEntry.trdgPartBA }),
            'docHeader': forms.TextInput(attrs={'id': 'docHeaderTextInput', 'label':"Document Header Text", 'value': lastSecondPage.docHeader })
        }
