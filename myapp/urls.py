from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('getuserfeedbackform',views.getuserfeedbackform,name="getuserfeedbackform"),
    path('cloudantcsv',views.cloudantcsv,name="cloudantcsv"),
    path('saveuserfeedbackform',views.saveuserfeedbackform,name="saveuserfeedbackform"),
    path('api',views.api,name='api'),
    path('testresults',views.testresults,name='testresults'),
    path('search',views.search,name="search"),
    path('result',views.result,name='result'),
    path('fetchanalysis',views.fetchanalysis,name='fetchanalysis'),
    path('about',views.about,name='about'),
    path('geturlhistory',views.geturlhistory,name="geturlhistory"),
    path('discuss',views.discuss,name="discuss"),
    path('reply/<int:replyid>',views.replyform,name="reply"),
    path('savereply',views.savereply,name="reply"),
    path('searchdiscuss',views.searchdiscuss,name="searchdiscuss"),
    path('getdataset',views.getdataset,name='getdataset')

]

