from django.shortcuts import render

# Create your views here.

def index(request):

	return render(request, 'index.html')
def blog(request):

	return render(request, 'blog.html')
def elements(request):

	return render(request, 'elements.html')
def blog_details(request):

	return render(request, 'blog_details.html')
