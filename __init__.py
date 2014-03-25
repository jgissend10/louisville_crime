from archiver.models import ArchiverApp

app_info = {
    'name':'Louisville Crime',
    'app_label' : 'louisville_crime', 
    'flavor_text' : "Activity of the 5-0 in 502!",
    'description' : "Louisville Crime is a project dedicated to storing a record the crime data for Metro Louisville.",
    'public' : False,
}

try:
    app = ArchiverApp.objects.get(app_label=app_info['app_label'])
    for key, value in app_info.iteritems():
        setattr(app, key, value)
    app.save()
except ArchiverApp.DoesNotExist:
    app = ArchiverApp(**app_info)
    app.save()

