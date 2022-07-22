from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def loginview(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            context={
                'username':username,
                'errorMessage':': this username not found.'
            }
        return render(request,'users/login.html',context)

    else:    
        return render(request,'users/login.html',{})


def logooutview(request):
    logout(request)
    return redirect('sport_news:index')


def register(request):
    """register a new user"""
    if request.method != "POST":
        form = UserCreationForm()
    
    else:
        form = UserCreationForm(data = request.POST)
        if form .is_valid():
            new_user = form.save()
            #Log the user in and redirect to home page.
            authenticate_user = authenticate(username=new_user.username,password=request.POST['password1'])
            login(request,authenticate_user)
            return redirect('sport_news:index')
    
    context = {'form':form}
    return render(request,'users/register.html',context)