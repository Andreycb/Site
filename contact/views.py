from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import ContactForm
from django.http import HttpResponseRedirect
# Create your views here.

def contact(request):
    send = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        comment = request.POST.get('comment', '')
        email = EmailMessage(
            "Mensagem do Blog",
            "De {} <{}> Escreveu:\n\n{}".format(name, email, comment),
            "nao-responder@inbox.mailtrap.ioW",
            ['andreycunha08@gmail.com'],
            reply_to=[email]
        )
        try:
            email.send()
            send = True
            form = ContactForm()
        except:
             send = False

    context = {
        'form': form,
        'success': send
    }
    return render(request, 'contact/contact.html', context)
