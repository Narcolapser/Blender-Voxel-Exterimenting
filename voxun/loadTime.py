def main():
	import bge
	game_logic = bge.logic
	game_logic.lastblock = ""

	cont = game_logic.getCurrentController()
	cur_scene = game_logic.getCurrentScene()

	own = cont.owner


	#print("Load time script here.")
	
	#build_block(game_logic,cur_scene,[0,0,0],[0,0,0])
	
	makeGround(game_logic,cur_scene)

def build_block(game_logic,cur_scene,pos,build_normal=[0,0,0],block_type=None):
	if not block_type:
		block_type = "Grass"

	newblock = cur_scene.addObject(block_type, "outline")
	newblock.position = pos

def makeGround(game_logic,cur_scene):
	for i in range(-10,11,2):
		for j in range(-10,11,2):
			for n in range(-3,0,2):
				build_block(game_logic,cur_scene,[i,j,n],block_type='Stone')

main()
