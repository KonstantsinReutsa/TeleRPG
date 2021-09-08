from django.urls import path
from django.views.generic import RedirectView
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico'), name='favicon'),
    path("start_bot", views.start, name="#"),
    path("start_game", views.start_game, name="#"),
    path("finish_bot", views.stop, name="#"),
    path("answer", views.answer, name=""),
    path('games/', views.games, name="games"),
    path("contact/", views.contact, name="contact"),
    path("RPGame/", views.RPGame, name="RPGame"),
]
