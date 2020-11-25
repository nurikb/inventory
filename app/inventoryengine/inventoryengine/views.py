from django.shortcuts import redirect
from django.http import HttpResponse

def redirect_inventory(request):
    return redirect('admissions_url', permanent=True)
