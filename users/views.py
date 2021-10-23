from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

#Registering a new user


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        # Process Completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #Log user and redirect to home 
            login(request, new_user)
            return redirect('learning_logs:index')
            

    


         
    context = {'form': form}
    return render(request, 'registration/register.html', context)
