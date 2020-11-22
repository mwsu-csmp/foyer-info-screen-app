from django.shortcuts import render, redirect
import json
import qrcode
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

# GLOBALID helps us keep track of where we are in the slideshow
GLOBALID = 1

# Helper functions to support the functionality in the views

#  This function will generate a qr code and save it as an image. Basic fuction for now redirects to google
#   until webapp has established url on a server
def qrGen(request):

    img = qrcode.make('http://google.com')
    response = HttpResponse(content_type='image/jpg')
    img.save(response, "JPEG")
    return response

# This function will keep track of a global ID value that starts at 1 and goes to the amount of
# of objects/slides we have in our newsData.json file. This global ID value will allow us to
# to "loop" through our slides using an html redirect
def slideCounter():
    global GLOBALID
    # Open the file and create a list that we can look at loaded with json objects
    with open('news/static/newsData.json') as fin:
        slidelist = json.loads(fin.read())
        # Set maxItems to length of the list of json objects
        maxItems = len(slidelist)
        # Check if GLOBALID is at maxItems
        if(GLOBALID == maxItems):
            # If it is, reset GLOBALID to 1 and return
            GLOBALID = 1
            return(GLOBALID)
        else:
            # If it is not, step GLOBALID up by 1 and return
            GLOBALID += 1
            return(GLOBALID)


# These are views that load a webpage
def index(request):

    print("In basic index function")
    return render(request, "news/index.jinja")


def slideView(request):
    id = slideCounter()
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