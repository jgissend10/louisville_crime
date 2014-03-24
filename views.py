from django.shortcuts import render, render_to_response
from archiver.models import ArchiverApp

from archiver.decorators import dashboard_view
# Create your views here.
@dashboard_view('louisville_crime')
def dashboard(request, context):
    return render_to_response('louisville_crime/dashboard.html', context)
