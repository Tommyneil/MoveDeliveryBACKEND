from django.contrib import admin

# Register your models here.

from .models import Veiculo
from .models import Frete
from .models import Cliente
from .models import Depoimento
from .models import Carga
from .models import Duvida
from .models import Endereco
from .models import Estado
from .models import Cidade
from .models import Bairro

admin.site.register (Veiculo)
admin.site.register (Frete)
admin.site.register (Cliente)
admin.site.register (Depoimento)
admin.site.register (Carga)
admin.site.register (Duvida)
admin.site.register (Endereco)
admin.site.register (Estado)
admin.site.register (Cidade)
admin.site.register (Bairro)
