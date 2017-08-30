from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
	template_name = "home_view.html"

class SteerView(TemplateView):
	template_name = "car_control_view.html"
