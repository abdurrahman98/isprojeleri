from django.shortcuts import render
import requests as req
from bs4 import BeautifulSoup
from openpyxl import workbook
from isproje.web_kod import ürünBilgileri

# Create your views here.
def veri(request):
    # https://www.hepsiburada.com/lenovo-ideapad-c340-14iml-intel-core-i3-10110u-4gb-128gb-ssd-windows-10-home-14-fhd-tasinabilir-bilgisayar-81tk00c3tx-p-HBV00000TBIHT

    if request.method == "POST":
        if request.POST["web"]!= None:
            ürünBilgileri.urunBilgileri(request)
        if request.POST["arama"]!=None:
            ürünBilgileri.aramaBilgileri(request)


# soup = BeautifulSoup(request.POST["web"],"html.parser")


    return render(request, "../static/../templates/index.html")
