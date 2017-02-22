import mcpi.minecraft as minecraft
import mcpi.block as block
from time import sleep
mc = minecraft.Minecraft.create()
mc.postToChat("Welkom bij Lava Val!!")

sleep(3)
pos = mc.player.getTilePos()
mc.setBlocks(pos.x - 5, pos.y - 2, pos.z - 5,
        pos.x + 5, pos.y - 2, pos.z + 5,
        block.STONE.id)
mc.setBlocks(pos.x - 5, pos.y - 1, pos.z - 5,
        pos.x + 5, pos.y - 1, pos.z + 5,
        block.LAVA.id)

mc.setBlock(pos.x, pos.y - 1, pos.z, block.DIAMOND_BLOCK.id)

mc.postToChat("Klaar voor de start!")
mc.postToChat("De blokken onder je voeten gaan verdwijnen")
sleep(3)
mc.postToChat("Go")
gameover = False
while gameover == False:
    p = mc.player.getTilePos()
    mc.setBlock(p.x, p.y - 1, p.z, block.OBSIDIAN.id)
    sleep(2)
    mc.setBlock(p.x, p.y - 1, p.z, block.AIR.id)
    sleep(0.5)
    if p.y != pos.y:
        gameover = True
mc.postToChat("Game over.")
