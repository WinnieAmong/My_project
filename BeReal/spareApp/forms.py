#handling form to be displayed to the users
from django.forms import ModelForm
from.models import *
#from


#handles a form that the user will use to add stock bought
class AddForm(ModelForm):#worker will edit/add received quantity here
    class Meta:
        model = Product
        fields =[
            'received_quantity'
        ]


class SaleForm(ModelForm):
    class Meta:
         model = Sale
         fields = [
             'quantity','amount_received','buyer_names','branch','buyer_contact','date_of_purchase',
         ]