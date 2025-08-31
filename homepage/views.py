from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings


# Create your views here.

def homepageView(req):

    if req.method == "POST":

        phone = req.POST['phone']
        sender = req.POST['email']

        print('Telefon je:'+ phone)
        print ('Email je: ' + sender)

        message = f"{req.POST['name']} má zájem o tvé služby. \n\n Telefon na něj je {req.POST['phone']} \n\n Lokalita: {req.POST['place']} \n\n Má zájem o: {req.POST['desc']}." 

        EmailMessage(
        subject=f"Kontakt z webu – {req.POST['name']}",
        body=f"Jméno: {req.POST['name']}\nE-mail: {req.POST['email']}\n\nZpráva:\n{message}",
        from_email=settings.DEFAULT_FROM_EMAIL,   # musí být tvoje @seznam.cz
        to=[settings.DEFAULT_FROM_EMAIL],
        reply_to=["bushman@seznam.cz",],
        ).send()

    
        # return redirect("success")  # přesměrování po odeslání

    content={}
    return render (req, 'homepage/homepage.html', content)