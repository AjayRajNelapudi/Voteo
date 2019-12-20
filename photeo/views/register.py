from django import forms
from django.urls import resolve
from django.shortcuts import render, redirect
from django.views import View
from photeo.forms import ContestantRegistrationForm
from photeo.models import *

class ContestantRegistrationView(View):
    def get(self, request, *args, **kwargs):
        contestant = ContestantRegistrationForm()
        return render(
            request,
            template_name='register.html',
            context={
                'contestant': contestant
            }
        )

    def post(self, request, *args, **kwargs):
        contestant_form = ContestantRegistrationForm(request.POST, request.FILES)
        if contestant_form.is_valid():
            contestant_form.save()
            return redirect('gallery')