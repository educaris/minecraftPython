#import all the necessary modules
from mcpi.minecraft import Minecraft
from mcpi import block
import time

#maak je koppeling met de Minecraft wereld
mc=Minecraft.create()

#zoek de positie van de speler op
pos=mc.player.getTilePos()

#Controleer of je niet te dicht bij de rand van de wereld staat
if pos.z<-40:
    mc.postToChat('teleporteer naar een veilige plek')
    mc.player.setPos(pos.x,pos.y,-40)
    pos=mc.player.getTilePos()


#Markeer waar de teleport is
zpos=pos.z-40

#Maak een vallei door blokken weg te halen
#mc.setBlocks(pos.x-1,pos.y+3,pos.z,pos.x+1,pos.y-7,pos.z,block.AIR.id)
mc.setBlocks(pos.x-1,pos.y+3,pos.z,pos.x+1,pos.y-7,pos.z-88,block.AIR.id)


#Bouw de onzichtbare bedrock plaats
mc.setBlocks(pos.x,pos.y-1,pos.z,pos.x,pos.y-7,pos.z,block.BEDROCK_INVISIBLE.id)
mc.setBlocks(pos.x-1,pos.y-1,pos.z,pos.x,pos.y-7,pos.z,block.BEDROCK_INVISIBLE.id)
mc.setBlocks(pos.x+1,pos.y-1,pos.z,pos.x,pos.y-7,pos.z,block.BEDROCK_INVISIBLE.id)
mc.setBlocks(pos.x,pos.y-1,pos.z-88,pos.x-1,pos.y-7,pos.z-88,block.BEDROCK_INVISIBLE.id)
mc.setBlocks(pos.x-1,pos.y-1,pos.z-88,pos.x,pos.y-7,pos.z-88,block.BEDROCK_INVISIBLE.id)
mc.setBlocks(pos.x+1,pos.y-1,pos.z-88,pos.x,pos.y-7,pos.z-88,block.BEDROCK_INVISIBLE.id)
mc.setBlocks(pos.x,pos.y,pos.z,pos.x,pos.y-7,pos.z-92,block.BEDROCK_INVISIBLE.id)

#Maak de bommen
mc.setBlocks(pos.x,pos.y,pos.z,pos.x,pos.y,pos.z-88,block.TNT.id,1)

#Maak het podiumeinde
mc.setBlocks(pos.x-2,pos.y,pos.z-93,pos.x+2,pos.y,pos.z-97,block.GLOWING_OBSIDIAN.id)
mc.setBlocks(pos.x-1,pos.y+1,pos.z-94,pos.x+1,pos.y+1,pos.z-96,block.NETHER_REACTOR_CORE.id,1)
mc.setBlock(pos.x,pos.y+2,pos.z-95,block.REDSTONE_ORE.id)

#hoeveel teleports heb je over
teleport=1

#Maak het teleport display
mc.setBlock(pos.x+1,pos.y+1,pos.z-44,block.NETHER_REACTOR_CORE.id,2)
mc.setBlock(pos.x-1,pos.y+1,pos.z-44,block.NETHER_REACTOR_CORE.id,2)

#Teleporteer de speler als hij/zij op een bepaalde plek is
while teleport ==1:
    pos=mc.player.getTilePos()
    if pos.z==zpos:
        mc.player.setPos(pos.x,pos.y,pos.z-24)
        teleport=0
