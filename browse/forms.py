from django import forms
from browse.models import OrderDetails


class UpdateForm(forms.ModelForm):
    order_id = forms.CharField(disabled=True)
    notes = forms.CharField(disabled=True)

    class Meta:
        model = OrderDetails
        fields = '__all__'
