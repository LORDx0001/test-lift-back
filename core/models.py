from django.db import models

class GeneralSetting(models.Model):
    brand_name = models.CharField(max_length=255, default="Lift test", verbose_name="Название бренда (Текст)")
    navbar_logo = models.ImageField(upload_to="logos/", blank=True, null=True, verbose_name="Логотип Navbar")
    footer_logo = models.ImageField(upload_to="logos/", blank=True, null=True, verbose_name="Логотип Footer")
    
    class Meta:
        verbose_name = "Общие настройки"
        verbose_name_plural = "Общие настройки"

    def __str__(self):
        return "Общие настройки"

class HeroSection(models.Model):
    hero_bg = models.ImageField(upload_to="hero/", blank=True, null=True, verbose_name="Фон Hero (Image)")
    mini_title_uz = models.CharField(max_length=255, blank=True, verbose_name="Mini Title (UZ)")
    mini_title_ru = models.CharField(max_length=255, blank=True, verbose_name="Mini Title (RU)")
    mini_title_en = models.CharField(max_length=255, blank=True, verbose_name="Mini Title (EN)")
    
    title_uz = models.TextField(blank=True, verbose_name="Title (UZ)")
    title_ru = models.TextField(blank=True, verbose_name="Title (RU)")
    title_en = models.TextField(blank=True, verbose_name="Title (EN)")
    
    desc_uz = models.TextField(blank=True, verbose_name="Desc (UZ)")
    desc_ru = models.TextField(blank=True, verbose_name="Desc (RU)")
    desc_en = models.TextField(blank=True, verbose_name="Desc (EN)")

    class Meta:
        verbose_name = "Секция Hero"
        verbose_name_plural = "Секция Hero"

    def __str__(self):
        return "Настройки Hero"

class ExperienceSection(models.Model):
    mini_title_uz = models.CharField(max_length=255, blank=True, verbose_name="Mini Title (UZ)")
    mini_title_ru = models.CharField(max_length=255, blank=True, verbose_name="Mini Title (RU)")
    mini_title_en = models.CharField(max_length=255, blank=True, verbose_name="Mini Title (EN)")
    
    title_uz = models.TextField(blank=True, verbose_name="Title (UZ)")
    title_ru = models.TextField(blank=True, verbose_name="Title (RU)")
    title_en = models.TextField(blank=True, verbose_name="Title (EN)")
    
    desc_uz = models.TextField(blank=True, verbose_name="Desc (UZ)")
    desc_ru = models.TextField(blank=True, verbose_name="Desc (RU)")
    desc_en = models.TextField(blank=True, verbose_name="Desc (EN)")

    class Meta:
        verbose_name = "Секция Experience"
        verbose_name_plural = "Секция Experience"

    def __str__(self):
        return "Настройки Experience"

class ServiceSection(models.Model):
    mini_title_uz = models.CharField(max_length=255, blank=True, verbose_name="Mini Title (UZ)")
    mini_title_ru = models.CharField(max_length=255, blank=True, verbose_name="Mini Title (RU)")
    mini_title_en = models.CharField(max_length=255, blank=True, verbose_name="Mini Title (EN)")
    
    title_uz = models.TextField(blank=True, verbose_name="Title (UZ)")
    title_ru = models.TextField(blank=True, verbose_name="Title (RU)")
    title_en = models.TextField(blank=True, verbose_name="Title (EN)")
    
    desc_uz = models.TextField(blank=True, verbose_name="Desc (UZ)")
    desc_ru = models.TextField(blank=True, verbose_name="Desc (RU)")
    desc_en = models.TextField(blank=True, verbose_name="Desc (EN)")

    class Meta:
        verbose_name = "Секция Services"
        verbose_name_plural = "Секция Services"

    def __str__(self):
        return "Настройки Services"

class GallerySection(models.Model):
    mini_title_uz = models.CharField(max_length=255, blank=True, verbose_name="Mini Title (UZ)")
    mini_title_ru = models.CharField(max_length=255, blank=True, verbose_name="Mini Title (RU)")
    mini_title_en = models.CharField(max_length=255, blank=True, verbose_name="Mini Title (EN)")
    
    title_uz = models.TextField(blank=True, verbose_name="Title (UZ)")
    title_ru = models.TextField(blank=True, verbose_name="Title (RU)")
    title_en = models.TextField(blank=True, verbose_name="Title (EN)")

    class Meta:
        verbose_name = "Секция Gallery"
        verbose_name_plural = "Секция Gallery"

    def __str__(self):
        return "Настройки Gallery"

