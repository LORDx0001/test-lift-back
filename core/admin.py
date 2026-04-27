from django.contrib import admin
from .models import (
    GeneralSetting, HeroSection, ExperienceSection, ServiceSection, 
    GallerySection, ContactSection, ExperienceCard, ServiceCard, 
    GalleryImage, ContactRequest, PhoneNumber, EmailAddress
)

class SingletonAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not self.model.objects.exists()

@admin.register(GeneralSetting)
class GeneralSettingAdmin(SingletonAdmin):
    pass

@admin.register(HeroSection)
class HeroSectionAdmin(SingletonAdmin):
    pass

@admin.register(ExperienceSection)
class ExperienceSectionAdmin(SingletonAdmin):
    pass

@admin.register(ServiceSection)
class ServiceSectionAdmin(SingletonAdmin):
    pass

@admin.register(GallerySection)
class GallerySectionAdmin(SingletonAdmin):
    pass

@admin.register(ContactSection)
class ContactSectionAdmin(SingletonAdmin):
    pass

@admin.register(ExperienceCard)
class ExperienceCardAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'title_uz', 'title_en')

@admin.register(ServiceCard)
class ServiceCardAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'title_uz', 'title_en')

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'title_uz', 'title_en')

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at')
    search_fields = ('name', 'phone')
    list_filter = ('created_at',)

@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    pass

@admin.register(EmailAddress)
class EmailAddressAdmin(admin.ModelAdmin):
    pass
