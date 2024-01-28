import random

def palletfinder(color):
    if color in [9, 19, 25, 37, 53, 54, 56, 57, 58]:
        return "Red Pallet"
    elif color in [63, 10, 29, 59, 30, 64, 65, 62, 26]:
        return "Orange Pallet"
    elif color in [11, 71, 14, 31, 27, 45, 70]:
        return "Yellow Pallet"
    elif color in [0, 1, 105, 28, 32, 20, 2, 79, 72, 68, 38]:
        return "Green Pallet"
    elif color in [74, 3, 40, 77, 33, 21, 82, 75, 81, 76]:
        return "Lightblue Pallet"
    elif color in [16, 4, 5, 39, 34, 86, 89, 83, 84, 106, 88]:
        return "Blue Pallet"
    elif color in [52, 41, 6, 35, 96, 23, 95, 97, 49]:
        return "Purple Pallet"
    elif color in [98, 8, 36, 7, 13, 24, 100, 103, 43, 99, 104]:
        return "Pink Pallet"
    elif color in [12, 17, 102, 18, 15, 91, 94]:
        return "Grey Pallet"
    else:
        return "ERROR, PLEASE CHECK"

# ----------------------------------------- ^^^^ FUNCTIONS/MISC ^^^^ ------------------------------------------------------------------------------------------------
# ----------------------------------------- vvvv ICON LISTS vvvv ------------------------------------------------------------------------------------------------

cubes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 
        37, 38, 39, 40, 41, 42, 43, 44, 45, 47, 49, 50, 51, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 64, 65, 66, 67, 68, 69, 70, 71, 72, 
        73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 
        109, 110, 111, 112, 113, 114, 115, 116, 118, 119, 120, 121, 122, 126, 136, 137, 138, 139, 140, 141, 142, 143, 144, 
        145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 158, 159, 160, 162, 165, 172, 173, 178, 180, 
        188, 191, 199, 202, 203, 205, 206, 207, 213,
        217, 218, 222, 225, 226, 227, 228, 229, 233, 235, 237, 240, 242, 246, 247, 
        256, 259, 267, 274,
        290, 299, 300, 313, 318, 319, 
        325, 328, 331, 336, 340, 341, 344, 345, 349, 352, 355, 359, 
        365, 366, 371, 374, 380, 382, 388, 389, 392, 
        398, 402, 403, 407, 408, 418, 431, 432, 
        441, 456, 461, 466, 
        474, 482, 483]

ships = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 
        37, 38, 39, 40, 41, 42, 43, 44, 45, 47, 49, 50, 51, 52, 53, 58, 60, 63, 71,
        75, 77, 78, 79, 89, 90, 91, 98, 103, 
        110, 125, 129, 137,
        148, 150, 161, 163]

balls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 
        37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 52, 53, 57, 60, 68, 71, 
        75, 77, 78, 81, 82, 83, 85, 87, 92, 93, 101, 103, 104, 105, 106, 107, 
        109, 111, 112, 116, 117]

ufos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 
        37, 38, 40, 45, 52,
        74, 78, 80, 81, 83, 85, 93, 100, 102, 103, 
        119, 123, 127, 140, 141,
        149]

waves = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 
        38, 45, 50, 53, 54, 58, 64, 66, 
        74, 79, 80, 81, 91, 93]

robots = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 31, 32, 33, 34,
        38, 39, 43, 46, 49, 51, 56, 57, 60, 62]

spiders = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 22, 23, 24, 26, 29, 32, 34,
        38, 43, 44, 49, 51, 52, 53, 54, 60, 63, 64, 65, 66, 69]

swings = [1, 2, 3, 7, 9, 12, 14, 21, 22, 23, 25, 26, 28, 29, 32, 36,
        40]

color1set = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 
            35, 36, 37, 38, 39, 40, 41, 45, 49, 52, 53, 56, 58, 59, 61, 62, 63, 64, 65, 
            71, 74, 76, 77, 82, 84, 86, 89, 94, 95, 96, 97, 98, 99, 100, 102, 103, 105]

color2set = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 
            35, 36, 37, 38, 39, 40, 41, 43, 45, 53, 54, 57, 59, 62, 64, 65, 68, 70,
            71, 72, 75, 77, 81, 82, 83, 84, 85, 86, 88, 89, 91, 94, 100, 102, 103, 104, 105, 106]

trails = [1, 2, 4, 5, 6, 7]

death_effects = [1, 2, 3, 4, 5, 6, 7, 9, 10, 12, 14, 15]

# ----------------------------------------- ^^^^ ICON LISTS ^^^^ ------------------------------------------------------------------------------------------------
# ----------------------------------------- vvvv MENU vvvv ------------------------------------------------------------------------------------------------

