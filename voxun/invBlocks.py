# Not entirely sure what this Code does. It seems to be related to the inventory boxes at the bottom
# of the screen. Though I can't pin exactly what each step does. 

def main():
	import bge
	game_logic = bge.logic

	controller = game_logic.getCurrentController()
	cur_scene = game_logic.getCurrentScene()
	own = controller.owner

	#doesn't seem to be used
	objects = cur_scene.objects

	if 'block' in own:
		if len(own.children) > 0:
			if own.children[0].name != own['block']:
				own.children[0].endObject()
				ob = cur_scene.addObject(own['block'], own)
				ob.cur_scenetParent(own)
		else:
			ob = cur_scene.addObject(own['block'], own)
			ob.cur_scenetParent(own)

#main()
