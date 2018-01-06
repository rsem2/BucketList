# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Idea, Activity, Post
from ..users_app.models import User
from time import strftime

# Create your views here.
def profile(request):
    return render(request,'profile.html')

def add_idea(request):
    return render(request, 'new_idea.html')

def idea_process(request):
    user = User.objects.get(id = request.session['userid'])
    idea = Idea.objects.createIdea(request.POST, user)
    string = '/dashboard/idea/'+str(idea.id)
    return redirect(string)

def idea(request, num):
    user = User.objects.get(id=request.session['userid'])
    context = {
        'idea': Idea.objects.get(id=num),
        'user': user,
        'friends': user.friends.all(),
    }
    return render(request, 'idea.html', context)

def add_activity(request, num):
    idea = Idea.objects.get(id=num)
    user = User.objects.get(id=request.session['userid'])
    activity = Activity.objects.createActivity(request.POST, idea, user)
    # return redirect('/dashboard/idea/'+num)
    string = '/dashboard/activity/'+str(activity.id)
    return redirect(string)

def activity(request,num):
    friends = User.objects.get(id=request.session['userid']).friends.all()
    people = Activity.objects.get(id=num).people.all()
    for person in people:
        friends = friends.exclude(id = person.id)  

    context = {
        'activity': Activity.objects.get(id=num),
        'user': User.objects.get(id=request.session['userid']),
        'people': people,
        'friends': friends,
        'posts': Activity.objects.get(id=num).posts.all()
    }

    return render(request, 'activity.html', context)

def add_people(request,num):
    activity = Activity.objects.get(id=num)
    Activity.objects.addPeople(request.POST,activity)
    return redirect('/dashboard/activity/'+num)

def remove_person(request, num1, num2):
    activity = Activity.objects.get(id=num1)
    person = User.objects.get(id=num2)
    Activity.objects.removePerson(activity, person)
    return redirect('/dashboard/activity/'+num1)

def add_post(request, num):
    activity = Activity.objects.get(id=num)
    user = User.objects.get(id=request.session['userid'])
    Post.objects.createPost(request.POST,activity, user)
    return redirect('/dashboard/activity/'+num)

def add_book(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request,'books_app/new_book.html', context)

def book(request, num):
    x = Book.objects.get(id=num).reviews.all()[0].stars
    print x
    print type(x)
    context = {
        'book': Book.objects.get(id=num),
        'reviews': Book.objects.get(id=num).reviews.all(),
    }
    return render(request,'books_app/book.html', context)

def review(request, num):
    user = User.objects.get(id = request.session['userid'])
    book = Book.objects.get(id=num)
    Review.objects.createReview(request.POST, book, user)
    string = "/dashboard/book/"+num
    return redirect(string)
