from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    this_passcard_visits_filtered = Visit.objects.filter(passcard = passcard)
  
    this_passcard_visits = []
    for visit in this_passcard_visits_filtered:
        duration = visit.format_duration()
        visit.is_long = visit.get_duration().total_seconds() // 3600 > 1
             
        this_passcard_visits_dataset = {
              'entered_at': visit.entered_at,
              'duration': duration,
              'is_strange': visit.is_long
        }
          
        this_passcard_visits.append(this_passcard_visits_dataset)

    
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
