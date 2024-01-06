from django.template import loader
from django.http import HttpResponse

def handler(request):
    template = loader.get_template('homePage.html')
    context = {
        'firstname':'Benjamin',
    }
    return HttpResponse(template.render(context,request))

# Create your views here.
