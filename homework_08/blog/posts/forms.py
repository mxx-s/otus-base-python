from django import forms
from .models import Post, Comment
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


class CommentModelForm(forms.ModelForm):
    body=forms.CharField(label="Введите комментарий:", widget=forms.Textarea(attrs={"class":"form-control"}))
    post=forms.ModelChoiceField(label='Номер поста', queryset=Post.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    author=forms.ModelChoiceField(label='Автор поста', queryset=User.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Comment
        fields = ('body', 'post', 'author')