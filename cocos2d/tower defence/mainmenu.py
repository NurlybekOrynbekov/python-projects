import cocos
import cocos.actions as ac

from cocos.menu import *
from cocos.scenes.transitions import FadeTRTransition

import pyglet.app

from gamelayer import new_game

def new_menu():
    scene = cocos.scene.Scene()
    color_layer = cocos.layer.ColorLayer(205, 133, 63, 255)
    scene.add(MainMenu(), z=1)
    scene.add(color_layer, z=0)
    return scene

class MainMenu(Menu):
    def __init__(self):
        super(MainMenu, self).__init__('Tower Defence')

        self.font_title['font_name'] = 'Oswald'
        self.font_item['font_name'] = 'Oswald'
        self.font_item_selected['font_name'] = 'Oswald'

        self.menu_anchor_y = 'center'
        self.menu_anchor_x = 'center'

        items = list()
        items.append(MenuItem('New Game', self.on_new_game))
        items.append(ToggleMenuItem('Show FPS: ', self.show_fps, cocos.director.director.show_FPS))
        items.append(MenuItem('Quit', pyglet.app.exit))

        self.create_menu(items, ac.ScaleTo(1.25, duration=0.25), ac.ScaleTo(1.0, duration=0.25))

    def show_fps(self, val):
        cocos.director.director.show_FPS = val

    def on_new_game(self):
        cocos.director.director.push(FadeTRTransition(new_game(), duration=2))