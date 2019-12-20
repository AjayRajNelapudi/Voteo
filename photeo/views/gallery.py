from django import forms
from django.urls import resolve
from django.shortcuts import render, redirect
from django.views import View
from photeo.models import Contestant, Voter
from django.db.models import OuterRef, Subquery, Count

class GalleryView(View):
    def get(self, request, *args, **kwargs):
        pictures = Contestant.objects.all().order_by('-votes')
        return render(
            request,
            template_name='gallery.html',
            context={
                'pictures': pictures,
            }
        )