class ContactSection(models.Model):
    mini_title_uz = models.CharField(max_length=255, blank=True, verbose_name="Mini Title (UZ)")
    mini_title_ru = models.CharField(max_length=255, blank=True, verbose_name="Mini Title (RU)")
    mini_title_en = models.CharField(max_length=255, blank=True, verbose_name="Mini Title (EN)")
    
    title_uz = models.TextField(blank=True, verbose_name="Title (UZ)")
    title_ru = models.TextField(blank=True, verbose_name="Title (RU)")
    title_en = models.TextField(blank=True, verbose_name="Title (EN)")
    
    desc_uz = models.TextField(blank=True, verbose_name="Desc (UZ)")
    desc_ru = models.TextField(blank=True, verbose_name="Desc (RU)")
    desc_en = models.TextField(blank=True, verbose_name="Desc (EN)")

    class Meta:
        verbose_name = "Секция Contact"
        verbose_name_plural = "Секция Contact"

    def __str__(self):
        return "Настройки Contact"

class ExperienceCard(models.Model):
    title_uz = models.CharField(max_length=255, verbose_name="Заголовок (UZ)")
    title_ru = models.CharField(max_length=255, verbose_name="Заголовок (RU)")
    title_en = models.CharField(max_length=255, verbose_name="Заголовок (EN)")
    desc_uz = models.TextField(verbose_name="Описание (UZ)")
    desc_ru = models.TextField(verbose_name="Описание (RU)")
    desc_en = models.TextField(verbose_name="Описание (EN)")

    class Meta:
        verbose_name = "Карточка Experience"
        verbose_name_plural = "Карточки Experience"

    def __str__(self):
        return self.title_ru

class ServiceCard(models.Model):
    icon = models.ImageField(upload_to="services/", verbose_name="Иконка (Image)")
    title_uz = models.CharField(max_length=255, verbose_name="Заголовок (UZ)")
    title_ru = models.CharField(max_length=255, verbose_name="Заголовок (RU)")
    title_en = models.CharField(max_length=255, verbose_name="Заголовок (EN)")
    desc_uz = models.TextField(verbose_name="Описание (UZ)")
    desc_ru = models.TextField(verbose_name="Описание (RU)")
    desc_en = models.TextField(verbose_name="Описание (EN)")

    class Meta:
        verbose_name = "Карточка Услуги"
        verbose_name_plural = "Карточки Услуг"

    def __str__(self):
        return self.title_ru

class GalleryImage(models.Model):
    image = models.ImageField(upload_to="gallery/", verbose_name="Картинка (Image)")
    title_uz = models.CharField(max_length=255, verbose_name="Заголовок (UZ)")
    title_ru = models.CharField(max_length=255, verbose_name="Заголовок (RU)")
    title_en = models.CharField(max_length=255, verbose_name="Заголовок (EN)")
    desc_uz = models.TextField(blank=True, verbose_name="Описание (UZ)")
    desc_ru = models.TextField(blank=True, verbose_name="Описание (RU)")
    desc_en = models.TextField(blank=True, verbose_name="Описание (EN)")

    class Meta:
        verbose_name = "Карточка Галереи"
        verbose_name_plural = "Карточки Галереи"

    def __str__(self):
        return self.title_ru


from django.core.validators import RegexValidator

class ContactRequest(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    name = models.CharField(max_length=255, verbose_name="Имя")
    phone = models.CharField(validators=[phone_regex], max_length=50, verbose_name="Телефон")
    details = models.TextField(verbose_name="Детали", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"{self.name} - {self.phone}"

class PhoneNumber(models.Model):
    number = models.CharField(max_length=255, verbose_name="Номер телефона")

    class Meta:
        verbose_name = "Номер телефона"
        verbose_name_plural = "Номера телефонов"

    def __str__(self):
        return self.number

class EmailAddress(models.Model):
    email = models.EmailField(max_length=255, verbose_name="Email")

    class Meta:
        verbose_name = "Email адрес"
        verbose_name_plural = "Email адреса"

    def __str__(self):
        return self.email
