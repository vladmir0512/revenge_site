from django.views.generic.base import TemplateView
from django.shortcuts import render
from . import models


# Create your views here.
class HomePageView(TemplateView):

    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['persons'] = models.Person.objects.all()
        context['singers'] = models.Singer.objects.all()
        context['ranks'] = models.Singer.objects.all()

        # context['latest_articles'] = Article.objects.all()[:5]
        return context
    # HTTP Error 400

class SchedulePageView(TemplateView):

    template_name = "main/schedule.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context['latest_articles'] = Article.objects.all()[:5]
        return context

class ArtsPageView(TemplateView):

    template_name = "main/arts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context['latest_articles'] = Article.objects.all()[:5]
        return context

class MembersPageView(TemplateView):

    template_name = "main/members.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context['latest_articles'] = Article.objects.all()[:5]
        return context

class RulesPageView(TemplateView):

    template_name = "main/rules.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context['latest_articles'] = Article.objects.all()[:5]
        return context   
    
    
def custom_page_not_found_view(request, exception):
    return render(request, "errors/404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "errors/500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "errors/403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "errors/400.html", {})