from datacenter.models import Visit
from django.shortcuts import render
 

def storage_information_view(request):
    
    non_closed_visits = []
    non_leaved_visits = Visit.objects.filter(leaved_at=None)

    for non_leaved_visit in non_leaved_visits:
        passcard = non_leaved_visit.passcard
                
        visit_dataset = {
            'who_entered': passcard.owner_name,
            'entered_at': non_leaved_visit.entered_at,
            'duration': non_leaved_visit.format_duration(),
            'is_strange': non_leaved_visit.is_long(),
        }

        non_closed_visits.append(visit_dataset)

    context = {
        'non_closed_visits': non_closed_visits,  
    }
    return render(request, 'storage_information.html', context)
    