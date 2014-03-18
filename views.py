from django.shortcuts import render, render_to_response
from archiver.models import ArchiverApp

from archiver.decorators import dashboard_view
# Create your views here.
@dashboard_view
def dashboard(request, context):
    context['creators'] = ArchiverApp.objects.get(app_label='louisville_crime').creators.all()
    context['members'] = ArchiverApp.objects.get(app_label='louisville_crime').members.all()
    return render_to_response('louisville_crime/dashboard.html', context)
