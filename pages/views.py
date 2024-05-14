from django.views.generic import TemplateView

class TestView(TemplateView):
    template_name = 'pages/test.html'

class AboutView(TemplateView):
    template_name = 'pages/about.html'

class ContactView(TemplateView):
    template_name = 'pages/contact.html'