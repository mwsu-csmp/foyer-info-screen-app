from django.shortcuts import render
from django.http import HttpResponse
import jsonlines
import json
import qrcode
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

#  This function will generate a qr code and save it as an image. Basic fuction for now redirects to CSMP dep
#  homepage until urls are established for each slide
def qrGen(request):

    img = qrcode.make('http://google.com')
    response = HttpResponse(content_type='image/jpg')
    img.save(response, "JPEG")
    return response


def index(request):

    print("In basic index function")
    return render(request, "news/index.jinja")


def slideView(request, id):
    with open('news/static/newsData.json') as fin:
        slidelist = json.loads(fin.read())
        for slide in slidelist:
            if slide['id'] == id:
                return render(request, "news/"+slide['template']+".jinja", slide)
    return HttpResponseNotFound('<h1>slide '+id+' not found</h1>')

def advanceSlideView(request, id):
    pass
    # TODO: load list of slides, find which slide id is at, go to next slide (or wrap around to first slide)
    # use a redirect rather than rendering it

def newsArticle(request):
    print("In News Title function")
    with jsonlines.open('news/static/newsData.jsonl') as reader:
        for obj in reader:
            if obj:
                print("we got json")
                return render(request, "news/newsTitle.jinja", obj)
            else:
                print("we got NO json")
                return render(request, "news/newsTitle.jinja")