from django import forms
from django.core import validators
from django.forms import ModelForm, Textarea
from pykickstart.i18n import _
from Cliente.Choices import STATUS_CADASTRO_CHOICES, TIPO_DOCUMENTO_CHOICES, SEXO_CHOICES
from .models import GrupoCliente, CadastroCliente


"""class CadastrarClienteForms(forms.Form):

    nome_fantasia = forms.CharField(
        label='Nome fantasia',
        max_length=50,
    )
    razao_social = forms.CharField(
        label='Razao social',
        max_length=50,
    )
    cep = forms.IntegerField(
        label='CEP',
    )
    rua = forms.CharField(
        label='Rua',
        max_length=60,
    )
    numero = forms.CharField(
        label='Numero',
        max_length=10,
    )
    complemento = forms.CharField(
        label='Complemento',
        max_length=60,
    )
    bairro = forms.CharField(
        label='Bairro',
        max_length=20,
    )
    cidade = forms.CharField(
        label='Cidade',
        max_length=20,
    )
    codigo_municipal = forms.IntegerField(
        label='Codigo Municipal',

    )
    estado = forms.CharField(
        label='Estado',
        max_length=20,
    )
    pais = forms.CharField(
        label='Pais',
        max_length=20,
    )
    tipo_documento = forms.ChoiceField(
        label='Tipo do documento',
        choices=TIPO_DOCUMENTO_CHOICES,

    )
    identidade = forms.IntegerField(
        label='Identidade',

    )
    cnpj = forms.IntegerField(
        label='CNPJ',

    )
    cpf = forms.IntegerField(
        label='CPF',

    )
    sexo = forms.ChoiceField(
        label='Sexo',
        choices=SEXO_CHOICES
    )
    inscricao_estadual = forms.IntegerField(
        label='Inscricao Estadual',

    )
    inscricao_municipal = forms.IntegerField(
        label='Inscricao Municipal',

    )
    telefone_1 = forms.IntegerField(
        label='Telefone1',
    )
    telefone_2 = forms.IntegerField(
        label='Telefone2',
    )
    celular = forms.IntegerField(
        label='Celular',
    )
    email = forms.CharField(
        label='Email',
        max_length=50,
        validators=[validators.validate_email],
    )
    cnae = forms.CharField(
        label='CNAE',
        max_length=40,
    )
    grupo_cliente = forms.ModelMultipleChoiceField(
        label='Grupo do cliente',
        widget=forms.CheckboxSelectMultiple,
        queryset=GrupoCliente.objects.only('nome_grupo'),

    )
    nascimento = forms.DateField(
        label='Nascimento',
        widget=forms.TextInput(attrs={'class': 'abc'})

    )
    outras_informacoes = forms.CharField(
        label='Outras_informacoes',
        max_length=100,
        widget=forms.Textarea
    )
    status_cadastro = forms.CharField(
        label='Status_cadastro',
        max_length=2,
        widget=forms.Select(choices=STATUS_CADASTRO_CHOICES),
    )
"""


class CadastrarClienteForms(ModelForm):
    class Meta:
        model = CadastroCliente
        fields = ['nome_fantasia',
                  'razao_social',
                  'cep',
                  'rua',
                  'numero',
                  'complemento',
                  'bairro',
                  'cidade',
                  'codigo_municipal',
                  'estado',
                  'pais',
                  'tipo_documento',
                  'identidade',
                  'cnpj',
                  'cpf',
                  'sexo',
                  'inscricao_municipal',
                  'inscricao_estadual',
                  'telefone_1',
                  'telefone_2',
                  'celular',
                  'email',
                  'cnae',
                  'grupo_cliente',
                  'nascimento',
                  'outras_informacoes',
                  'status_cadastro',
                  ]
        required = (
            'nome_fantasia',
            'razao_social',
            'cep',
        )
        labels = {
            'nome_fantasia': _('Nome fantasia da empresa')
        }


class CadastrarGrupoClienteForms(ModelForm):
    class Meta:
        model = GrupoCliente
        fields = ['nome_grupo', 'descricao']
        required = (
            'nome_grupo',
        )
        widgets = {
            'descricao': Textarea(attrs={'cols': 50, 'rows': 20}),
            'nome_grupo': forms.TextInput(attrs={'class': 'abc'})
        }
        labels = {
            'nome_grupo': _('Nome do grupo'),
        }
        error_messages = {
            'nome_grupo': {
                'max_length': _('Valor maximo e caracteres atingidos.')
            },
            'descricao': {
                'max_length': _('Valor maximo e caracteres atingidos.')
            }
        }