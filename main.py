import pygame
import json

# o que funcionou para alteraar o tamanho, era só mudar o tilepa
# Inicializa o Pygame

imagem_teste = pygame.image.load("fundo.png")
pygame.init()

# Carregar JSON do mapa
with open("map.json", "r") as file:
    map_data = json.load(file)

tile_size = map_data["tileSize"]

# Configuração da tela
screen_width = 40 * tile_size
screen_height = 30 * tile_size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Visualizador de Tilemap")

# Lista de colisões
colliders = []


# IDÉIA 1: USAR O CADA PARTE DO QUADRADO DO SPIRITESHEET, SEPARAR, E DEPENDENDO DO ID DO JSON, USAR PRA PINTAR!
def draw_layer(colliders_only=False):
    """Desenha as camadas de fundo ou colisão."""
    for layer in map_data["layers"]:
        is_collider = layer.get("collider", False)
        
        if is_collider == colliders_only:
            for tile in layer["tiles"]:
                x, y = tile["x"] * tile_size, tile["y"] * tile_size
                
                if is_collider:
                    # Adiciona ao sistema de colisão
                    colliders.append(pygame.Rect(x, y, tile_size, tile_size))
                    # Desenha a imagem de colisão
                    screen.blit(imagem_teste, (x, y), (0, 0, tile_size, tile_size))
                else:
                    # Define a cor verde para o fundo
                    color = (0, 255, 0)
                    # Desenha o retângulo do fundo
                    pygame.draw.rect(screen, color, (x, y, tile_size, tile_size))

# Configuração do jogador
player_color = (0, 0, 255)  # Azul
player_speed = 1
player_rect = pygame.Rect(50, 100, tile_size, tile_size)  # Começa na posição (50, 50)

# Loop do jogo
running = True
while running:
    screen.fill((0, 0, 0))  # Limpa a tela

    colliders.clear()  # Resetar os colliders para evitar duplicações
    draw_layer(colliders_only=False)  # Desenha o fundo primeiro
    draw_layer(colliders_only=True)   # Depois desenha as paredes

    # Captura eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimento do jogador
    keys = pygame.key.get_pressed()
    new_x, new_y = player_rect.x, player_rect.y

    if keys[pygame.K_w]:
        new_y -= player_speed
    if keys[pygame.K_s]:
        new_y += player_speed
    if keys[pygame.K_a]:
        new_x -= player_speed
    if keys[pygame.K_d]:
        new_x += player_speed

    # Criar um retângulo temporário para testar a colisão
    new_rect = pygame.Rect(new_x, new_y, tile_size, tile_size)

    # Verificar colisão antes de mover
    if not any(new_rect.colliderect(collider) for collider in colliders):
        player_rect.x = new_x
        player_rect.y = new_y

    # Desenha o jogador
    pygame.draw.rect(screen, player_color, player_rect)

    pygame.display.flip()

pygame.quit()
