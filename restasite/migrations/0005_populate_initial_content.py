from django.db import migrations

def populate_initial_content(apps, schema_editor):
    TextContent = apps.get_model('restasite', 'TextContent')
    Address = apps.get_model('restasite', 'Address')

    # About page content
    TextContent.objects.create(
        key='about_title',
        content='О нас',
        description='About page title'
    )
    TextContent.objects.create(
        key='about_subtitle',
        content='Уютное место для ваших завтраков, обедов и ужинов',
        description='About page subtitle'
    )
    TextContent.objects.create(
        key='about_description',
        content='Ресторан вобрал в себя лучшие традиции европейской и средиземноморской кухни.Уютная, доброжелательная атмосфера и достойный сервис  - это основные преимущества ресторана. Все вышеперечисленное и плюс доступный уровень цен позволили заведению оказаться в списке лучших ресторанов  Киева. Секрет популярности прост - побывав здесь однажды и ощутив радушие и гостеприимство, теплый прием и заботливое обслуживание, гости непременно возвращаются вновь и рекомендуют своим друзьям.',
        description='About page main description'
    )

    # Index page content
    TextContent.objects.create(
        key='slider_title',
        content='Свежая и вкусная еда<br />Для вашего здоровья',
        description='Slider title'
    )
    TextContent.objects.create(
        key='about_section_title',
        content='Жизнь слишком коротка, чтобы есть невкусную еду',
        description='About section title on index page'
    )
    TextContent.objects.create(
        key='about_section_description',
        content='Добро пожаловать в мир вкусной еды...',
        description='About section description'
    )

    # Contact information
    TextContent.objects.create(
        key='contact_phone',
        content='+380 96 084 1234',
        description='Contact phone number'
    )
    TextContent.objects.create(
        key='contact_email',
        content='manager@example.com',
        description='Contact email'
    )

    # Addresses
    Address.objects.create(
        city='Киев',
        street='бул. Леси украинки',
        building='д.6',
        order=1
    )
    Address.objects.create(
        city='Тернополь',
        street='бул. Леси украинки',
        building='д.5',
        order=2
    )
    Address.objects.create(
        city='Одесса',
        street='бул. Леси украинки',
        building='д.5',
        order=3
    )

    # Add this to your populate_initial_content function
    TextContent.objects.create(
        key='contacts_title',
        content='Контакты',
        description='Contacts page title'
    )

def reverse_migration(apps, schema_editor):
    TextContent = apps.get_model('restasite', 'TextContent')
    Address = apps.get_model('restasite', 'Address')
    TextContent.objects.all().delete()
    Address.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('restasite', '0004_textcontent_address'),  # Updated to depend on the model migration
    ]

    operations = [
        migrations.RunPython(populate_initial_content, reverse_migration),
    ] 