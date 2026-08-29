from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import URegister

def register(request):
    if request.method == 'POST':
        form = URegister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('users:login')
    else:
        form = URegister()
    return render(request, 'users/register.html', {'form': form})