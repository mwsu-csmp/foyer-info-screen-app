from django.shortcuts import render
from django.http import HttpResponse
import json
import jsonlines
import qrcode

#This function will generate a qr code and save it as an image. Basic fuction for now redirects to CSMP dep
#  homepage until urls are established for each slide
def qrGen():
    siteData = "https://www.missouriwestern.edu/csmp/"

    qrImg = "static/qr.png"
    img = qrcode.make(siteData)
    img.save(qrImg)


# Create your views here.
def index(request):
    
    # Generate the qr code, Commented out because it doesn't work. Nothing is generated
    # qrGen()

    
    print("Passed qrGen()")
    with jsonlines.open('news/static/newsData.jsonl') as reader:
        for obj in reader:
            if obj:
                print("we got json")
                return render(request, "news/newsTitle.jinja", obj)
            else:
                print("we got NO json")
                return render(request, "news/newsTitle.jinja")


