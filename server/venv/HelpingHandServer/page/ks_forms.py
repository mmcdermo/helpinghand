
from django.utils.translation import gettext as _
from django.forms import ModelForm

from models import Item
class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['targetType', 'title', 'target', 'menu']

        labels = {
        }
from models import Page
class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ['content', 'title']

        labels = {
        }
