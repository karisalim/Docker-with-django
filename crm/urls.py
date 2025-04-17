# from django.urls import path
# from .views import *


# urlpatterns = [         
#     path('', MyView.as_view(), name='home'),
#     path('Hello/', Say.as_view(), name='hello'),# استدعاء as_view() لتحويل الكلاس إلى دالة
#     path('Time/<str:name>/<uuid:pk>/', Time.as_view(), name='time'),  # ✅ استخدام UUID بدل int
#     path('showform/', ShowForm.as_view(), name='showform'),  
#     path('getform/', GetForm.as_view(), name='getform'),  
    

# ]

from django.urls import path , re_path
from .views import *

urlpatterns = [
    path('', MyView.as_view(), name='home'),
    path('Hello/', Say.as_view(), name='hello'),
    re_path(r'^Time/(?P<name>\w+)/(?P<pk>[0-9a-f-]{36})/$', Time.as_view(), name='time'),
    # path('Time/<str:name>/<uuid:pk>/', Time.as_view(), name='time'),
    path('showform/', ShowForm.as_view(), name='showform'),
    path('getform/', GetForm.as_view(), name='getform'),
    path('restricted/', RestrictedView.as_view(), name='restricted'),
]
