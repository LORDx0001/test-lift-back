from django.urls import path
from .views import PageDataView, ContactRequestCreateView, ServiceCardListAPIView, ServiceCardDetailAPIView

urlpatterns = [
    path('page-data/', PageDataView.as_view(), name='page-data'),
    path('contact/', ContactRequestCreateView.as_view(), name='contact-create'),
    path('services/', ServiceCardListAPIView.as_view(), name='service-list'),
    path('services/<slug:slug>/', ServiceCardDetailAPIView.as_view(), name='service-detail'),
]
