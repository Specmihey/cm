from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, "home.html", {})

def about(request):
	my_name = "Hello! My name is Michael Chizhov!"
	return render(request, "about.html", {"my_tag": my_name})

def contact(request):
	from pages.namer import bob
	return render(request, "contact.html", {"my_stuff": bob})