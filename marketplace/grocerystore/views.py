from django.shortcuts import render
from django.http import HttpResponse
from .models import Exito
from django.http import Http404

# Create your views here.
def index(request):
    latest_results_list = Exito.objects.order_by('-unit_price')[:5]
    context = {
        'latest_results_list': latest_results_list,
    }
    return render(request, 'grocerystore/index.html', context)

def detail(request, result_id):
    try:
        result = Exito.objects.get(pk=result_id)
    except Exito.DoesNotExist:
        raise Http404("Result does not exist")
    return render(request, 'grocerystore/detail.html', {'result': result})

def results(request, result_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % result_id)

def vote(request, result_id):
    return HttpResponse("You're voting on question %s." % result_id)