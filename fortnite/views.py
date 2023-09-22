from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def historia(request):
    data = {
        'texto1':'Epic Games presentó "Fortnite" por primera vez en 2011 en los Spike Video Game Awards. Durante varios años, el juego estuvo en desarrollo. Originalmente, se concibió como un juego de supervivencia en equipo, en el que los jugadores construían fortificaciones durante el día y defendían contra zombis por la noche.',
        'texto2':'Fortnite se lanzó oficialmente en julio de 2017 con su modo cooperativo PvE llamado "Salvar el Mundo". En este modo, los jugadores trabajan juntos para defenderse de oleadas de enemigos controlados por la IA, mientras recolectan recursos y construyen fortificaciones.',
        'texto3':'En septiembre de 2017, Epic Games lanzó el modo "Battle Royale" de Fortnite, un modo PvP gratuito para 100 jugadores. Fue influenciado por el crecimiento del género battle royale, especialmente por juegos como "PlayerUnknowns Battlegrounds" (PUBG). Sin embargo, el enfoque de Fortnite en la construcción y el estilo artístico único lo distinguieron.',
        'texto4':'Fortnite Battle Royale rápidamente se convirtió en un fenómeno. Su modelo gratuito, combinado con su disponibilidad en múltiples plataformas (incluyendo consolas, PC y dispositivos móviles) y su estilo de juego adictivo, lo convirtieron en un éxito masivo. Epic introdujo el "Pase de Batalla", una forma para que los jugadores obtengan recompensas cosméticas mientras juegan.',
        'texto5':'A lo largo de los años, Fortnite ha realizado numerosos eventos en el juego y colaboraciones con franquicias populares como Marvel, Star Wars, Stranger Things y muchos más. Estos eventos han variado desde conciertos virtuales hasta batallas épicas con villanos como Thanos.',
        'texto6':'En 2020, Epic Games desafió las políticas de la tienda de aplicaciones de Apple y Google, lo que llevó a la eliminación de Fortnite de ambas tiendas. La disputa se centró en las tarifas que estas tiendas cobran y en la decisión de Epic de introducir un sistema de pago directo.',
        'texto7':'Fortnite ha continuado evolucionando con nuevas actualizaciones, modos de juego y características. El juego ha atravesado diferentes "capítulos" y "temporadas", cada uno con su propio conjunto de cambios en el mapa, skins y mecánicas de juego.'
    }
    return render(request, 'historia.html',data)

def comoJugar(request):
    return render(request, 'comoJugar.html')

def tips(request):
    return render(request, 'tips.html')

def videos(request):
    return render(request, 'videos.html')
