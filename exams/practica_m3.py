"""
Resolviendo el examen M3
"""
import biblioteca as bb

def buscar_genero(genero, lista_generos):
    pos = -1 
    i = 0
    while pos == -1 and i < len(lista_generos):
        if genero == lista_generos[i] :
            pos = i
        i = i + 1
    return pos
    
def reportar_artistas(biblioteca):
    artistas = biblioteca['artistas']    
    for llave in artistas :
        print(artistas[llave])

def crear_artista(nombre, genero, biblioteca):
    ans = False
    #artista = {'nombre': string , 'idx_genero': int, idx_discos=[]}
    if not nombre in biblioteca['artistas'] :
        lista_generos = biblioteca['generos']
        idx_genero = buscar_genero(genero, lista_generos)
        if idx_genero == -1 :
            lista_generos.append(genero)
            idx_genero = len(lista_generos) - 1
        artista = {'nombre': nombre,
                   'idx_genero': idx_genero, 
                   'idx_discos': [] }
        biblioteca['artistas'][nombre] = artista
        ans = True
    return ans


def crear_disco(nombre, fecha, artista, biblioteca):
    disco = {'nombre': nombre, 'fecha': fecha, 'idx_canciones':[]}
    biblioteca['discos'].append(disco)
    idx_disco = len(biblioteca['discos']) - 1
    lista_idx_discos = biblioteca['artistas'][artista]['idx_discos']
    lista_idx_discos.append(idx_disco)
    

def buscar_artistas_por_genero(genero, biblioteca):
    """
    la salida es una lista de nombres [strings]
    """     
    lista_nombres_artistas = []
    
    lista_generos = biblioteca['generos']
    idx = buscar_genero(genero, lista_generos)
    
    if idx != -1 :
        artistas = biblioteca['artistas']
        
        for llave in artistas :
            if artistas[llave]['idx_genero'] == idx :
                lista_nombres_artistas.append(llave)
    return lista_nombres_artistas
                
     
    
    


mi_biblioteca = bb.biblioteca
reportar_artistas(mi_biblioteca)
#ans = crear_artista('Fred Rovella', 'soft metal', mi_biblioteca)
#crear_disco('nuevo_disco', '18/05/2022', 'Nuns Honeyasfasfda', mi_biblioteca)
#reportar_artistas(mi_biblioteca)
print('*** Artistas por genero rap metal******')
nombres = buscar_artistas_por_genero('rap metal', mi_biblioteca)
print(nombres)

