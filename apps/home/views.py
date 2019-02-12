from django.shortcuts import render, HttpResponse, redirect
import urllib as urllib2, json
from .models import *
# the index function is called when root is visited
def index(request):
	spells = Spell.objects.all()
	content = {
	'spells': spells
	}
	return render(request, "blu_app/spells.html", content)

def spells(request):
	spells = Spell.objects.all()
	content = {
	'spells': spells
	}
	return render(request, "blu_app/spells.html", content)


def add_spell(request):
	print("Visit add_spell")
	Spell.objects.create(name=request.POST['name'],desc=request.POST['desc'],lvl_learned=request.POST['lvl_learned'],cast_time=request.POST['cast_time'],recast_time=request.POST['recast_time'],mp_cost=request.POST['mp_cost'],cast_range=request.POST['cast_range'],cast_radius=request.POST['cast_radius'],spell_type=request.POST['spell_type'],element=request.POST['element'],star_rank=request.POST['star_rank'],phys_type=request.POST['phys_type'])
	return redirect("/spells")

def sort(request, element):
	first_spells = Spell.objects.filter(element=element)
	spells = first_spells.filter(spell_type="Magic")
	content = {
	'spells':spells
	}
	return render(request, "blu_app/spells.html", content)

def type(request, spell_type):
	spells= Spell.objects.filter(spell_type=spell_type)
	content={
	'spells':spells
	}
	return render(request, "blu_app/spells.html", content)

def level(request):
	spells = Spell.objects.order_by("lvl_learned")
	content={
	'spells':spells
	}
	return render(request,"blu_app/spells.html", content)

def monster(request):
	spell = Spell.objects.get(id=request.POST['spell'])
	print(spell.name)
	Monster.objects.create(name=request.POST['name'],level=request.POST['level'],link=request.POST['link'],spell=spell)
	return redirect("/imcoocooforcocoapuffs")

def add_acq(request):
	spell = Spell.objects.get(id=request.POST['spell'])
	print(spell.name)
	spell.acquisition = request.POST['acquisition']
	spell.save()
	return redirect("/imcoocooforcocoapuffs")