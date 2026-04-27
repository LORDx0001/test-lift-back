from rest_framework import serializers
from core.models import (
    GeneralSetting, HeroSection, ExperienceSection, ServiceSection, 
    GallerySection, ContactSection, ExperienceCard, ServiceCard, 
    GalleryImage, ContactRequest, PhoneNumber, EmailAddress
)

class GeneralSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralSetting
        fields = '__all__'

class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'

class ExperienceSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceSection
        fields = '__all__'

class ServiceSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceSection
        fields = '__all__'

class GallerySectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GallerySection
        fields = '__all__'

class ContactSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSection
        fields = '__all__'

class ExperienceCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceCard
        fields = '__all__'

class ServiceCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCard
        fields = '__all__'

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = '__all__'

class ContactRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactRequest
        fields = '__all__'

class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = '__all__'

class EmailAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailAddress
        fields = '__all__'
