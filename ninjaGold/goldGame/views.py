from django.shortcuts import render, redirect
from random import random
import datetime

def randi(min, max):
    i = round(random() * max)
    while i < min:
        i = round(random() * max)
    return i

# Create your views here.
def index(request):
    if 'gold' in request.session:
        gold = request.session['gold']
        activities = request.session['activities']
    else:
        gold = 0
        activities = [f'No activities yet! {datetime.datetime.now()}']
        request.session['gold'] = gold
        request.session['activities'] = activities
    context = {
        'gold': gold,
        'activities': activities,
    }
    print(activities)
    print(type(activities))
    return render(request, "index.html", context)

def process_money(request):
    print(request.POST['which_form'])
    if request.POST['which_form'] == 'farm':
        gold_collected = randi(10,20)
        current_activity = f"Earned {gold_collected} golds from {request.POST['which_form']}! {datetime.datetime.now()}"
    elif request.POST['which_form'] == 'cave':
        gold_collected = randi(5,10)
        current_activity = f"Earned {gold_collected} golds from {request.POST['which_form']}! {datetime.datetime.now()}"
    elif request.POST['which_form'] == 'house':
        gold_collected = randi(5,10)
        current_activity = f"Earned {gold_collected} golds from {request.POST['which_form']}! {datetime.datetime.now()}"
    elif request.POST['which_form'] == 'casino':
        gold_collected = randi(5,10)
        if randi(0,1) == 1:
            current_activity = f"Entered a casino and won {gold_collected} golds...NICE!... {datetime.datetime.now()}"
        else:
            current_activity = f"Entered a casino and lost {gold_collected} golds...Ouch... {datetime.datetime.now()}"
            gold_collected = gold_collected * -1

    request.session['gold'] = request.session['gold'] + gold_collected 
    request.session['activities'].append(current_activity)
    return redirect('/')

def delete(request):
    request.session.clear()
    return redirect('/')