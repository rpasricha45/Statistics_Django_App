from django import forms


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label="Select a File",
        help_text="Max. 42 megabytes"
    )
