from django.core.management.base import BaseCommand
from core.models import (
    GeneralSetting, HeroSection, ExperienceSection, ServiceSection,
    GallerySection, ContactSection, ExperienceCard, ServiceCard,
    GalleryImage, PhoneNumber, EmailAddress
)
from django.core.files.base import ContentFile
import requests

class Command(BaseCommand):
    help = 'Seeds the database with initial data for the lift installation website'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        # 1. General Setting
        GeneralSetting.objects.update_or_create(
            id=1,
            defaults={
                'brand_name': 'OSTEN',
                'navbar_logo': 'logos/logo.gif',
                'footer_logo': 'logos/footer_logo.gif',
            }
        )

        # 2. Hero Section
        HeroSection.objects.update_or_create(
            id=1,
            defaults={
                'hero_bg': 'hero/Gemini_Generated_Image_lgr2welgr2welgr2.png',
                'mini_title_uz': 'Professional lift xizmatlari',
                'mini_title_ru': 'Профессиональные услуги лифтов',
                'mini_title_en': 'Professional lift services',
                'title_uz': 'Binoingiz uchun eng yaxshi lift yechimlari',
                'title_ru': 'Лучшие лифтовые решения для вашего здания',
                'title_en': 'Best lift solutions for your building',
                'desc_uz': 'Biz yuqori sifatli liftlarni o\'rnatish va ularga xizmat ko\'rsatish bo\'yicha mutaxassislarimiz.',
                'desc_ru': 'Мы эксперты по установке и обслуживанию высококачественных лифтов.',
                'desc_en': 'We are experts in installing and maintaining high-quality lifts.',
            }
        )

        # 3. Experience Section
        ExperienceSection.objects.update_or_create(
            id=1,
            defaults={
                'mini_title_uz': 'Bizning tajribamiz',
                'mini_title_ru': 'Наш опыт',
                'mini_title_en': 'Our Experience',
                'title_uz': 'Nima uchun bizni tanlashadi?',
                'title_ru': 'Почему выбирают нас?',
                'title_en': 'Why choose us?',
                'desc_uz': 'Ko\'p yillik tajriba va professional jamoa bilan biz mijozlarimizga eng yaxshi xizmatni taqdim etamiz.',
                'desc_ru': 'Благодаря многолетнему опыту и профессиональной команде мы предоставляем лучший сервис нашим клиентам.',
                'desc_en': 'With years of experience and a professional team, we provide the best service to our clients.',
            }
        )

        # 4. Service Section
        ServiceSection.objects.update_or_create(
            id=1,
            defaults={
                'mini_title_uz': 'Xizmatlarimiz',
                'mini_title_ru': 'Наши услуги',
                'mini_title_en': 'Our Services',
                'title_uz': 'Biz taqdim etadigan xizmatlar',
                'title_ru': 'Услуги, которые мы предоставляем',
                'title_en': 'Services we provide',
                'desc_uz': 'Biz liftlarni o\'rnatishdan tortib texnik xizmat ko\'rsatishgacha bo\'lgan barcha xizmatlarni taqdim etamiz.',
                'desc_ru': 'Мы предоставляем все услуги от установки до технического обслуживания лифтов.',
                'desc_en': 'We provide all services from lift installation to technical maintenance.',
            }
        )

        # 5. Gallery Section
        GallerySection.objects.update_or_create(
            id=1,
            defaults={
                'mini_title_uz': 'Galereya',
                'mini_title_ru': 'Галерея',
                'mini_title_en': 'Gallery',
                'title_uz': 'Bizning so\'nggi loyihalarimiz',
                'title_ru': 'Наши последние проекты',
                'title_en': 'Our latest projects',
            }
        )

        # 6. Contact Section
        ContactSection.objects.update_or_create(
            id=1,
            defaults={
                'mini_title_uz': 'Bog\'lanish',
                'mini_title_ru': 'Контакты',
                'mini_title_en': 'Contact',
                'title_uz': 'Bepul konsultatsiya oling',
                'title_ru': 'Получите бесплатную консультацию',
                'title_en': 'Get a free consultation',
                'desc_uz': 'Savollaringiz bormi? Biz bilan bog\'laning va biz sizga yordam beramiz.',
                'desc_ru': 'У вас есть вопросы? Свяжитесь с нами, и мы вам поможем.',
                'desc_en': 'Have questions? Contact us and we will help you.',
            }
        )

        # 7. Experience Cards
        exp_cards = [
            {
                'title_uz': '10+ Yillik tajriba',
                'title_ru': '10+ Лет опыта',
                'title_en': '10+ Years of experience',
                'desc_uz': 'Sohada ko\'p yillik muvaffaqiyatli ish stajiga egamiz.',
                'desc_ru': 'У нас многолетний опыт успешной работы в данной сфере.',
                'desc_en': 'We have many years of successful work experience in the field.',
            },
            {
                'title_uz': '500+ Loyihalar',
                'title_ru': '500+ Проектов',
                'title_en': '500+ Projects',
                'desc_uz': 'O\'zbekiston bo\'ylab yuzlab loyihalarni amalga oshirdik.',
                'desc_ru': 'Мы реализовали сотни проектов по всему Узбекистану.',
                'desc_en': 'We have implemented hundreds of projects across Uzbekistan.',
            },
            {
                'title_uz': '24/7 Qo\'llab-quvvatlash',
                'title_ru': '24/7 Поддержка',
                'title_en': '24/7 Support',
                'desc_uz': 'Bizning xizmatlarimiz har doim siz uchun mavjud.',
                'desc_ru': 'Наши услуги всегда доступны для вас.',
                'desc_en': 'Our services are always available for you.',
            }
        ]
        for card in exp_cards:
            ExperienceCard.objects.get_or_create(**card)

        # 8. Service Cards
        service_cards = [
            {
                'title_uz': 'O\'rnatish',
                'title_ru': 'Установка',
                'title_en': 'Installation',
                'desc_uz': 'Har qanday turdagi liftlarni professional o\'rnatish.',
                'desc_ru': 'Профессиональная установка лифтов любого типа.',
                'desc_en': 'Professional installation of all types of lifts.',
                'icon': 'services/icon1.gif'
            },
            {
                'title_uz': 'Texnik xizmat',
                'title_ru': 'Техническое обслуживание',
                'title_en': 'Maintenance',
                'desc_uz': 'Liftlarning xavfsiz va uzluksiz ishlashini ta\'minlash.',
                'desc_ru': 'Обеспечение безопасной и бесперебойной работы лифтов.',
                'desc_en': 'Ensuring safe and uninterrupted operation of lifts.',
                'icon': 'services/icon2.gif'
            },
            {
                'title_uz': 'Modernizatsiya',
                'title_ru': 'Модернизация',
                'title_en': 'Modernization',
                'desc_uz': 'Eski liftlarni zamonaviy talablarga moslashtirish.',
                'desc_ru': 'Адаптация старых лифтов под современные требования.',
                'desc_en': 'Adapting old lifts to modern requirements.',
                'icon': 'services/icon3.gif'
            }
        ]
        for card in service_cards:
            ServiceCard.objects.get_or_create(
                title_ru=card['title_ru'],
                defaults=card
            )

        # 9. Gallery Images
        gallery_images = [
            {
                'title_uz': 'Turar-joy binosidagi lift',
                'title_ru': 'Лифт в жилом доме',
                'title_en': 'Lift in a residential building',
                'image': 'gallery/gallery1.gif'
            },
            {
                'title_uz': 'Biznes markazdagi lift',
                'title_ru': 'Лифт в бизнес-центре',
                'title_en': 'Lift in a business center',
                'image': 'gallery/gallery2.gif'
            }
        ]
        for img in gallery_images:
            GalleryImage.objects.get_or_create(
                title_ru=img['title_ru'],
                defaults=img
            )

        # 10. Phone Numbers
        PhoneNumber.objects.get_or_create(number='+998 90 123 45 67')
        PhoneNumber.objects.get_or_create(number='+998 71 200 00 00')

        # 11. Email Addresses
        EmailAddress.objects.get_or_create(email='info@osten.uz')
        EmailAddress.objects.get_or_create(email='sales@osten.uz')

        self.stdout.write(self.style.SUCCESS('Successfully seeded data!'))
