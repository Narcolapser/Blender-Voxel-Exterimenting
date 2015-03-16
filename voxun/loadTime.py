import random

def main():
	import bge
	game_logic = bge.logic
	game_logic.lastblock = ""

	cont = game_logic.getCurrentController()
	cur_scene = game_logic.getCurrentScene()

	own = cont.owner

	#makeGround(game_logic,cur_scene)
	makeSwissGround(game_logic,cur_scene)

def build_block(game_logic,cur_scene,pos,build_normal=[0,0,0],block_type=None):
	if not block_type:
		block_type = "Grass"

	newblock = cur_scene.addObject(block_type, "outline")
	newblock.position = pos

def setFinishCube(game_logic,cur_scene,pos):
	build_block(game_logic,cur_scene,pos,block_type="Finish")

def makeGround(game_logic,cur_scene):
	game_logic.setGravity([0,0,-5])
	for i in range(-10,11+random.randint(1,100),2):
		for j in range(-10,11+random.randint(1,100),2):
			for n in range(-3,0,2):
				build_block(game_logic,cur_scene,[i,j,n],block_type='Stone')
	
	setFinishCube(game_logic,cur_scene,[6,6,6])

def makeSwissGround(game_logic,cur_scene):
	game_logic.setGravity([0,0,-10])

	for i in range(2,100,2):
		for j in range(2,100,2):
			for n in range(-10,90,2):
				if random.random()<0.05:
					build_block(game_logic,cur_scene,[i,j,n],block_type='Dirt')

	build_block(game_logic,cur_scene,[0,0,0])
	setFinishCube(game_logic,cur_scene,[90,90,95])

main()
