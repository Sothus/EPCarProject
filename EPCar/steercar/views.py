from django.shortcuts import render
from django.views.generic import TemplateView

class SteerView(TemplateView):
	template_name = "test.html"
