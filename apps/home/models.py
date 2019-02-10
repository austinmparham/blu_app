from __future__ import unicode_literals
from django.db import models
# Create your models here.
class Spell(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField()
	icon = models.TextField()
	lvl_learned = models.IntegerField()
	cast_time = models.FloatField(null=True)
	recast_time = models.FloatField(null=True)
	mp_cost = models.IntegerField()
	cast_range = models.IntegerField()
	cast_radius = models.IntegerField()
	spell_type = models.CharField(max_length=255, null=True)
	phys_type = models.CharField(max_length=255, null=True)
	element = models.CharField(max_length=255, null=True)
	star_rank = models.IntegerField(null=True)
	acquisition = models.CharField(max_length=255, null=True)
	# learned_from = ArrayField(models.TextField())

class Monster(models.Model):
	name = models.CharField(max_length=255)
	level = models.IntegerField()
	link = models.CharField(max_length=255)
	spell = models.ForeignKey(Spell, related_name="monsters",on_delete=models.CASCADE)
