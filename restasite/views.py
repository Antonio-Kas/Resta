from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import get_template

from restasite.forms import ContactForm
from restasite.models import MenuItem


def index(request):
    menu_brk = MenuItem.objects.filter(type__exact='BRK').order_by('?')[:6]
    menu_lun = MenuItem.objects.filter(type__exact='LUN').order_by('?')[:6]
    menu_din = MenuItem.objects.filter(type__exact='DIN').order_by('?')[:6]
    context = {'menu_brk': menu_brk, 'menu_lun': menu_lun, 'menu_din': menu_din}
    return render(
        request,
        'index.html',
        context=context
    )


def about(request):
    return render(
        request,
        'about.html'
    )


def contacts(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message'])
            context = {'success': 1}
    else:
        form = ContactForm()
    context['form'] = form
    return render(
        request,
        'contacts.html',
        context=context
    )


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
