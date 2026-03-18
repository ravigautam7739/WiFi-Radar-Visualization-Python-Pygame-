import pygame
import math
import subprocess

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("WiFi Radar - All Networks")

clock = pygame.time.Clock()

CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 300

font = pygame.font.SysFont("Arial", 14)


def get_wifi_data():
    networks = []

    try:
        result = subprocess.check_output(
            ["netsh", "wlan", "show", "networks", "mode=bssid"]
        ).decode("utf-8", errors="ignore")

        current_ssid = None

        for line in result.split("\n"):
            line = line.strip()

            # Capture SSID
            if line.startswith("SSID"):
                parts = line.split(":")
                if len(parts) > 1:
                    current_ssid = parts[1].strip()

            # Capture Signal
            if "Signal" in line and current_ssid:
                signal = int(line.split(":")[1].strip().replace("%", ""))
                networks.append((current_ssid, signal))

        # Remove duplicates (keep strongest signal)
        unique = {}
        for ssid, signal in networks:
            if ssid not in unique or signal > unique[ssid]:
                unique[ssid] = signal

        return list(unique.items())

    except:
        return [
            ("DemoWiFi", 80),
            ("OfficeNet", 65),
            ("MobileHotspot", 40),
            ("CafeWiFi", 55)
        ]


def generate_positions(networks):
    positions = []
    total = len(networks)

    for i, (ssid, signal) in enumerate(networks):
        angle = (2 * math.pi / total) * i

        # Strong signal → closer
        distance = (100 - signal) * 2.5

        x = CENTER[0] + distance * math.cos(angle)
        y = CENTER[1] + distance * math.sin(angle)

        positions.append((ssid, signal, int(x), int(y)))

    return positions


networks = get_wifi_data()
points = generate_positions(networks)

angle = 0

running = True

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Radar circles
    for r in range(50, RADIUS, 50):
        pygame.draw.circle(screen, (0, 80, 0), CENTER, r, 1)

    # Sweep line
    end_x = CENTER[0] + RADIUS * math.cos(angle)
    end_y = CENTER[1] + RADIUS * math.sin(angle)
    pygame.draw.line(screen, (0, 255, 0), CENTER, (end_x, end_y), 2)

    # Draw all networks
    for ssid, signal, x, y in points:
        pygame.draw.circle(screen, (0, 255, 0), (x, y), 5)

        label = font.render(f"{ssid} ({signal}%)", True, (0, 255, 0))
        screen.blit(label, (x + 5, y + 5))

    angle += 0.02

    pygame.display.update()
    clock.tick(60)

pygame.quit()