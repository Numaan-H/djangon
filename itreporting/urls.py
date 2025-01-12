from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from itreporting.views import contact, success

from . import views

app_name = 'itreporting'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    #path('report/', views.report, name='report'),
    path('issues/<int:pk>', PostDetailView.as_view(), name = 'issue-detail'),
    path('report/', PostListView.as_view(), name = 'report'),
    path('issue/new', PostCreateView.as_view(), name = 'issue-create'),
    path('issue/<int:pk>/update/', PostUpdateView.as_view(), name = 'issue-update'),
    path('issue/<int:pk>/delete/', PostDeleteView.as_view(), name = 'issue-delete'),
    path('issue/<str:username>', UserPostListView.as_view(), name = 'user-issues'),
    path('contact/', contact, name='contact'),
    path('success/', success, name='success')
] 

# testing5, signals123
# admin1, Dance@123