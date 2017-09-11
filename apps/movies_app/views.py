# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import datetime
import bcrypt, requests



# Create your views here.
def login_reg(request):
    return render(request, 'movies_app/index.html')

def process(request):
    errors = User.objects.user_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        found_users = User.objects.filter(email = request.POST['email'])
        if found_users.count() > 0:
            messages.error(request, 'Email already taken', extra_tags='email')
            return redirect('/')
        else:
            passwordDB = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            created_user = User.objects.create(name = request.POST['name'], username = request.POST['username'] , email = request.POST['email'], password = passwordDB, birthday = request.POST['birth'], zipCode = request.POST['zipCode'])
            request.session['user_id'] = created_user.id
            request.session['user_name'] = created_user.name
            return redirect('/welcome')

def login(request):
    found_users = User.objects.filter(email = request.POST['email'])
    if found_users.count() > 0:
        found_user = found_users.first()
        if bcrypt.checkpw(request.POST['password'].encode(), found_user.password.encode()) == True:
            request.session['user_id'] = found_user.id
            request.session['user_name'] = found_user.name
            return redirect('/welcome')
        else:
            messages.error(request, 'Login Failed', extra_tags='fail')
            return redirect('/')
    else:
        messages.error(request, 'Login Failed', extra_tags='fail')
        return redirect('/')

def welcome(request):
    the_user = User.objects.get(id = request.session['user_id'])
    context = {
        "the_user": the_user
    }
    return render(request, 'movies_app/welcome.html', context)

def look(request):
    movies = requests.get('http://data.tmsapi.com/v1.1/movies/showings?startDate=' + request.POST['date'] + '&zip=' + request.POST['zip'] + '&api_key=sszbbjhadk82fc9nh469bs2k').content
    return HttpResponse(movies)

def addMovie(request, root_id, movie_title, theatre):
    the_title = str (movie_title.replace("_", " "))
    the_theatre = str (theatre.replace("_", " "))
    the_id = str (root_id)
    the_user = User.objects.get(id = request.session['user_id'])
    the_showtime = Showtime.objects.create(movieID = the_id, title = the_title, theatre = the_theatre)
    the_showtime.save()
    the_showtime.users.add(the_user)
    the_showtime.save()
    return redirect('/moviesAttending')

def moviesAttending(request):
    the_user = User.objects.get(id = request.session['user_id'])
    context = {
        "the_user": the_user,
        "movies": Showtime.objects.filter(users = the_user)
    }
    return render(request, 'movies_app/added.html', context)

def logout(request):
    del request.session['user_name']
    del request.session['user_id']
    messages.error(request, 'Logout Successful', extra_tags='logout')
    return redirect('/')

def delete(request, movie_id):
    Showtime.objects.get(id = movie_id).delete()
    return redirect("/moviesAttending")

def whosGoing(request, movie_id):
    the_movie = Showtime.objects.get(id = movie_id)
    context = {
        "movie": the_movie
    }
    return render(request, 'movies_app/whosGoing.html', context)
