from django import forms


class searchForm(forms.Form):
    originDestination=forms.CharField(label="مبدا" ,required=True ,error_messages={"required":"لطفا مبدا را وارد کنید"}, widget=forms.TextInput(attrs={"class":"searchInput","id":"originDest"}))
    finalDestination=forms.CharField(label="مقصد",required=True,error_messages={"required":"لطفا مقصد را وارد کنید"},widget=forms.TextInput(attrs={"class":"searchInput","id":"finalDest"}))