import pygame #bruger pygame til at tegne former
import math #bruger math til at beregne visernes placering, takkernes placering mm. 
import time #henter pakken tid, så jeg kan benytte min computers lokale tid.
import sys #bruger sys til at afslutte programmet og lukke vinduet
import random #bruges til sneen 

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Miniprojekt 1: Mit seje, men simple analog ur. TRYK SPACE")


#valgte farver
white = (255, 255, 255)
black = (0, 0, 0)
dark_blue = (6, 2, 122)
light_blue = (226, 234, 244)
purple = (204, 108, 231)
lavendel = (231, 221, 255)
rosa = (239, 195, 202)
orange = (255, 165,0)
green = (35, 87, 35)
red = (204, 93, 85)
yellow = (251, 204, 76)
brown = (62, 56, 39)
light_brown = (94, 41, 22)

background_color = lavendel

#placering af uret
center = (250, 250)
ur_radius = 180

season = "none"

# jeg laver en funktion til at tegne viserne
def draw_hand():
    current_time = time.localtime()
    hours = current_time.tm_hour % 12
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    
    hour_angle = math.radians((hours * 30) + (minutes * 0.5) - 90)
    minute_angle = math.radians((minutes * 6) - 90)
    second_angle = math.radians((seconds * 6) - 90)
#jeg ændrer farverne på viserne og baggrunden afhængigt af årstiden (season)
    if season == "efterår":
        hour_color = red
        minute_color = yellow
        seconds_color = black
        screen_fill = brown
    elif season == "vinter":
        hour_color = lavendel
        minute_color = light_blue
        seconds_color = black
    else:
        hour_color = purple
        minute_color = dark_blue
        seconds_color = rosa
        screen_fill = lavendel
#jeg beregner og tegner viserne
    hour_x = center[0] + 80 * math.cos(hour_angle)
    hour_y = center[1] + 80 * math.sin(hour_angle)
    pygame.draw.line(screen, hour_color, center, (int(hour_x), int(hour_y)), 8)

    minutes_x = center[0] + 120 * math.cos(minute_angle)
    minutes_y = center[1] + 120 * math.sin(minute_angle)
    pygame.draw.line(screen, minute_color, center, (int(minutes_x), int(minutes_y)), 4)

    seconds_x = center[0] + 120 * math.cos(second_angle)
    seconds_y = center[1] + 120 * math.sin(second_angle)
    pygame.draw.line(screen, seconds_color, center, (int(seconds_x), int(seconds_y)), 1)
#jeg laver en funktion. Her tegner jeg de forskellige sæsoner, når jeg trykker på space
def draw_season():
    if season == "efterår":
        pygame.draw.circle(screen, orange,(250,250),180) #græskar
        pygame.draw.polygon(screen, black,[(198, 155), (170, 195), (210, 205)]) #venstre øje
        pygame.draw.polygon(screen, black,[(290,155), (275,205), (320,195)]) # højre øje
        pygame.draw.polygon(screen, black,[(250,230),(230,270),(270,270)]) #næsen
        pygame.draw.ellipse(screen, black,(125,320,250,60)) #mund
        pygame.draw.polygon(screen, orange,[(270,320),(300,320),(285,350)]) #højre tand øverst
        pygame.draw.polygon(screen, orange,[(230,320), (200,320), (215,350)]) #venstre tand øverst
        pygame.draw.polygon(screen, orange, [(250,350),(230,380),(270,380)]) # nederste tand i midten
        pygame.draw.polygon(screen, green, [(210,76),(290,75), (295,20)]) #græskar stilk/hat
    elif season == "vinter":
        pygame.draw.circle(screen, white,(250,300),150) #snemandkrop
        pygame.draw.circle(screen, white,(250,120),60) #snemand hoved
        pygame.draw.rect(screen, black,(200,60,100,15)) #bunden af hatten
        pygame.draw.rect(screen, brown, (210,10,80,50)) #toppen af hatten
        pygame.draw.polygon(screen, orange, [(250,120), (250,130),(280,125)]) #gulerodsnæse
        pygame.draw.circle(screen, black,(230,110), 5) #venstre øje
        pygame.draw.circle(screen, black, (270,110), 5) #højre øje
        for i in range (4): #knapper på snemanden
            x = 250 
            y = 220 + i * 50
            pygame.draw.circle(screen, light_brown, (x,y), 5)
        pygame.draw.line(screen, light_brown, (110,240), (70,180), 2) #venstre arm:
        pygame.draw.line(screen, light_brown, (70,180), (80,170),1) #højre finger
        pygame.draw.line(screen, light_brown, (70,180), (65,170),1) #midterste finger
        pygame.draw.line(screen, light_brown, (70,180), (60,180),1) #venstre finger
        pygame.draw.line(screen, light_brown, (388,240), (440,220),2) #højre arm:
        pygame.draw.line(screen, light_brown, (440,220), (445,230),1) #højre finger
        pygame.draw.line(screen, light_brown, (440,220), (440,210),1) #venstre finger
        pygame.draw.line(screen, light_brown, (440,220), (450,215),1) #finger i midten

        draw_snow()
    elif season == "none":
        pass
#jeg laver en funktion, så der kommer snefnug effekt på vinter sæsonen.
def draw_snow():
    for _ in range (50):
        x = random.randint(0, 500)
        y = random.randint(0, 500)
        pygame.draw.circle(screen, white, (x,y), 2)
#her laver jeg en løkke, så programmet kører indtil det lukkes ned
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
# her skifter jeg årstiderne, når der trykkes på space
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if season == "none":
                    season = "efterår"
                    background_color = light_brown
                elif season == "efterår":
                    season = "vinter"
                    background_color = light_blue
                    
                else:
                    season = "none"
                    background_color = lavendel
        #jeg rykker urskiven, så der er plads til snemandens hoved
        if season == "vinter":
            center = (250, 300)
            ur_radius = 150
        else: 
            center = (250, 250)
            ur_radius = 180
#her tegner jeg urskiven, viserne og årstiderne
    screen.fill(background_color)
    pygame.draw.circle(screen, black, center, ur_radius, 3)
    #jeg tegner takkerne på urskiven
    draw_season()
    for i in range(12):
        angle = math.radians(i * 30)
        x1 = center[0] + (ur_radius - 20) * math.cos(angle)
        y1 = center[1] + (ur_radius - 20) * math.sin(angle)
        x2 = center[0] + (ur_radius - 40) * math.cos(angle)
        y2 = center[1] + (ur_radius - 40) * math.sin(angle)
        pygame.draw.line(screen, black, (int(x1), int(y1)), (int(x2), int(y2)), 3)

    #jeg tegner viserne
    draw_hand()
    pygame.display.flip()
pygame.quit()
sys.exit()