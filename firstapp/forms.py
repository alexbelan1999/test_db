from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя", initial="undefined",help_text="Введите своё имя", required=True, min_length=2,max_length=15)
    age = forms.IntegerField(label="Возраст", initial=18,help_text="Введите свой возраст",required=True, min_value=1,max_value=100)
    email = forms.EmailField(label="Email",help_text="Введите свой почтовый адрес",required=False, min_length=7)
    comment = forms.CharField(label="Комментарий", widget=forms.Textarea,help_text="Оставьте комментарий",required=False)
    field_order = ["name","age","email","comment"]
