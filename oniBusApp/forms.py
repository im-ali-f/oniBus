from django import forms
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime

class searchForm(forms.Form):
    originDestination=forms.CharField(label="مبدا" ,required=True ,error_messages={"required":"لطفا مبدا را وارد کنید"}, widget=forms.TextInput(attrs={"class":"searchInput","id":"originDest"}))
    finalDestination=forms.CharField(label="مقصد",required=True,error_messages={"required":"لطفا مقصد را وارد کنید"},widget=forms.TextInput(attrs={"class":"searchInput","id":"finalDest"}))
    dateDeparture=JalaliDateField(label='تاریخ',required=True,error_messages={"required":"لطفا تاریخ را وارد کنید"},widget=AdminJalaliDateWidget(attrs={"id":"dateDeparture"}))
