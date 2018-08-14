from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.
def signup(request):
  if request.method == 'POST':
    if request.POST['password'] == request.POST['confirmpw']:
      try:
        user = User.objects.get(username=request.POST['username'])
        return render(request, 'accounts/signup.html', {'error':'Username has already been taken!'})
      except User.DoesNotExist:
        user = User.objects.create_user(
          request.POST['username'], 
          password = request.POST['password'])
        auth_login(request, user)
        return render(request, 'accounts/signup.html', {'success':'Your account of username "' + user.username + '" has been created.'})
    else:
      return render(request, 'accounts/signup.html', {'error':'Passwords didn\'t match.'})
  else:
    return render(request, 'accounts/signup.html')

def login(request):
  if request.method == 'POST':
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is not None:
      auth_login(request, user)
      if 'next' in request.POST:
        if request.POST['next'] is not None:
            return redirect(request.POST['next'])
      # Redirect to a success page.
      return redirect('home')
    else:
      # Return an 'invalid login' error message.
      return render(request, 'accounts/login.html', {'error':'Username and/or password didn\'t match!'})
  else:
    return render(request, 'accounts/login.html')

def logout(request):
  if request.method == 'POST':
    auth_logout(request)
    return redirect('home')