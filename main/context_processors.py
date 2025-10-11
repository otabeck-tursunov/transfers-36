from .models import Country
from django.db.models import Count

def get_countries_context(request):
    contries = Country.objects.annotate(
        club_count=Count('club')
    ).order_by('-club_count')

    context = {
        'countries': contries
    }
    return context


