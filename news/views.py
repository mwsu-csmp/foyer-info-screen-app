from django.shortcuts import render, redirect
import json
import qrcode
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

# Helper functions to support the functionality in the views

#  This function will generate a qr code and save it as an image. Basic fuction for now redirects to google
#   until webapp has established url on a server
def qrGen(request, id):
    img = qrcode.make('http://127.0.0.1:8000/news/slide/' + str(id))
    response = HttpResponse(content_type='image/jpg')
    img.save(response, "JPEG")
    return response


# These are views that load a webpage
def index(request):

    print("In basic index function")
    return render(request, "news/index.jinja")

def slideView(request, id):
    with open('news/static/newsData.json') as fin:
        slidelist = json.loads(fin.read())
        for slide in slidelist:
            if slide['id'] == id:
                return render(request, "news/"+slide['template']+"Single.jinja", slide)
    return HttpResponseNotFound('<h1>slide '+id+' not found</h1>')

def slideshowView(request, id):
    with open('news/static/newsData.json') as fin:
        slidelist = json.loads(fin.read())
        for slide in slidelist:
            if slide['id'] == id:
                return render(request, "news/"+slide['template']+".jinja", slide)
    return HttpResponseNotFound('<h1>slide '+id+' not found</h1>')

def advanceSlideView(request, id):
    with open('news/static/newsData.json') as fin:
        slidelist = json.loads(fin.read())
        if id == len(slidelist):
            id = 1
            return redirect('slideshowView', id)
        # We know we are not at the last element, so we update id then loop again
        # this time accessing the next slide from our list without using an iterator
        id += 1
        for slide in slidelist:
            if slide['id'] == id:
                return redirect('slideshowView', id)
    return HttpResponseNotFound('<h1>slide ' + str(id) + ' not found</h1>')