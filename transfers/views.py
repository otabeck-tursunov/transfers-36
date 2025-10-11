from django.shortcuts import render
from django.db.models import F, ExpressionWrapper, Func
from .models import *


def latest_transfers_view(request):
    last_season = Season.objects.order_by('name').last()
    transfers = Transfer.objects.filter(season=last_season).order_by('-price')
    context = {
        'last_season': last_season,
        'transfers': transfers
    }
    return render(request, 'latest-transfers.html', context)


def stats_view(request):
    return render(request, 'stats.html')


def stats_top_150_accurate_predictions(request):
    class Round(Func):
        function = 'ROUND'
        template = '%(function)s(%(expressions)s, 2)'

    transfers = Transfer.objects.annotate(
        accurate_predictions=ExpressionWrapper(
            Round(
                Func(
                    (F('price') - F('price_tft')) / F('price_tft') * 100,
                    function='ABS'
                )
            ),
            output_field=models.FloatField()
        )
    ).order_by('accurate_predictions')
    context = {
        'transfers': transfers
    }
    return render(request, 'stats/150-accurate-predictions.html', context)
