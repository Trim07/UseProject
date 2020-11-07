from django.db import models
from django.core.validators import MaxLengthValidator
from django.db.models import SET_NULL
from Cliente.Choices import SEXO_CHOICES, TIPO_DOCUMENTO_CHOICES, STATUS_CADASTRO_CHOICES


class CadastroCliente(models.Model):

    nome_fantasia = models.CharField(
        verbose_name='Nome fantasia',
        max_length=50,
        blank=False,
        help_text="Nome fantasia da empresa. Exemplo: Lunar filtros LTDA.",
    )
    razao_social = models.CharField(
        verbose_name='Razao social',
        max_length=50,
        blank=False,
        help_text="Razão social da empresa. Exemplo: Judandir Zulu.",
    )
    cep = models.IntegerField(
        verbose_name='CEP',
        null=True,
        validators=[],
        help_text="CEP do endereço. Exemplo: 41500-000.",
    )
    rua = models.CharField(
        verbose_name='Rua',
        max_length=60,
        blank=True,
        help_text="Nome da rua. Exemplo: 2° Tv 2 de Janeiro.",
    )
    numero = models.CharField(
        verbose_name='Numero',
        blank=True,
        max_length=10,
        help_text="Numero da residencia",
    )
    complemento = models.CharField(
        verbose_name='Complemento',
        max_length=60,
        blank=True,
        help_text="Complemento de endereço. Exemplo: proximo ao MC donalds.",
    )
    bairro = models.CharField(
        verbose_name='Bairro',
        max_length=20,
        blank=True,
        help_text="Nome do bairro. Exemplo: Village.",
    )
    cidade = models.CharField(
        verbose_name='Cidade',
        max_length=20,
        blank=True,
        help_text="Nome da cidade. Exemplo:  Salvador.",
    )
    codigo_municipal = models.IntegerField(
        verbose_name='Codigo Municipal',
        null=True,
        validators=[],
        help_text="Codigo municipal. Exemplo: 1200203 (Cruzeiro do Sul).",
    )
    estado = models.CharField(
        verbose_name='Estado',
        max_length=20,
        blank=True,
        help_text="Estado. Exemplo: Bahia."
    )
    pais = models.CharField(
        verbose_name='Pais',
        max_length=20,
        blank=True,
        help_text="Nome do pais. Exemplo: Brasil"
    )
    #codigo_pais
    tipo_documento = models.CharField(
        verbose_name='Tipo do documento',
        max_length=2,
        blank=False,
        choices=TIPO_DOCUMENTO_CHOICES,
        help_text="Tipo do documento. Exemplo: Pessoa Fisica.",
    )
    identidade = models.IntegerField(
        verbose_name='Identidade',
        null=True,
        validators=[],
        help_text="Numero da identidade.",
    )
    cnpj = models.IntegerField(
        verbose_name='CNPJ',
        unique=True,
        null=True,
        validators=[],
        help_text="Numero do CNPJ.",
    )
    cpf = models.IntegerField(
        verbose_name='CPF',
        unique=True,
        null=True,
        validators=[],
        help_text="Numero do CPF.",
    )
    sexo = models.CharField(
        verbose_name='Sexo',
        max_length=3,
        blank=False,
        choices=SEXO_CHOICES,
        help_text="Sexo. Exemplo: M (Masculino).",
    )
    inscricao_estadual = models.IntegerField(
        verbose_name='Inscricao Estadual',
        unique=True,
        null=True,
        validators=[],
        help_text="Inscrição Estadual.",
    )
    inscricao_municipal = models.IntegerField(
        verbose_name='Inscricao Municipal',
        unique=True,
        null=True,
        validators=[],
        help_text="Inscricao Municipal.",
    )
    telefone_1 = models.IntegerField(
        verbose_name='Primeiro Telefone',
        null=True,
        help_text="Telefone Fixo 1. Exemplo: Exemplo (11) 1234-5678.",
    )
    telefone_2= models.IntegerField(
        verbose_name='Segundo Telefone',
        null=True,
        help_text="Telefone Fixo 2. Exemplo (11) 1234-5678.",
    )
    celular = models.IntegerField(
        verbose_name='Celular',
        null=True,
        help_text="Celular. Exemplo: (11) 12345-6789.",
    )
    email = models.CharField(
        verbose_name='Email',
        max_length=50,
        blank=True,
        help_text="Email para contato. Exemplo: cliente@dominio.com.br .",
    )
    cnae = models.CharField(
        verbose_name='CNAE',
        max_length=40,
        blank=True,
        help_text="Codigo Nacional de Atividade Economica. Exemplo: vendedor de arroz."
    )
    grupo_cliente = models.ForeignKey(
        'GrupoCliente',
        on_delete=SET_NULL,
        default="Sem Grupo",
        null=True,
        blank=True,
        help_text="Grupo em que o cliente pertence."
    )
    #data_validade_cadastro
    nascimento = models.DateField(
        verbose_name='Nascimento',
        null=True,
        validators=[],
        help_text="Data de nascimento. Exemplo: 24/04/1994"
    )
    outras_informacoes = models.TextField(
        verbose_name='Outras_informacoes',
        max_length=100,
        blank=True,
        help_text="Outras informações. Exemplo: Vende arroz"
    )
    status_cadastro = models.CharField(
        verbose_name='Status_cadastro',
        max_length=2,
        choices=STATUS_CADASTRO_CHOICES,
        blank=False,
        help_text="Status do cadastro do cliente. Exemplo: Ativo"
    )

    def __str__(self):
        return f'Razao Social {self.razao_social} | ' \
               f'Nome Fantasia{self.nome_fantasia} | ' \
               f'CNAE {self.cnae}'


class GrupoCliente(models.Model):

    nome_grupo = models.CharField(
        verbose_name='Nome_Grupo',
        max_length=30,
        blank=False,
        help_text="Nome do grupo. Exemplo: Caixa."
    )
    descricao = models.TextField(
        verbose_name='Descricao',
        max_length=200,
        blank=True,
        help_text="Descricao do grupo. Exemplo: Vendem arroz."
    )

    def __str__(self):
        return self.nome_grupo

