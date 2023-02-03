from django import forms
from .models import Post
from users.models import User

# ModelForm, Form


class PostModelForm(forms.ModelForm):

    title = forms.CharField(
        label="Заголовок", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    body = forms.CharField(
        label="Тело поста", widget=forms.Textarea(attrs={"class": "form-control"})
    )
    autor = forms.ModelChoiceField(
        label="Имя автора",
        queryset=User.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Post
        fields = ("title", "body", "autor")
