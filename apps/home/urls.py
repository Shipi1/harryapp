# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views, views1

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    path('botoncito/',views1.botoncito,name="botoncito"),
    path('ingresarEmocion/',views1.entrydiario,name="entrydiario"),
    path('test',views1.testForm,name="testForm"),
    path('samplepage',views1.samplepage,name="samplepage"),
    path('diario.html',views1.diario,name="diario"),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
