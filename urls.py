from django.conf.urls import url, patterns, include
from rest_framework import viewsets, routers

from louisville_crime.models import Incident

# ViewSets define the view behavior.
class IncidentViewSet(viewsets.ModelViewSet):
    model = Incident

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'incidents', IncidentViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
