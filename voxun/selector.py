def main():
	import bge
	game_logic = bge.logic

	controller = game_logic.getCurrentController()
	cur_scene = game_logic.getCurrentScene()

	own = controller.owner
	objects = cur_scene.objects

	block = objects['block'+str(own['selected'])]
	if "block" in block:
		game_logic.selected = block['block'].rstrip("Inv")


main()
