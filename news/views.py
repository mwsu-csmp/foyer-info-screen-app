from django.shortcuts import render, redirect
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
    with open('news/static/newsData.json') as fin:
        slidelist = json.loads(fin.read())

        print(slidelist[-1])
        for slide in slidelist:
            print(slide['id'])
            if slide['id'] == len(slidelist):
                id = 1
                return redirect('slideView', id)
        # We know we are not at the last element, so we update id then loop again
        # this time accessing the next slide from our list without using an iterator
        id += 1
        for slide in slidelist:
            if slide['id'] == id:
                return redirect('slideView', id)
    return HttpResponseNotFound('<h1>slide ' + str(id) + ' not found</h1>')