"""
processing
"""
from penrose_p2 import *
import math

def render(tile):
    stroke(200)
    for coords in tile.lines():
        line(*coords)

def render_filled(tile):
    c = RED if tile.shape == KITE else BLUE
    stroke(*c)
    fill(*[v*0.5 for v in c])
    beginShape()
    for p in tile.points():
        vertex(p.x, p.y)
    endShape()

size(2000,1200)

background(0)
RED = (255,0,0)
BLUE = (60,60,255)
strokeWeight(1)

def draw_progression():
    translate(300, 300)
    pushMatrix()
    tiles = SUN
    print("x")
    for i in range(5):
        for t in tiles:
            render(t)
        tiles = inflate(tiles, False)
        translate(600,0)

    popMatrix()
    tiles = STAR
    translate(0,800)
    for i in range(5):
        for t in tiles:
            render(t)
        tiles = inflate(tiles, False)
        translate(600,0)

def draw_tiling():
    translate(900,500)
    scale(8)
    strokeWeight(0.5)
    tiles = iterate(SUN, 5)
    for tile in tiles:
        render(tile)

#  draw_progression()
draw_tiling()
