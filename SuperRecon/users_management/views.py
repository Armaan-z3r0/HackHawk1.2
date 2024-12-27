from django.shortcuts import render , redirect 
from django.contrib.auth import login , authenticate ,logout

# Create your views here.
def home(request):
    return render(request,'home.html')

def login_view(request):
    return render(request,'login.html')

def logout_view(request):
    return render(request,'logout.html')

def register(request):
    return render(request,'register.html')

def process_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is None :
            context = {'error':'Username or password is invalid'}
            return render(request,"login.html",context)
        login(request,user)
    return redirect('dashboard')

def process_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request,'logout')

#def process_register(request):
    
