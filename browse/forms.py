from django import forms
from browse.models import OrderDetails


class UpdateForm(forms.ModelForm):

    class Meta:
        model = OrderDetails
        fields = '__all__'
