from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Item Has Been Added To List'))
            return render(request, 'home.html', {'all_items': all_items})

    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items':all_items})

def about(request):
    context = {'first_name': 'my_name', 'last_name': 'Richberg'}
    return render(request, 'about.html', context)

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item Has Been Deleted!'))
    return redirect('home')

def nfl_week1(request):
    context = {'first_name': 'my_name', 'last_name': 'Richberg'}
    return render(request, 'nfl_week1.html', context)
