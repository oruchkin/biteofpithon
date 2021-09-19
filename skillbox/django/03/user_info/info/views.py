from django.shortcuts import render

# Create your views here.

def index(request):
    ip = request.META.get('REMOTE_ADDR')
    return render(request, 'info/user_info.html',{
        "ip_address": ip,
    })