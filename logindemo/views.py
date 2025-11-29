from django.shortcuts import render
from allauth.account.views import LoginView
# Create your views here.

def home(request):
    return render(request, 'logindemo/home.html')


class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    success_url = '/'