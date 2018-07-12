from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #log the user in
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'userForm': form})
