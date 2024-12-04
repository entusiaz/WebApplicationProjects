from django.shortcuts import render
from django.urls import path
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

import user.views


app_name = 'user'


class RegisterView(CreateView):
    template_name = 'user/register.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should redirect to home.
        form.save()
        # username = form.cleaned_data.get('username')
        # password = form.cleaned_data.get('password')
        # user = authenticate(username=username, password=password)
        # login(request, user)
        return redirect('/')
