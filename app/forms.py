from django import forms
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        template = get_template('contact_template.txt')

        context = dict({'name': name,
                        'email': email,
                        'subject': subject,
                        'message': message,
                     })
        content = template.render(context)

        email = EmailMessage(
            "New contact form submission",
            content,
            "Website Title" + ' ',
            ['ch.hammad.shaukat@gmail.com'],
            headers={'Reply-To': email}
        )
        email.send()
        return redirect('app:index_view')



