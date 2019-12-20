from django.db.models import F
from .models import Voter, Contestant

def cast_vote(backend, user, response, *args, **kwargs):
    email = response.get('email')

    contestant = Voter.objects.filter(email=email).values_list('vote__name')
    if not contestant:
        pass
    elif email.split('@')[-1] == 'anits.edu.in':
        pass
    else:
        contestant_name = contestant[0][0]
        Voter.objects.filter(email=email).update(verified=True)
        Contestant.objects.filter(name=contestant_name).update(votes=F('votes') + 1)
