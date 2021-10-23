"""Defines URL patterns for learning_logs."""
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #URL gives path to views 
    path('topics/' , views.topics, name='topics'),
    # page to show all topics
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #page to show individual topic pages and details
    path('new_topic/' , views.new_topic, name='new_topic'),
    #Page to add new topic
    path('new_entry/<int:topic_id>/' , views.new_entry, name='new_entry'),
    #Page to add new entry
    path('edit_entry/<int:entry_id>/' , views.edit_entry, name='edit_entry')
]