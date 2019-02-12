from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^$', views.spells),
	url(r'^spells$', views.spells),
	url(r'^add_spell$', views.add_spell),
	url(r'^spells/(?P<element>\w+)$',views.sort),
	url(r'^type/(?P<spell_type>\w+)$', views.type),
	url(r'^level$',views.level),
	url(r'^monster$',views.monster),
	url(r'^add_acq$',views.add_acq)
]