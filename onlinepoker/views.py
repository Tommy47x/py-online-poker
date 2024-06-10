# Create your views here.
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from django.http import HttpResponseRedirect

def poker_view(request):
    # You can define the game_state or other variables here
    game_state = "Your current cards or game status"
    return render(request, 'onlinepoker/poker.html', {'game_state': game_state})

class HomeView(LoginRequiredMixin, View):
    login_url = '/login/'  # Redirect to login page if not authenticated
    redirect_field_name = 'redirect_to'
    def get(self, request):
        # your code for handling GET request
        return render(request, 'onlinepoker/home.html')  # Make sure you have a home.html template


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page.
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    

