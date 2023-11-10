from django.db import models

class EntryManager(models.Manager):
    """procedimiento para entrada"""

    def entrada_en_portada(self):
        return self.filter(
            public=True,
            portada=True,
        ).order_by('-created').first()
    
    def entradas_en_home(self):
        #Devuelve sus ultimas 4 entradas en home
        return self.filter(
            public=True,
            in_home=True,
        ).order_by('-created')[:4] # Retorna los primeros 4 recordemos que ya esta ordenado desde los ultimos. 
    
    def entradas_recientes(self):
        #Devuelve sus ultimas 6 entradas recientes
        return self.filter(
            public=True,
        ).order_by('-created')[:6] # Retorna los primeros 4 recordemos que ya esta ordenado desde los ultimos. 
    
    def buscar_entrada(self, kword, categoria):
        # procedimiento para buscar entradas por categoria o palabra clave
        if len(categoria) > 0:
            return self.filter(
                category__short_name=categoria,
                title__icontains=kword,
                public=True
            ).order_by('-created')
        
        else:
            return self.filter(
                title__icontains=kword,
                public=True
            ).order_by('-created')
        
        



