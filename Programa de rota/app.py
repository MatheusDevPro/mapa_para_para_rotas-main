import folium
import openrouteservice

# Configurar a chave de API
API_KEY = '5b3ce3597851110001cf6248868901d91f6c4c89b20a7a8027bba612'

# Coordenadas das capitais brasileiras (estado -> (latitude, longitude))
capitais_brasil = {
    'Acre': (-8.7742, -68.1893),
    'Alagoas': (-9.6658, -35.7354),
    'Amapá': (0.0396, -51.0704),
    'Amazonas': (-3.1190, -60.2170),
    'Bahia': (-12.9714, -38.5014),
    'Ceará': (-3.7172, -38.5437),
    'Espírito Santo': (-20.3155, -40.3128),
    'Goiás': (-16.6869, -49.2643),
    'Maranhão': (-2.5396, -44.2828),
    'Mato Grosso': (-15.6010, -56.0979),
    'Mato Grosso do Sul': (-20.4697, -54.6201),
    'Minas Gerais': (-19.8157, -43.9542),
    'Pará': (-1.4558, -48.4902),
    'Paraíba': (-7.1152, -34.8610),
    'Paraná': (-25.4284, -49.2733),
    'Pernambuco': (-8.0476, -34.8770),
    'Piauí': (-5.0917, -42.8034),
    'Rio de Janeiro': (-22.9068, -43.1729),
    'Rio Grande do Norte': (-5.7945, -35.2110),
    'Rio Grande do Sul': (-30.0346, -51.2177),
    'Rondônia': (-8.7608, -63.9039),
    'Roraima': (2.8193, -60.6731),
    'Santa Catarina': (-27.5954, -48.5480),
    'São Paulo': (-23.5505, -46.6333),
    'Sergipe': (-10.9472, -37.0731),
    'Tocantins': (-10.1896, -48.3342)
}

# Criar cliente do OpenRouteService
client = openrouteservice.Client(key=API_KEY)

# Criar mapa centralizado no Brasil
mapa = folium.Map(location=[-15, -55], zoom_start=4)

# Adicionar marcadores para todas as capitais
for estado, coordenadas in capitais_brasil.items():
    folium.Marker(coordenadas, tooltip=estado).add_to(mapa)

# Solicitar rota entre duas capitais de exemplo (São Paulo e Rio de Janeiro)
origem = capitais_brasil['São Paulo']
destino = capitais_brasil['Rio de Janeiro']

# Solicitar a rota
rota = client.directions(
    coordinates=[origem[::-1], destino[::-1]],
    profile='driving-car',  # Pode ser 'walking', 'cycling', etc.
    format='geojson'
)

# Extraindo informações da rota
distancia = rota['routes'][0]['summary']['distance'] / 1000  # Em km
duracao = rota['routes'][0]['summary']['duration'] / 60  # Em minutos
coordenadas_rota = rota['routes'][0]['geometry']

print(f"Distância entre São Paulo e Rio de Janeiro: {distancia:.2f} km")
print(f"Duração: {duracao:.2f} minutos")

# Adicionar a rota ao mapa
folium.GeoJson(coordenadas_rota).add_to(mapa)

# Salvar mapa como arquivo HTML
mapa.save("mapa_brasil_com_estados_e_rota.html")

print("Mapa gerado e salvo como 'mapa_brasil_com_estados_e_rota.html'.")
