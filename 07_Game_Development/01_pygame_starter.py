import pygame
import sys

# 1. Pygame को शुरू करना
pygame.init()

# 2. स्क्रीन (विंडो) सेट करना
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("मेरा पहला पायगेम - स्टार्टर टेम्पलेट")

# रंग (RGB फॉर्मेट)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# खिलाड़ी की स्थिति
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

# घड़ी (फ्रेम रेट को नियंत्रित करने के लिए)
clock = pygame.time.Clock()

# 3. गेम लूप (यह लूप तब तक चलेगा जब तक आप गेम बंद नहीं करते)
running = True
while running:
    # A. इवेंट्स को हैंडल करना (कीबोर्ड, माउस इनपुट)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # चाबियाँ (Keys) दबाने की जांच
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # B. स्क्रीन को अपडेट करना (Render)
    # पहले पूरी स्क्रीन को सफेद करें
    screen.fill(WHITE)

    # खिलाड़ी (एक नीले बॉक्स) को स्क्रीन पर बनाएं
    # pygame.draw.rect(screen, color, (x, y, width, height))
    pygame.draw.rect(screen, BLUE, (player_x, player_y, 50, 50))

    # बदलावों को डिस्प्ले पर दिखाना
    pygame.display.flip()

    # गेम को 60 फ्रेम प्रति सेकंड (FPS) पर चलाएं
    clock.tick(60)

# गेम बंद करें
pygame.quit()
sys.exit()
