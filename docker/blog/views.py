from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author':'Gaurav KB',
        'title':'Blog Post 1',
        'content': 'Firtst Post content',
        'date_posted': 'Ausgust 27, 2018'	
    },
    {
        'author':'Jane Dow',
        'title':'Blog Post 2',
        'content': 'Second Post content',
        'date_posted': 'Ausgust 28, 2018'	
    }
]
def home(request):
	context = {
	    'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title':'About'})

