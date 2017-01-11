from django import forms
from django.forms.extras.widgets import SelectDateWidget
#from django.forms import extras

#from django.db import SelectDateWidget
#from SelectDate.widgets import SelectDateWidget
from pagedown.widgets import PagedownWidget

from .models import Post
#from .models import datetime
class PostForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget(show_preview=False))
    widget = forms.extras.widgets.SelectDateWidget()
#publish = forms.DateField(widget=forms.SelectDateWidget)
    #publish = forms.DateField(widget=SelectDateWidget, initial=datetime.date.today())
    #widgets = {
     #   'publish': SelectDateWidget(),
    #}
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
            "draft",
            "publish",
        ]
       # widgets = #{
            
           # 'publish': widgets.SelectDateWidget(required=True),
        #}
   # widgets = {
    #  'publish': SelectDateWidget()}
    