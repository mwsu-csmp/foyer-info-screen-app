from django.shortcuts import render
from django.http import HttpResponse
import json
import jsonlines
import qrcode

#This function will generate a qr code and save it as an image. Basic fuction for now redirects to CSMP dep
#  homepage until urls are established for each slide
def qrGen(request):
    img = qrcode.make('http://google.com')
    response = HttpResponse(content_type='image/jpg')
    img.save(response, "JPEG")
    return response


# Create your views here.
def index(request):

    print("Passed qrGen()")
    with jsonlines.open('news/static/newsData.jsonl') as reader:
        for obj in reader:
            if obj:
                print("we got json")
                return render(request, "news/newsTitle.jinja", obj)
            else:
                print("we got NO json")
                return render(request, "news/newsTitle.jinja")


