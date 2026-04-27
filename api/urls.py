from django.urls import path
from .views import PageDataView, ContactRequestCreateView

urlpatterns = [
    path('page-data/', PageDataView.as_view(), name='page-data'),
    path('contact/', ContactRequestCreateView.as_view(), name='contact-create'),
]
