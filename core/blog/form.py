from django import forms
from blog.models import Post


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            "author",
            "title",
            "content",
            "status",
            "category",
            "published_date",
        ]
