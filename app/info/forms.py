from django import forms 
from .models import Employees

class CreateEmployess(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ("name","age","position","office","startdate","salary")
        labels = {
            }
        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control"}),
            "age": forms.TextInput(attrs={"class":"form-control"}),
            "position": forms.Select(attrs={"class":"form-control"}),
            "office": forms.TextInput(attrs={"class":"form-control"}),
            "startdate": forms.TextInput(attrs={"class":"form-control"}),
            "salary": forms.TextInput(attrs={"class":"form-control"}),
            }
        

class EditEmployess(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ("name","age","position","office","startdate","salary")
        labels = {
            }
        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control"}),
            "age": forms.TextInput(attrs={"class":"form-control"}),
            "position": forms.Select(attrs={"class":"form-control"}),
            "office": forms.TextInput(attrs={"class":"form-control"}),
            "startdate": forms.TextInput(attrs={"class":"form-control"}),
            "salary": forms.TextInput(attrs={"class":"form-control"}),
            }        
