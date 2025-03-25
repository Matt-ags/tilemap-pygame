# 🎮 Visualizador de Tilemap no Pygame

> Este projeto é um sistema de mapas baseado em JSON para o Pygame, permitindo a criação de múltiplas camadas com diferentes tipos de blocos, incluindo colisões e terrenos variados.

<details>
  <summary><h2>💻 Explicando o código Python</h2></summary>
  
  ## 1. Carregar o mapa de um arquivo JSON

  ```python
  with open("map.json", "r") as file:
      map_data = json.load(file)
  
  tile_size = map_data["tileSize"]
  ```
  - O mapa é lido de um arquivo map.json, que contém informações como o tamanho dos tiles (tileSize) e as camadas (layers).
  
  - O tile_size define o tamanho dos blocos (tiles) no jogo.

  ## 2. Criar tela

  ```python
  screen_width = 40 * tile_size
  screen_height = 30 * tile_size
  screen = pygame.display.set_mode((screen_width, screen_height))
  pygame.display.set_caption("Visualizador de Tilemap")
  ```
  - A tela do jogo é criada com dimensões baseadas na grade do mapa (40x30 tiles).

  ## 3. Função para desenhar o mapa
  
  ```python
  def draw_layer(colliders_only=False):
      """Desenha as camadas de fundo ou colisão."""
      for layer in map_data["layers"]:
          is_collider = layer.get("collider", False)  # Verifica se a camada é de colisão
  
          if is_collider == colliders_only:
              for tile in layer["tiles"]:
                  x, y = tile["x"] * tile_size, tile["y"] * tile_size
  
                  if is_collider:
                      # Adiciona ao sistema de colisão
                      colliders.append(pygame.Rect(x, y, tile_size, tile_size))
                      # Desenha a imagem de colisão (um bloco da sprite)
                      screen.blit(imagem_teste, (x, y), (0, 0, tile_size, tile_size))
                  else:
                      # Define uma cor de fundo (verde)
                      color = (0, 255, 0)
                      pygame.draw.rect(screen, color, (x, y, tile_size, tile_size))
  ```
  - A função *draw_layer(colliders_only)* desenha o fundo ou a camada de colisão.

  - O mapa JSON contém camadas que podem ou não ser de colisão.

  - Se for uma camada de colisão, os blocos são adicionados à lista colliders e desenhados com a imagem fundo.png.

  - Caso contrário, os tiles do fundo são apenas desenhados como quadrados verdes.

  ## 4. Criar o Jogador

  ```python
  player_color = (0, 0, 255)  # Azul
  player_speed = 1
  player_rect = pygame.Rect(50, 100, tile_size, tile_size)  # Posição inicial do jogador
  O jogador é representado como um retângulo azul (player_color).
  ```
  - *player_speed = 1*: Define a velocidade do movimento.

  - *player_rect* guarda a posição e o tamanho do jogador.

  ## 5. Loop principal do jogo
  
  ```python
  running = True
  while running:
      screen.fill((0, 0, 0))  # Limpa a tela
  
      colliders.clear()  # Resetar os colliders para evitar duplicações
      draw_layer(colliders_only=False)  # Desenha o fundo
      draw_layer(colliders_only=True)   # Depois desenha as paredes
  ```
  
  - O loop limpa a tela e redesenha o mapa a cada frame.

  - A lista colliders é limpa antes de ser reconstruída para evitar tiles duplicados.

  ## 6. Capturar eventos

  ```python
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
  ```

  - O loop verifica se o jogador fechou a janela (pygame.QUIT).

  ## 7. Mover o jogador

  ```python
    keys = pygame.key.get_pressed()
    new_x, new_y = player_rect.x, player_rect.y

    if keys[pygame.K_w]:  # Cima
        new_y -= player_speed
    if keys[pygame.K_s]:  # Baixo
        new_y += player_speed
    if keys[pygame.K_a]:  # Esquerda
        new_x -= player_speed
    if keys[pygame.K_d]:  # Direita
        new_x += player_speed
  ```

  - Se o jogador pressionar W, A, S ou D, o código tenta mover o jogador.

  ## 8. Testar colisão

  ```python
    new_rect = pygame.Rect(new_x, new_y, tile_size, tile_size)

    if not any(new_rect.colliderect(collider) for collider in colliders):
        player_rect.x = new_x
        player_rect.y = new_y
  ```

  - Um novo retângulo (new_rect) é criado na posição para onde o jogador quer se mover.

  - Se não houver colisão, a posição do jogador é atualizada.

  ## 9. Desenhar o jogador e atualizar a tela

  ```python
    pygame.draw.rect(screen, player_color, player_rect)
    pygame.display.flip()
  ```

  - O jogador é desenhado na tela como um retângulo azul.

  - *pygame.display.flip()* atualiza a tela.

  ## 10. Fechar o jogo

  ```python
  pygame.quit()
  ```

  - Quando o loop termina, o Pygame é encerrado. 
</details>