print("GEOMETRY DASH ICON RANDOMIZER\n")
while True:
    option = input("PRESS ENTER TO PERFORM RANDOMIZATION (1 to see total icons, 0 to exit program): ")
    
    # MIN ICON FOR NEW ONLY FILTER
    # CUBES: 143
    # SHIPS: 52
    # BALLS: 44 
    # UFOS: 36
    # WAVES: 38
    # ROBOT: 27
    # SPIDER: 18
    
    
    
    if option == '':
        cube = random.choice(cubes[cubes.index(142):])
        ship = random.choice(ships[ships.index(52):])
        ball = random.choice(balls[balls.index(44):])
        ufo = random.choice(ufos[ufos.index(36):])
        wave = random.choice(waves[waves.index(38):])
        robot = random.choice(robots[robots.index(27):])
        spider = random.choice(spiders[spiders.index(18):])
        swing = random.choice(swings)
        color1 = random.choice(color1set)
        color2 = random.choice(color2set)
        glow = random.choice(color2set)
        trail = random.choice(trails)
        deatheffect = random.choice(death_effects)
        
        print(f"""NEW ICONS: 
              CUBE: {cube}
              SHIP: {ship}
              BALL: {ball}
              UFO: {ufo}
              WAVE: {wave}
              ROBOT: {robot}
              SPIDER: {spider}
              SWING: {swing}
              TRAIL: {trail}
              DEATH EFFECT: {deatheffect}
              COLOR 1: {color1} ({palletfinder(color1)})  
              COLOR 2: {color2} ({palletfinder(color2)})
              GLOW: {glow} ({palletfinder(glow)})
              \n""")
        
    elif option == "1":
        print(f"""ICON COUNT:
              --> {len(cubes)} / 484 CUBES ({(len(cubes) / 484)*100:.1f}%)
              --> {len(ships)} / 169 SHIPS ({(len(ships) / 169)*100:.1f}%)
              --> {len(balls)} / 118 BALLS ({(len(balls) / 118)*100:.1f}%)
              --> {len(ufos)} / 149 UFOS ({(len(ufos) / 149)*100:.1f}%)
              --> {len(waves)} / 96 WAVES ({(len(waves) / 96)*100:.1f}%)
              --> {len(robots)} / 68 ROBOTS ({(len(robots) / 68)*100:.1f}%)
              --> {len(spiders)} / 69 SPIDERS ({(len(spiders) / 69)*100:.1f}%)
              --> {len(swings)} / 43 SWINGS ({(len(swings) / 43)*100:.1f}%)
              --> {len(trails)} / 7 TRAILS ({(len(trails) / 7)*100:.1f}%)
              --> {len(death_effects)} / 20 DEATH EFFECTS ({(len(death_effects) / 20)*100:.1f}%)
              --> {len(color1set)} / 107 MAIN COLORS ({(len(color1set) / 106)*100:.1f}%)
              --> {len(color2set)} / 107 SECONDARY COLORS ({(len(color2set) / 106)*100:.1f}%)
              \n""")
    


# GAUNTLET UNLOCKS
# --> ICONS: 
# 138 (Time Gauntlet) x
# 139 (Cristal Gauntlet) x 
# 141 (Spike Gauntlet) x
# 142 (Monster Gauntlet) x
# 244 (Inferno Gauntlet)
# 303 (Surprise Gauntlet)
# 312 (Rune Gauntlet)
# 315 (Spooky Gauntlet)
# 316 (Treasure Gauntlet)
# 326 (Halloween Gauntlet)
# 377 (Cyborg Gauntlet)
# 397 (Gem Gauntlet)
# 408 (Castle Gauntlet) x
# 425 (Cursed Gauntlet)
# 436 (Toxic Gauntlet)
# 453 (Grave Gauntlet)
# 467 (Acid Gauntlet)
# 476 (Haunted Gauntlet)
# 482 (Discord Gauntlet)

# --> SHIPS:
# 49 (Death Gauntlet) x
# 90 (Split Gauntlet) x
# 96 (Dragon Gauntlet)
# 142 (Snake Gauntlet)
# 166 (Mystery Gauntlet)

# --> BALLS:
# 43 (Magic Gauntlet) x
# 67 (Forest Gauntlet)
# 82 (Universe Gauntlet) x
# 103 (World Gauntlet) x

# --> UFOS:
# 119 (Galaxy Gauntlet) x
# 137 (Water Gauntlet) 

# --> WAVES:
# 49 (Temple Gauntlet)
# 63 (Christmas Gauntlet)
# 90 (Fantasy Gauntlet)
# 94 (Potion Gauntlet)

# --> ROBOTS:
# 16 (Chaos Gauntlet) x 

# --> SPIDERS
# 10 (Demon Gauntlet) x
# 67 (Spider Gauntlet)

# --> SWINGS
# 16 (Portal Gauntlet)
# 31 (Strange Gauntlet)
