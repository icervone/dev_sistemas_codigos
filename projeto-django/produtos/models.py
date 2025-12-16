from django.db import models

class Usuario(models.Model):
    
    nome = models.CharField(max_length=80,
                    verbose_name='Nome',
                    help_text='Nome do produto',
                    null=False)
    email = models.EmailField(unique=True, 
                    verbose_name='Preço',
                    help_text='Preço do produto',
                    null=False)
    senha = models.CharField(max_length=255,
                    verbose_name='Marca',
                    help_text='Marca do produto',
                    null=False)
    criado = models.DateTimeField(auto_now_add=True,
                    verbose_name='Criado em')
    atualizado = models.DateTimeField(auto_now=True,
                    verbose_name='Atualizado em')
    
    class Meta:
        # nome da tabela
        db_table = 'usuarios'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['nome'] #ordena por nome (ordem alfabetica)
        # se fosse por data de criação
        # ordering = ['-criado'] 
        # ordem do mais recente (decrescente)
    
    def __repr__(self):
        """
        Retorna uma string representativa do objeto, no formato
        "<nome>".
        """
        return f'<Usuario {self.nome}>'
    
    def __str__(self):
        """
        Retorna uma string representativa do objeto, no formato
        "<nome> (<email>)".
        """
        return f'{self.nome} ({self.email})'

    def verificar_senha(self, senha_texto):
        return check_password(senha_texto, self.senha)
        # a primeira senha é sempre a digitada no momento
        # a segunda senha vem do banco de dados

    def save(self, *args, **kwargs):
        # args = argumentos posicionais
        # kwargs = argumentos nomeados
        if self.senha and not \
        self.senha.startswith('pbkdf2_sha256'):
            # se a senha for alterada
            self.senha = make_password(self.senha)
        # se a senha for criada ou atualizada
        # chama o save da superclasse
        super().save(*args, **kwargs)

# criar a verificação se o usuário está autenticado
# Isso faz com que qualquer instancia (objeto) desse
# modelo seja considerada autenticada pelo Django

@property
def is_authenticated(self):
    '''
    Retorna True sempre, pois objetos (usuario) só existem
    se autenticados
    '''
    return True

@property
def is_anonymous(self):
    '''
    Retorna False sempre, pois não aceita objeto (usuario)
    anonimo
    Isso infrma ao Django que esse objeto não é do tipo
    especial "AnonymousUser" (que representa usuários não
    logados)
    '''
    return False
