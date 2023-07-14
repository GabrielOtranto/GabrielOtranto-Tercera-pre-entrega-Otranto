from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    description=forms.CharField(label="descripcion de la tarea", widget=forms.Textarea(attrs={'class': 'input'}))
    

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del Proyect", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))


class registro(forms.Form):
    user = forms.CharField(label= "Nombre de Usuario", max_length= 20)
    mail = forms.CharField(label= "Mail", max_length= 20)
    pwd = forms.CharField(label= "Contraseña", max_length= 20)
    pwd2 = forms.CharField(label= "Confirmar contraseña", max_length= 20)


class cosmetico(forms.Form):
    titulo = forms.CharField(label= "Buscar cosmetico", max_length= 200)
    descripcion = forms.Textarea()
   