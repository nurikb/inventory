import os
from django import forms
from .models import *
from django.core.exceptions import ValidationError

class DateInput(forms.DateInput):
    input_type = 'date'

class AdmissionForm(forms.ModelForm):
    id_type = forms.ModelChoiceField(queryset=Type.objects.all())
    upload = forms.ModelChoiceField(queryset=Upload.objects.all())
    date = forms.DateField(widget=DateInput())

    id_type.widget.attrs.update({'class': 'form-control'})
    upload.widget.attrs.update({'class': 'form-control'})
    date.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Admission
        fields = ['date', 'name', 'admission','in_stock', 'out_of_stock', 'id_type', 'upload', 'decommission']

        widgets = {

        'admission': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
        'name': forms.TextInput(attrs={'class': 'form-control'}),

        }


    def clean_in_stock(self):
        return self.cleaned_data['admission']

    def clean_decommission(self):
        return 0

    def clean_out_of_stock(self):
        return 0

class EquipmentWorkersForm(forms.ModelForm):
    id_workers = forms.ModelChoiceField(queryset=Workers.objects.all(), required=False)
    id_room = forms.ModelChoiceField(queryset=Room.objects.all())
    upload = forms.ModelChoiceField(queryset=Upload.objects.all())
    date = forms.DateField(widget=DateInput())

    id_workers.widget.attrs.update({'class': 'form-control'})
    id_room.widget.attrs.update({'class': 'form-control'})
    upload.widget.attrs.update({'class': 'form-control'})
    date.widget.attrs.update({'class': 'form-control'})


    class Meta:
        model = EquipmentWorker
        fields = ['date', 'inven_num', 'eq_name', 'id_type', 'id_workers', 'id_room', 'upload']

        readonly = ('id_type')

        widgets = {
        'inven_num': forms.TextInput(attrs={'class': 'form-control', 'id': 'demo'}),
        'id_type': forms.HiddenInput(attrs={'class': 'form-control'}),
        }

    def clean_inven_num(self):
        inven_num = self.cleaned_data['inven_num']

        if EquipmentWorker.objects.filter(inven_num__icontains=inven_num).count():
            raise ValidationError("учетная единица с таким номером уже существует")
        return inven_num

    def clean_id_type(self):
        admission_id = self.cleaned_data['eq_name']
        eq_name = admission_id.id_type
        return eq_name

class RelocationForm(forms.ModelForm):
    class Meta:
        model = Relocation
        fields = ['movereason', 'id_previous_room', 'previous_user']

        widgets = {
        'movereason': forms.TextInput(attrs={'class': 'form-control'}),

        }

class WorkersForm(forms.ModelForm):
    class Meta:
        model = Workers
        fields = ['name', 'first_name', 'last_name', 'full_name']

        widgets = {
        'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_full_name(self):
        full = self.cleaned_data['first_name']+' '+ self.cleaned_data['name']+' '+self.cleaned_data['last_name']
        return full


class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['image', 'name']

    image = forms.FileField()

    image.widget.attrs.update({'class': 'custom-file-input rounded-pill'})

    def clean_image(self):
        uploaded_file = self.cleaned_data['image']
        b=str(uploaded_file)
        x=b[:len(b)-4]
        if Upload.objects.filter(name__icontains=x).count():
            raise ValidationError("Накладная с таким названием уже существует")

        try:
            # create an ImageField instance
            im = forms.ImageField()
            # now check if the file is a valid image
            im.to_python(uploaded_file)
        except forms.ValidationError:
            # file is not a valid image;
            # so check if it's a pdf
            name, ext = os.path.splitext(uploaded_file.name)
            if ext not in ['.pdf', '.PDF']:
                raise forms.ValidationError("Разрешены только изображения и файлы PDF")
        return uploaded_file


    def clean_name(self):
        c = self.cleaned_data['name']
        if len(self.cleaned_data)>1:
            x = str(self.cleaned_data['image'])
            c = x[:len(x)-4]
            return c
