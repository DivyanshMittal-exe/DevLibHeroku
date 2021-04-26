from django import forms
from.models import Issue,Book

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = [
            'Title',
            'BookID',
            'User',
            'DoI',
            'DoD',
            'State',
            'Comments'
        ]
        
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'Title',
            'Author',
            'Publisher',
            'Genre',
            'ISBN',
            'Location',
            'Comments'
        ]