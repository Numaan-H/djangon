from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Issue
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import User
import requests
from products.forms import ContactForm

# Create your views here.

def home(request):

    url = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&units=metric&appid={}'
    cities = [('Huddersfield', 'UK')]
    weather_data = []
    api_key = '81d097d3c86974d04f2dddb744828a22'

    for city in cities:
        city_weather = requests.get(url.format(city[0], city[1], api_key)).json() # Request the API data and convert the JSON to Python data types

    weather = {
        'city': city_weather['name'] + ', ' + city_weather['sys']['country'],
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description']
    }   
    weather_data.append(weather) # Add the data for the current city into our list
    return render(request, 'itreporting/home.html', {'title': 'Homepage', 'weather_data': weather_data})


# def products(request):
#    return render(request, 'itreporting/products.html')

def about(request):
    return render(request, 'itreporting/about.html')


def admin(request):
    return render(request, 'users/admin.py')


def contact(request):
    
    return render(request, 'itreporting/contact.html')

def report(request):
    # Get all reported issues
    daily_report = {'issues': Issue.objects.all(), 'title': 'Issues Reported'}
    return render(request, 'itreporting/report.html', daily_report)


    # Create a context dictionary to pass to the template
    context = {'issues': issues}

    # Render the report.html template with the context
    return render(request, 'itreporting/report.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            pass
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'itreporting/contact.html', {'form': form})


def success(request):
  return render(request, 'itreporting/success.html')

class PostListView(ListView):
    model = Issue
    ordering = ['-date_submitted']
    template_name = 'itreporting/report.html'
    context_object_name = 'issues'
    paginate_by = 5  # Optional pagination

class PostDetailView(DetailView):
    model = Issue
    template_name = 'itreporting/issue_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):

    model = Issue
    fields = ['type', 'room', 'urgent', 'details']

    def form_valid(self, form): 

        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Issue
    fields = ['type', 'room', 'details']

    def test_func(self):

        issue = self.get_object()

        return self.request.user == issue.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Issue

    success_url = '/report'

    def test_func(self):

        issue = self.get_object()

        return self.request.user == issue.author
    
class UserPostListView(ListView): 

    model = Issue
    template_name = 'itreporting/user_issues.html'
    context_object_name = 'issues'
    paginate_by = 5


    def get_queryset(self):

        user=get_object_or_404(User, username=self.kwargs.get('username'))

        return Issue.objects.filter(author=user).order_by('-date_submitted')
    
