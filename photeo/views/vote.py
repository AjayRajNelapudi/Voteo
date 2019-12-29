from django.views import View
from photeo.models import Contestant, Voter
from django.shortcuts import render, redirect
from photeo.forms import VoterForm

class VoteView(View):
    def get(self, request, *args, **kwargs):
        email = kwargs.get('email')
        picture = Contestant.objects.get(email=email)
        voter_form = VoterForm()
        return render(
            request,
            template_name='vote.html',
            context={
                'picture': picture,
                'voter_form': voter_form,
            }
        )

    def post(self, request, *args, **kwargs):
        contestant_email = kwargs.get('email')
        voter_email = request.POST['email']

        contestant = Contestant.objects.get(email=contestant_email)

        voter = Voter.objects.filter(email=voter_email, verified=True)
        if voter:
            return redirect('gallery')

        voter = Voter.objects.get(email=voter_email)
        if voter:
            voter.vote = contestant
            voter.save()
        else:
            vote = Voter(email=voter_email, vote=contestant)
            vote.save()

        return render(
            request,
            template_name="auth_vote.html",
            context={
                'email': voter_email
            }
        )
