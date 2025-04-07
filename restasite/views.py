from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import get_template

from restasite.forms import ContactForm
from restasite.models import MenuItem, TextContent, Address


def get_common_context():
    """Get content used across multiple pages"""
    addresses = Address.objects.all().order_by('order')
    return {
        'contact_phone': TextContent.objects.get(key='contact_phone').content,
        'contact_email': TextContent.objects.get(key='contact_email').content,
        'addresses': addresses,
    }


def index(request):
    context = {
        'slider_title': TextContent.objects.get(key='slider_title').content,
        'about_section_title': TextContent.objects.get(key='about_section_title').content,
        'about_section_description': TextContent.objects.get(key='about_section_description').content,
        'menu_din': MenuItem.objects.filter(type='DIN'),
        'menu_brk': MenuItem.objects.filter(type='BRK'),
        'menu_lun': MenuItem.objects.filter(type='LUN'),
        **get_common_context()
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'title': TextContent.objects.get(key='about_title').content,
        'subtitle': TextContent.objects.get(key='about_subtitle').content,
        'description': TextContent.objects.get(key='about_description').content,
        **get_common_context()
    }
    return render(request, 'about.html', context)


def contacts(request):
    try:
        title = TextContent.objects.get(key='contacts_title').content
    except TextContent.DoesNotExist:
        title = 'Контакты'  # Default fallback
        
    context = {
        'title': title,
        **get_common_context()
    }
    return render(request, 'contacts.html', context)


def send_message(name, email, message):
    text = get_template('message.html')
    html = get_template('message.html')
    context = {'name': name, 'email': email, 'message': message}
    subject = 'Сообщение от пользователя'
    from_email = 'from@example.com'
    text_content = text.render(context)
    html_content = html.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['manager@example.com'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
