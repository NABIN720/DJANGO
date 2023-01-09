from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.

#here yo view le model bata data liyera template ma show garyo
#mymembeers vanne object chai Member(model) value ko vayo
def membeers(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('members/all_members.html')
    context= {
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context, request))






# The details view does the following:

# Gets the id as an argument.
# Uses the id to locate the correct record in the Member table.
# loads the details.html template.
# Creates an object containing the member.
# Sends the object to the template.
# Outputs the HTML that is rendered by the template.

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('members/details.html')
    context = {
        'mymember':mymember,
    }
    return HttpResponse(template.render(context, request))