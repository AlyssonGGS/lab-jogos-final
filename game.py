__author__ = 'AlyssonNote'
from PPlay.window import *
from gameScene import *

janela = Window(800,600)
actualScene = GameScene()
janela.set_background_color((255,255,255))
while True:
    #roda o update da cena atual
    actualScene.update(janela.delta_time(),janela.get_keyboard())
    #desenha a cena
    actualScene.draw()
    #atualiza a janela
    janela.update()


