from django.shortcuts import render
from .models import customer_details, renewal, trainer_details, branch, subscription
from. import  views
# Create your views here.
def index(request):
    num_customer =customer_details.objects.all().count()
    num_renewal =renewal.objects.all().count()
    num_trainer_details = trainer_details.objects().count()
    context = {
        'num_customer': num_customer,
        'num_renewal' : num_renewal,
        'num_trainer' : num_trainer_details,
    }
    return render(request, 'index.html', context=context)
