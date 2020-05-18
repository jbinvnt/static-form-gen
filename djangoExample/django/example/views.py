from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
from .forms import CarForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def carEndpoint(request): #We're exempting this one because it is an example and AJAX CSRF is an extra step
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            newCar = Car(license_plate=form.cleaned_data['license_plate'], purchase_date=form.cleaned_data['purchase_date'], vin_number=form.cleaned_data['vin_number'], miles=form.cleaned_data['miles'])
            newCar.save()
            return HttpResponse("Car created successfully")
    return HttpResponse("Error creating car")
