from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages  # أضف ده عشان نعرض رسائل

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created for {user.username}!')  # رسالة نجاح
            return redirect('home')
        else:
            messages.error(request, 'Error creating account. Please check the form.')  # رسالة خطأ
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})