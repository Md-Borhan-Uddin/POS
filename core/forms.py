from django import forms



class BaseForm(forms.Form):
    input_css = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 '
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        for field in self.visible_fields():
            field.field.widget.attrs.update({
                'class':self.input_css or '',
                'placeholder':field.label

            })
            




class BaseModalForm(forms.ModelForm):
    input_css = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'
    file_input_css = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full'
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.visible_fields():
            try:
                css = self.file_input_css if field.field.widget.input_type=='file' else self.input_css
            except:
                css = self.input_css
            field.field.widget.attrs.update({
                'class':css,
                'placeholder':field.label


            })