from django import forms


from sport_news.models import Contact, Order

class Contact_Form(forms.ModelForm):
    class Meta:
        model = Contact
        fields =  ['name','e_mail','message_type','message']

class Order_Form(forms.ModelForm):
    class Meta:
        model = Order
        readonly_field = ['']
        fields =  ['product','size','count']
        