from Application.Objects_For_Display.Inanimate_Objects.Inanimate_Objects import Inanimate_Object

def Inanimate_Objects_facilitator(walls,w_counter,c1,c2,x_i=100,y_i=100,color="blue"):

    x1,y1 = c1
    x2,y2 = c2
    while x1 < x2 or y1 < y2:
        walls.append(Inanimate_Object())
        walls[w_counter].set_color(color)
        walls[w_counter].set_img(f"wall_{color}.png")
        walls[w_counter].set_coord(x1,y1)
        walls[w_counter].block_movement = True

        w_counter+=1
        if x1 < x2:
            x1 += x_i
        if y1 < y2:
            y1 += y_i

    x1-= x_i
    y1-= y_i
    return w_counter
