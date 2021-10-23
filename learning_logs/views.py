import learning_logs
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic
from .forms import TopicForm, EntryForm
from .models import Topic, Entry 

# Create your views here.
def index(request):
    """The home page for Learning_log."""
    return render(request, 'learning_logs/index.html')

    #views give path to pages
@login_required
def topics(request):
    """Show all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context )
@login_required
def topic(request, topic_id):
    """Show single topic and all entries"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
@login_required
def new_topic(request):
    """Adding new topic"""
    if request.method != 'POST':
        #no data, submit blank form
        form = TopicForm()
    else:
        #Post data submitted, data can be processed
        form = TopicForm(data=request.POST)
        if form.is_valid():
           new_topic = form.save(commit=False)
           new_topic.owner = request.user
           new_topic.save()
        return redirect('learning_logs:topics')
    #Display black or invalid form
    context = {'form': form}
    return render(request,'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """new entry for specific topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #no data submitted, blank form
        form = EntryForm()
    else:
        #POST data submitted, process
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic' , topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """edit existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        #initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)

    else: 
        # POST data submitted, process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic':topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)
