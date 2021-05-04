from .models import User, Friend, Event, Information, AdjustingSchedule
# Create your views here.

from django.views import generic
 
 
class HomeView(generic.TemplateView):
    template_name = 'home.html'
 
class WelcomeView(generic.TemplateView):
    template_name = 'welcome.html'
