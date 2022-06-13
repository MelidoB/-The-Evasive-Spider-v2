from Application.An_Application import Application
from Application.Objects_For_Display.Player.Player import Player
from Application.Objects_For_Display.Inanimate_Objects.Inanimate_Objects import Inanimate_Object
from Application.Objects_For_Display.Inanimate_Objects.Inanimate_Objects_facilitator import Inanimate_Objects_facilitator


def main():
    #una aplicacion
    a = Application()
    #Esta applicacion de w and h. Que pone todos los objetos en la display
    a.set_display_measurements(900,800)

    #un contenedor

    #Un jugador en la aplicaccions
    p = Player() #player instance
    p.set_img("spider.png") ##img for player
    p.set_coord(200,500) #x,y
    p.set_images_movements('left', ['Left/1.png', 'Left/2.png','Left/3.png'])
    p.set_images_movements('right', ['Right/1.png', 'Right/2.png', 'Right/3.png'])
    p.set_images_movements('top', ['Top/1.png', 'Top/2.png', 'Top/3.png'])
    p.set_images_movements('down', ['Down/1.png', 'Down/2.png', 'Down/3.png'])
    p.set_movement_keybinds(left = 'a', right = 'd', top = 'w', down='s')

    #a red mushroom en la aplicacion
    red_m = Inanimate_Object()
    red_m.set_img("red_mushroom.png")
    red_m.set_character_img_transformation("Red")
    red_m.set_coord(300, 900)


    # a yellow mushroom en la aplicacion
    yellow_m = Inanimate_Object()
    yellow_m.set_img("yellow_mushroom.png")
    yellow_m.set_character_img_transformation("Yellow")
    yellow_m.set_coord(500, 200)


    #walls
    walls = []
    n = 0
    #Top
    n = Inanimate_Objects_facilitator(walls, n, (0, 0), (800, 0))
    n = Inanimate_Objects_facilitator(walls, n, (0, 0), (0, 500))
    n = Inanimate_Objects_facilitator(walls, n, (0, 600), (0, 1000))
    n = Inanimate_Objects_facilitator(walls, n, (0, 1000), (800, 1000))
    n = Inanimate_Objects_facilitator(walls, n, (800, 0), (800, 1100), color='red')

    n = Inanimate_Objects_facilitator(walls, n, (400, 0), (400, 400))
    n = Inanimate_Objects_facilitator(walls, n, (400, 500), (400, 1000))
    n = Inanimate_Objects_facilitator(walls, n, (100, 400), (500, 400), color='yellow')

    #Victory flag
    victory_flag = Inanimate_Object()
    victory_flag.set_img("victory_flag.png")
    victory_flag.set_coord(200, 180)
    #victory_flag.set_coord(200, 480) #for auto-win

    #victory img
    victory = Inanimate_Object()
    victory.set_img("won.png")
    victory.set_coord(150, 180)

    #pasarlo al contenedor
    a.insert_element_to_container("player",[p])
    a.insert_element_to_container("mushroom", [red_m, yellow_m])
    a.insert_element_to_container("walls", walls)
    a.insert_element_to_container("victory_flag",[victory_flag])
    a.set_victory(victory)

    #Correr Aplicacion
    a.run()

if __name__=='__main__':
    main()