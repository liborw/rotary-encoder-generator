import svgwrite
import math

def arc(x, y, r1, r2, a0, a1) -> svgwrite.path.Path:
    """
    Create arc

    Parameters
        x,y center of the arc
        r1  smaller radius of the arc
        r2  larger radius of the arc
        a0  start angle
        a1  end angle
    """

    a0 = a0 / 180 * math.pi
    a1 = a1 / 180 * math.pi

    arc = f"""
        M {r2*math.sin(a0) + x} {r2*math.cos(a0) + y}
        A {r2} {r2} 0 0 0 {r2*math.sin(a1) + x} {r2*math.cos(a1) + y}
        L {r1*math.sin(a1) + x} {r1*math.cos(a1) + y}
        A {r1} {r1} 0 0 1 {r1*math.sin(a0) + x} {r1*math.cos(a0) + y}
        L {r2*math.sin(a0) + x} {r2*math.cos(a0) + y}
        Z
    """

    print(arc)

    return svgwrite.path.Path(arc.strip().replace("\n", " "), stroke_width=0)


def gray(n):
    for i in range(0, 1<<n):
        gray=i^(i>>1)
        yield "{0:0{1}b}".format(gray,n)


def gen_rotary_encoder(n:int, r0:int, r1:int, spacing:int, output_file:str):
    dwg = svgwrite.Drawing(output_file, profile='tiny')



    for j, g in enumerate(gray(n)):
        for i in range(n):
            r_small = r0 + (i * (r1 - r0)) + spacing
            r_big = r0 + ((i + 1) * (r1 - r0))

            a_step = 360 / (1<<n)
            a0 = j*a_step - 1
            a1 = (j+1)*a_step + 1

            if int(g[i]):
                dwg.add(arc(100, 100, r_small, r_big, a0, a1))

    dwg.save()


gen_rotary_encoder(7, 5, 10, 1,  "test.svg")





