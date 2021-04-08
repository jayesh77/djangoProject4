from  django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import FormView,CreateView
from registration.models import incident


class MyLogin(views.LoginView):
    template_name = 'registration/login.html'


@method_decorator(login_required,name='dispatch')
class incidentviews(CreateView):
    model = incident
    fields = ['location','incident_department','Suspected_Cause',
              'Initial_Severity','environment_incident',"Vehicle",'property_damage']
    success_url = '/dashboard'
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)
