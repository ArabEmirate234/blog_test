from django.shortcuts import render

from about import models as about_models
from elenizado import models as elenizado_models

from . import models


# Create your views here.
def poeme(request):
    events_r = elenizado_models.Evenement.objects.all().order_by("-date_add")[:3]
    gallerie = about_models.Gallerie.objects.filter(status=True)
    poeme = models.Poesie.objects.filter(status=True)
    datas = {
        "events_r": events_r,
        "gallerie": gallerie,
        "poeme": poeme,
    }
    return render(request, "pages/poesie.html", datas)
