from django.shortcuts import render
from django.views import View

# Create your views here.
class TestView(View):
	def get(self, request):
		context = {}
		return render(request, "test.html", context)
