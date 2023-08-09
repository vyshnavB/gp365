# views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from app1.models import Login
from django.http import JsonResponse
from app1.models import Device

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Login.objects.get(email=email, password=password, status='Active')
            response = {
                "association_id": user.association_id,
                "association_user_id": user.association_user_id,
                "status": Active,
                "responseCode": 0,
                "message": "Success"
            }
        except Login.DoesNotExist:
            response = {
                "responseCode": 1,
                "message": "Failed"
            }
        
        return JsonResponse(response)

    # For GET request or initial display of login page
    return render(request, 'login.html')


def display_devices(request):
    # Query all devices from the Device model
    devices = Device.objects.all()
    
    if devices:
        # If devices exist, display the devices.
        return render(request, 'devices.html', {'devices': devices})
    else:
        # If no devices exist, return response code 1.
        return render(request, 'response_failed.html', {'responseCode': "1"})