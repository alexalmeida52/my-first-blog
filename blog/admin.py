from django.contrib import admin
from .models import Post

admin.site.register(Post)

# from localflavor.br.forms import BRPhoneNumberField
# class MyModelFormAdmin(forms.ModelForm):
#     fone = BRPhoneNumberField(required=False, label='fone')
#     celular = BRPhoneNumberField(required=False, label='cel')
#     class Meta:
#         model = MyModel
#   