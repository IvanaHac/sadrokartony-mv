from django.shortcuts import render

# Create your views here.

def homepageView(req):

    content={}
    return render (req, 'homepage/homepage.html', content)