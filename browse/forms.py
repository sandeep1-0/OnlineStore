from django import forms
from browse.models import OrderDetails


class UpdateForm(forms.ModelForm):
    order_id = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'readonly':'readonly'}))
    notes = forms.CharField(disabled=True)

    class Meta:
        model = OrderDetails
        fields = '__all__'
