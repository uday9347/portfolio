from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'mainapp/folio.html')

def eda(request):
    return render(request,'mainapp/PlayStore_EDA.html')

def ipl(request):
    return render(request,'mainapp/IPL_analysis.html')
