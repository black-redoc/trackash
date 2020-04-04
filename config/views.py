from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


def index_dashboard(request):
    return HttpResponseRedirect(reverse_lazy("budget:dashboard"))
