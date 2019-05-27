from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        print("request.POST :", request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("form.cleaned_data :", form.cleaned_data)
            username = form.cleaned_data.get('username')
    else:
        form = UserCreationForm()
    return render(request, template_name='users/register.html', context={'form':form})
