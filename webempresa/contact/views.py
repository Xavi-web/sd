from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):  
    #print ("tipo peticion:",request.method)
    contact_form= ContactForm()  # "plantilla" vacia
    if request.method=='POST':  # si llega algo rellenamos la plantilla
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid()==True:
            name=request.POST.get('name','')   # recogemos los datos
            email=request.POST.get('email','')
            content=request.POST.get('content','')
            # enviarmos correo y redireccionamos
            asunto="Sinergidata - Contacto web"
            cuerpo="De {} <{}>\n\nEscribió:\n\n{}".format(name,email,content)
            desde="No-Contestar@inbox.mailtrap.io"
            para=["mailxavis@gmail.com"]  # es una lista
            responder=[email] # es una lista
            email= EmailMessage(
                asunto,
                cuerpo,
                desde,
                para,
                reply_to=responder
            )

            try:
                email.send()
                return redirect(reverse ('contact')+"?ok" )  # reverse es como el url
                print ("Mail enviado",para,cuerpo)
            except:
                return redirect(reverse ('contact')+"?fail" )  
                print ("Mail Error, no enviado",para,cuerpo)

          



    return render(request,"contact/contact.html", {'formu':contact_form} )