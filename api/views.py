import requests
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import (
    GeneralSetting, HeroSection, ExperienceSection, ServiceSection, 
    GallerySection, ContactSection, ExperienceCard, ServiceCard, 
    GalleryImage, ContactRequest, PhoneNumber, EmailAddress
)
from .serializers import (
    GeneralSettingSerializer, HeroSectionSerializer, ExperienceSectionSerializer,
    ServiceSectionSerializer, GallerySectionSerializer, ContactSectionSerializer,
    ExperienceCardSerializer, ServiceCardSerializer, 
    GalleryImageSerializer, ContactRequestSerializer,
    PhoneNumberSerializer, EmailAddressSerializer
)

class PageDataView(APIView):
    def get(self, request):
        general = GeneralSetting.objects.first()
        hero = HeroSection.objects.first()
        experience = ExperienceSection.objects.first()
        service = ServiceSection.objects.first()
        gallery = GallerySection.objects.first()
        contact = ContactSection.objects.first()
        
        exp_cards = ExperienceCard.objects.all()
        service_cards = ServiceCard.objects.all()
        gallery_images = GalleryImage.objects.all()
        phones = PhoneNumber.objects.all()
        emails = EmailAddress.objects.all()

        return Response({
            'general': GeneralSettingSerializer(general, context={'request': request}).data if general else None,
            'hero': HeroSectionSerializer(hero).data if hero else None,
            'experience': ExperienceSectionSerializer(experience).data if experience else None,
            'service': ServiceSectionSerializer(service).data if service else None,
            'gallery': GallerySectionSerializer(gallery).data if gallery else None,
            'contact': ContactSectionSerializer(contact).data if contact else None,
            
            'experience_cards': ExperienceCardSerializer(exp_cards, many=True, context={'request': request}).data,
            'service_cards': ServiceCardSerializer(service_cards, many=True, context={'request': request}).data,
            'gallery_images': GalleryImageSerializer(gallery_images, many=True, context={'request': request}).data,
            'phones': PhoneNumberSerializer(phones, many=True).data,
            'emails': EmailAddressSerializer(emails, many=True).data,
        })

from django.conf import settings

class ContactRequestCreateView(generics.CreateAPIView):
    queryset = ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        
        # Send message to Telegram bot
        token = settings.TG_BOT_TOKEN
        chat_id = settings.TG_CHAT_ID
        site_name = settings.SITE_NAME
        
        if token and chat_id:
            text = (
                f"🚀 НОВАЯ ЗАЯВКА | {site_name}\n\n"
                f"👤 Клиент: {instance.name}\n"
                f"📞 Телефон: {instance.phone}\n"
                f"📝 Детали: {instance.details if instance.details else 'Не указаны'}\n\n"
                f"--- \n"
                f"⚡️ Пожалуйста, свяжитесь как можно скорее!"
            )
            
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            payload = {
                "chat_id": chat_id,
                "text": text
            }
            try:
                response = requests.post(url, json=payload, timeout=5)
                print(f"Telegram response: {response.status_code}, {response.text}")
            except Exception as e:
                print("Failed to send telegram message", e)
