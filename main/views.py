from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import DebitEntryForm, TransactionsForms, SecondPageForm, CreditEntryForm, OverviewForm
from .models import CreditEntry, SecondPage, DebitEntry, Overview
from random import randrange
from django.contrib import messages

companyIdDict = {'2909': ['Verizon Wireless', '141 Industrial Parkway', 'Branchburg', '1720010'], '1644': ['ATT', 'New York City', 'New York', '70817081'], '60':['Pierre', '23 WestVille Avenue','Caldwell', '70817081']}

lastSecondPage = SecondPage.objects.last() 
lastDebitEntry = DebitEntry.objects.last()
lastCreditEntry = CreditEntry.objects.last()

carrierNumber = lastSecondPage.accountBottom
fiscal = lastSecondPage.postDate.year
compCode = lastSecondPage.companyCode
currency = lastSecondPage.currency
glAcc = lastDebitEntry.accountBottom
differenceDebitCredit = lastDebitEntry.amount - lastCreditEntry.amount


try:
    carrierDetails = companyIdDict[carrierNumber]
except KeyError:
    carrierDetails = "carrier not found for Account Number  {accNum} that was entered in last page. Go back to correct it.".format(accNum=carrierNumber)
companyInfo = [carrierNumber, carrierDetails]

def docNumGen():
    return '1600000' + str(randrange(0,999))

def landPage(request):
    if request.method == 'POST':
        form = TransactionsForms(request.POST)
        if form.is_valid():
            transactionCode = form.cleaned_data['transactionCode']
            print(transactionCode)
            if transactionCode.lower() == 'vf04':
                return redirect(secondPage)
    else:
        form = TransactionsForms()
    return render(request, "main/landingPage.html", {'form': form})

def secondPage(request):
    try:
        if request.session['docNum']:
            documentNumber = request.session['docNum']
            messages.add_message(request, 20, 'Document Number is {docNum}'.format(docNum=documentNumber))
            print(request.session.get_expiry_age())
            del request.session['docNum']
    except KeyError:
        pass
    if request.method == 'POST':
        form = SecondPageForm(request.POST)
        if form.is_valid():
            secondPageData = form.save()
            return redirect(debitEntry)
    else: 
        form = SecondPageForm()
    return render(request, 'main/secondPage.html', {'form': form})

def debitEntry(request):
    if request.method == 'POST':
        form = DebitEntryForm(request.POST)
        if form.is_valid():
            debitEntryData = form.save()
            return redirect(creditEntry)
    else: 
        form = DebitEntryForm()
    return render(request, 'main/debitEntry.html', {'form': form, 'companyInfo': companyInfo, 'lastSecondPage': lastSecondPage})

def creditEntry(request):
    listForHtml = [compCode, glAcc, currency]
    if request.method == 'POST':
        form = CreditEntryForm(request.POST)
        print(listForHtml[2])
        if form.is_valid():
            creditEntrydata = form.save()
            return redirect(overview)
    else: 
        form = CreditEntryForm()
        print(listForHtml[2])
    return render(request, 'main/creditEntry.html', {'listForHtml': listForHtml, 'form': form})

def overview(request):
    if request.method == 'POST':
        form = OverviewForm(request.POST)
        if form.is_valid():
            overviewData = form.save()
            cleanedForm = form.cleaned_data
            lastSecondPage.reference = cleanedForm['reference']
            print(lastSecondPage.reference)
            lastCreditEntry.trdgPartBA = cleanedForm['trdgPartBA']
            lastSecondPage.docHeader = cleanedForm['docHeader']
            lastSecondPage.save()
            lastDebitEntry.save()
            request.session['docNum'] = docNumGen()
            return redirect(secondPage)
    else: 
        form = OverviewForm()
    return render(request, 'main/overview.html', {'lastSecondPage': lastSecondPage, 'lastDebitEntry': lastDebitEntry, 'lastCreditEntry': lastCreditEntry, 'fiscal': fiscal, 'form': form, 'companyInfo': companyInfo, 'differenceDebitCredit': differenceDebitCredit})

def docHeaderPage(request):
    return render(request, 'main/docHeaderPage.html')

def fastDataEntry(request):
    return render(request, 'main/fastDataEntry.html')
