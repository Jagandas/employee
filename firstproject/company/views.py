from django.http import HttpResponse
from company.models import employees

def index(request):
    return HttpResponse('welcome to my homepage')

def detail(request,id):
    dt=employees.objects.get(id=id)
    return HttpResponse(f'{dt.name} {dt.salary}')
    