<details>
  <summary><h2>📄 Explicando o JSON</h2></summary>
  
  ## map.JSON
  
  - JSON simples para exemplificação:
  
  ```json
  {
    "tileSize": 32,
    "layers": [
      {
        "name": "Fundo",
        "tiles": [
          { "x": 0, "y": 0 },
          { "x": 1, "y": 0 },
          { "x": 2, "y": 0 }
        ]
      },
      {
        "name": "Colisões",
        "collider": true,
        "tiles": [
          { "x": 5, "y": 5 },
          { "x": 6, "y": 5 },
          { "x": 7, "y": 5 }
        ]
      }
    ]
  }
  ```

  ### Explicação
  
  1. ```"tileSize"```: 32
  Indica que cada tile (quadrado do mapa) tem 32x32 pixels.

  2. ```"layers"``` (Lista de Camadas)
  O JSON contém um array layers, onde cada item representa uma camada do mapa.

  3. "Fundo"

  ```json
  {
    "name": "Fundo",
    "tiles": [
      { "x": 0, "y": 0 },
      { "x": 1, "y": 0 },
      { "x": 2, "y": 0 }
    ]
  }
  ```

  - Essa camada contém os tiles que fazem parte do cenário de fundo.

  - Os objetos dentro de tiles representam a posição do tile no mapa.

  ```{ "x": 0, "y": 0 }``` → Tile na posição (0,0)

  ```{ "x": 1, "y": 0 }``` → Tile na posição (1,0)

  ```{ "x": 2, "y": 0 }``` → Tile na posição (2,0)

  4. "Colisões"

  ```json
  {
    "name": "Colisões",
    "collider": true,
    "tiles": [
      { "x": 5, "y": 5 },
      { "x": 6, "y": 5 },
      { "x": 7, "y": 5 }
    ]
  }
  ```
  - Essa camada representa blocos que têm colisão.

  - ```"collider": true``` → Indica que essa camada é de colisão.

  - Os tiles dessa camada são blocos sólidos que o jogador não pode atravessar.

  ## Como o código usa esse JSON?
  
  ### 1. Define o tamanho dos tiles:

  ```python
  tile_size = map_data["tileSize"]
  ```

  ### 2. Percorre as camadas do JSON e desenha os tiles:

  ```python
  for layer in map_data["layers"]:
      for tile in layer["tiles"]:
          x, y = tile["x"] * tile_size, tile["y"] * tile_size
  ```

  ### 3. Se a camada for de colisão ("collider": true), adiciona à lista de colisores (colliders):

  ```python
  if is_collider:
      colliders.append(pygame.Rect(x, y, tile_size, tile_size))
  ```

  ### 4. Se for um tile de fundo, desenha um quadrado verde:

  ```python
  pygame.draw.rect(screen, (0, 255, 0), (x, y, tile_size, tile_size))
  ```

</details>

<details>
  <summary><h2>🗂️ Explicando o sistema de camadas</h2></summary>
  
  ## 🔹 Como as camadas funcionam?

  - Se houver um tile de chão na posição (1,2) e uma parede na mesma posição (1,2), o código vai desenhar o chão primeiro e depois a parede por cima.
  
  - Isso acontece porque no loop do código, primeiro ele desenha as camadas sem colisão (exemplo: chão, grama, água) e depois desenha a camada de colisão, que podem ser paredes ou objetos sólidos:

  ```python
  draw_layer(colliders_only=False)  # Desenha o fundo primeiro
  draw_layer(colliders_only=True)   # Depois desenha as paredes
  ```


  ## 📌 Exemplo de JSON com sobreposição de camadas

  ```json
  {
    "tileSize": 32,
    "layers": [
      {
        "name": "Chão",
        "tiles": [
          { "x": 1, "y": 1 },
          { "x": 1, "y": 2 }
        ]
      },
      {
        "name": "Paredes",
        "collider": true,
        "tiles": [
          { "x": 1, "y": 2 }
        ]
      }
    ]
  }
  ```

  ### 🔹 O que acontece aqui?
  
  - O tile (1,2) primeiro recebe um chão.

  - Depois, um tile de parede é desenhado por cima na mesma posição.

  - O jogador não pode atravessar a parede porque ela está na camada "collider": true.

  ### 🎮 Visualizando a sobreposição
  
  - Se você imaginasse isso como um mapa 2D, ficaria algo assim:

  ```
  Legenda:
  
  🟩 = Chão
  
  🟥 = Parede
  
  ⬛ = Vazio
  ```

  - Antes de desenhar colisões:

  ```
  🟩⬛⬛⬛
  🟩⬛⬛⬛
  ```

  - Depois de adicionar colisão:

  ```
  🟩⬛⬛⬛
  🟥⬛⬛⬛
  ```

  - Ou seja, a parede apareceu por cima do chão!

  ## 🛠 E se eu quiser mudar a ordem das camadas?
  
  - Se você quiser que uma camada apareça por cima de outra, basta mudar a ordem no JSON. Por exemplo, se você colocar "Paredes" antes do "Chão", o chão vai aparecer por cima da parede.

  - Caso queira fazer algo mais avançado, você pode adicionar uma chave "zIndex" no JSON e ordenar as camadas antes de desenhar.

</details>

<details>
  <summary><h2>⚠️ Importante</h2></summary>
  
  - O projeto foi criado com base na criação de somente duas camadas, 2 elementos, uma forma simples. Contudo, e se adicionarmos mais elementos?
    
  - A primeiro momento pensei em usar os "ids" do json, mas o recomendado é o seguinte: Cada elemento, uma nova camada, tipo uma parede quebrada, a camada de parede quebrada, um chão com cor diferente, uma camada de chão de cor diferente!
    
  - Isso torna mais fácil encontrar as camadas futuramente, além de mudar de estado dependendo da interação do jogador!
    
</details>
