from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['assignation', 'type', 'customer', 'file', 'object', 'comment', 'deadline']
        widgets = {
            'deadline': DatetimeInput(format='%Y-%m-%dT%H:%M'),
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

        # Ajout des classes
        self.fields['assignation'].widget.attrs['class'] = 'form-control selectpicker'
        self.fields['type'].widget.attrs['class'] = 'form-select'
        self.fields['customer'].widget.attrs['class'] = 'form-control selectpicker'
        self.fields['file'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['object'].widget.attrs['class'] = 'form-control'
        self.fields['comment'].widget.attrs['class'] = 'form-control'
        self.fields['deadline'].widget.attrs['class'] = 'form-control'
        # Ajout de l'attribut data-live-search
        self.fields['assignation'].widget.attrs['data-live-search'] = 'true'
        self.fields['customer'].widget.attrs['data-live-search'] = 'true'

        self.fields['assignation'].queryset = User.objects.get_bbandco_users()
