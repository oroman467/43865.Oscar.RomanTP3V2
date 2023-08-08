from django import forms

class EquipoForm(forms.Form):
    nombre= forms.CharField(label="Nombre", max_length=50, required = True)
    tipo= forms.CharField(label="Tipo", max_length=50, required = True)
    precio = forms.IntegerField(label="Valor", required = True)
    patente = forms.CharField(label="Patente", required = True)
    serie = forms.IntegerField(label="Serie", required = True)
    ESTADO = (
        (1, "Usado"),
        (2, "Nuevo"),
    )
    estado = forms.ChoiceField(label="Estado elegido", choices=ESTADO, required=True)
    Documentacion = forms.BooleanField()

class AlquilerForm(forms.Form):
    nombre= forms.CharField(label="Nombre de equipo", max_length=50, required = True)
    tipo= forms.CharField(label="tipo de equipo", max_length=50, required = True)
    precio = forms.IntegerField(label="Precio de equipo", required = True)
   
