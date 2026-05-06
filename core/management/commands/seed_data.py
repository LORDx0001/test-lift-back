import os
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from core.models import (
    GeneralSetting, HeroSection, ExperienceSection, ServiceSection, 
    GallerySection, ContactSection, ExperienceCard, ServiceCard, 
    GalleryImage, PhoneNumber, EmailAddress
)
from django.conf import settings

class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')

        # Create a dummy image
        dummy_image_content = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b'
        dummy_image = ContentFile(dummy_image_content, name='dummy.gif')

        # 1. GeneralSetting
        if not GeneralSetting.objects.exists():
            gen = GeneralSetting.objects.create(brand_name='Lift test')
            gen.navbar_logo.save('logo.gif', dummy_image)
            gen.footer_logo.save('footer_logo.gif', dummy_image)
            self.stdout.write('GeneralSetting created.')

        # 2. HeroSection
        if not HeroSection.objects.exists():
            HeroSection.objects.create(
                mini_title_uz="Lift test - SIFAT VA ISHONCH",
                mini_title_ru="Lift test - КАЧЕСТВО И НАДЕЖНОСТЬ",
                mini_title_en="Lift test - QUALITY AND RELIABILITY",
                title_uz="BINOINGIZ UCHUN\nMUKAMMAL\nLIFTLAR",
                title_ru="СОВЕРШЕННЫЕ\nЛИФТЫ ДЛЯ\nВАШЕГО ЗДАНИЯ",
                title_en="PERFECT\nLIFTS FOR\nYOUR BUILDING",
                desc_uz="Biz O'zbekistonda eng ishonchli va zamonaviy liftlarni o'rnatish va ularga xizmat ko'rsatish bilan shug'ullanamiz.",
                desc_ru="Мы занимаемся установкой и обслуживанием самых надежных и современных лифтов в Узбекистане.",
                desc_en="We are engaged in the installation and maintenance of the most reliable and modern elevators in Uzbekistan."
            )
            self.stdout.write('HeroSection created.')

        # 3. ExperienceSection
        if not ExperienceSection.objects.exists():
            ExperienceSection.objects.create(
                mini_title_uz="TAJRIBAMIZ",
                mini_title_ru="НАШ ОПЫТ",
                mini_title_en="OUR EXPERIENCE",
                title_uz="15 YILLIK\nMUKAMMAL TAJRIBA",
                title_ru="15 ЛЕТ\nБЕЗУПРЕЧНОГО ОПЫТА",
                title_en="15 YEARS OF\nFLAWLESS EXPERIENCE",
                desc_uz="Bizning jamoamiz ko'p yillar davomida lift sanoatida yetakchi bo'lib kelmoqda.",
                desc_ru="Наша команда на протяжении многих лет является лидером лифтовой индустрии.",
                desc_en="Our team has been a leader in the elevator industry for many years."
            )
            self.stdout.write('ExperienceSection created.')

        # 4. ServiceSection
        if not ServiceSection.objects.exists():
            ServiceSection.objects.create(
                mini_title_uz="XIZMATLARIMIZ",
                mini_title_ru="НАШИ УСЛУГИ",
                mini_title_en="OUR SERVICES",
                title_uz="BIZ TAQDIM ETADIGAN\nXIZMATLAR",
                title_ru="УСЛУГИ, КОТОРЫЕ\nМЫ ПРЕДОСТАВЛЯЕМ",
                title_en="SERVICES WE\nPROVIDE",
                desc_uz="Biz liftlarni loyihalashdan tortib, ularga texnik xizmat ko'rsatishgacha bo'lgan barcha bosqichlarni qamrab olamiz.",
                desc_ru="Мы охватываем все этапы, от проектирования лифтов до их технического обслуживания.",
                desc_en="We cover all stages, from elevator design to their maintenance."
            )
            self.stdout.write('ServiceSection created.')

        # 5. GallerySection
        if not GallerySection.objects.exists():
            GallerySection.objects.create(
                mini_title_uz="GALEREYA",
                mini_title_ru="ГАЛЕРЕЯ",
                mini_title_en="GALLERY",
                title_uz="BIZNING\nLOYIHALARIMIZ",
                title_ru="НАШИ\nПРОЕКТЫ",
                title_en="OUR\nPROJECTS"
            )
            self.stdout.write('GallerySection created.')

        # 6. ContactSection
        if not ContactSection.objects.exists():
            ContactSection.objects.create(
                mini_title_uz="BOG'LANISH",
                mini_title_ru="КОНТАКТЫ",
                mini_title_en="CONTACT",
                title_uz="BIZ BILAN\nBOG'LANING",
                title_ru="СВЯЖИТЕСЬ\nС НАМИ",
                title_en="CONTACT\nWITH US",
                desc_uz="Savollaringiz bormi? Bizga yozing yoki qo'ng'iroq qiling.",
                desc_ru="Есть вопросы? Напишите нам или позвоните.",
                desc_en="Have questions? Write to us or call."
            )
            self.stdout.write('ContactSection created.')

        # Cards
        if not ExperienceCard.objects.exists():
            ExperienceCard.objects.create(
                title_uz="500+", title_ru="500+", title_en="500+",
                desc_uz="O'rnatilgan liftlar", desc_ru="Установленных лифтов", desc_en="Installed elevators"
            )
            ExperienceCard.objects.create(
                title_uz="15", title_ru="15", title_en="15",
                desc_uz="Yillik tajriba", desc_ru="Лет опыта", desc_en="Years of experience"
            )
            ExperienceCard.objects.create(
                title_uz="24/7", title_ru="24/7", title_en="24/7",
                desc_uz="Texnik xizmat", desc_ru="Техподдержка", desc_en="Technical support"
            )
            ExperienceCard.objects.create(
                title_uz="100%", title_ru="100%", title_en="100%",
                desc_uz="Mamnun mijozlar", desc_ru="Довольных клиентов", desc_en="Satisfied customers"
            )
            self.stdout.write('ExperienceCards created.')

        # 3. ServiceCard
        if not ServiceCard.objects.exists():
            s1 = ServiceCard.objects.create(
                title_uz="O'rnatish", title_ru="Установка", title_en="Installation",
                desc_uz="Barcha turdagi liftlarni sifatli o'rnatish.",
                desc_ru="Качественная установка всех видов лифтов.",
                desc_en="High-quality installation of all types of elevators."
            )
            s1.icon.save('icon1.gif', dummy_image)
            
            s2 = ServiceCard.objects.create(
                title_uz="Ta'mirlash", title_ru="Ремонт", title_en="Repair",
                desc_uz="Liftlarni tez va ishonchli ta'mirlash xizmati.",
                desc_ru="Быстрый и надежный ремонт лифтов.",
                desc_en="Fast and reliable elevator repair service."
            )
            s2.icon.save('icon2.gif', dummy_image)
            
            s3 = ServiceCard.objects.create(
                title_uz="Modernizatsiya", title_ru="Модернизация", title_en="Modernization",
                desc_uz="Eski liftlarni zamonaviy talablarga moslashtirish.",
                desc_ru="Адаптация старых лифтов под современные требования.",
                desc_en="Adapting old elevators to modern requirements."
            )
            s3.icon.save('icon3.gif', dummy_image)
            
            self.stdout.write('ServiceCards created.')

        # 4. GalleryImage
        if not GalleryImage.objects.exists():
            g1 = GalleryImage.objects.create(
                title_uz="Toshkent City", title_ru="Ташкент Сити", title_en="Tashkent City",
                desc_uz="Zamonaviy lift tizimi", desc_ru="Современная лифтовая система", desc_en="Modern elevator system"
            )
            g1.image.save('gallery1.gif', dummy_image)
            
            g2 = GalleryImage.objects.create(
                title_uz="Turar-joy majmuasi", title_ru="Жилой комплекс", title_en="Residential complex",
                desc_uz="Yevropa standarti", desc_ru="Европейский стандарт", desc_en="European standard"
            )
            g2.image.save('gallery2.gif', dummy_image)
            self.stdout.write('GalleryImages created.')

        # 5. PhoneNumber & EmailAddress
        if not PhoneNumber.objects.exists():
            PhoneNumber.objects.create(number="+998 (71) 244-87-22")
            self.stdout.write('PhoneNumber created.')

        if not EmailAddress.objects.exists():
            EmailAddress.objects.create(email="[EMAIL_ADDRESS]")
            self.stdout.write('EmailAddress created.')

        self.stdout.write(self.style.SUCCESS('Successfully seeded database'))
