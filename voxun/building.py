import bge

def clear_children(block):
	if len(block.children) > 0:
		for x in block.children:
			x.endObject()

def build_block(game_logic,cur_scene,pos,build_normal):
	name = game_logic.selected
	if name == "Torch":
		print("called at 1")
		if round(build_normal[2]) == 0:
			name = "Torch2"
	newblock = cur_scene.addObject(name, "outline")
	newblock.position = pos
	if name == "Torch2":
		print("called at 2")
		build_normal = build_normal.copy()
		temp = build_normal[1]
		build_normal[1] = build_normal[0]
		build_normal[0] = temp
		newblock.orientation = [build_normal, norm2, [0,0,1]]
	if name == "Torch" or name == "Torch2":
		print("called at 3")
		lamp = cur_scene.addObject("torchLight", block)
		lamp.position = newblock.position
		lamp.setParent(newblock)

def is_block_in_build_range(pos,box):
	return abs(box[0] - pos[0]) > 2 or abs(box[1] - pos[1]) > 2 or abs(box[2] - pos[2]) > 2.5

def get_build_location(blockray):
	norm = blockray.hitNormal
	pos = blockray.hitObject.position.copy()
	pos[0] += round(norm[0]*2)
	pos[1] += round(norm[1]*2)
	pos[2] += round(norm[2]*2)
	return pos

def try_build(game_logic,cur_scene,own,blockray):
	if blockray.positive:
		pos = get_build_location(blockray)
		build_normal = blockray.hitNormal
		box = own.parent.position
		if is_block_in_build_range(pos,box):
			build_block(game_logic,cur_scene,pos,build_normal)

def pick_at(game_logic,cur_scene,own,blockray,holdclick):
	if blockray.positive:
		own['destroy'] += 1
		block = blockray.hitObject
		if block != game_logic.lastblock and game_logic.lastblock != "":
			clear_children(game_logic.lastblock)
			own['destroy'] = 0
		if own['destroy'] <= 10 and not 'instabreak' in block:
			if len(block.children) > 0:
				block.children[0].endObject()
				game_logic.lastblock = block
				destroy = cur_scene.addObject("destroy"+str(own['destroy']), block)
				destroy.setParent(block)
			else:
				game_logic.lastblock = block
				destroy = cur_scene.addObject("destroy"+str(own['destroy']), block)
				destroy.setParent(block)			
		else:
			block.endObject()
			game_logic.lastblock = ""
			own['destroy'] = 0
	
	elif not holdclick.positive:
		if game_logic.lastblock:
			clear_children(game_logic.lastblock)	
		own['destroy'] = 0

def update():
	game_logic = bge.logic
	cont = game_logic.getCurrentController()
	cur_scene = game_logic.getCurrentScene()
	obs = cur_scene.objects
	own = cont.owner

	outline = obs['outline']

	lclick = cont.sensors['lclick']
	rclick = cont.sensors['rclick']
	blockray = cont.sensors['blockray']
	holdclick = cont.sensors['holdclick']

	# If user has right clicked, build a block.
	if rclick.positive:
		try_build(game_logic,cur_scene,own,blockray)

	# If user has left clicked, start the destroy process
	if lclick.positive:
		pick_at(game_logic,cur_scene,own,blockray,holdclick)

	# Draw box outline if the user can build.
	if blockray.positive:
		outline.visible = 1
		outline.position = get_build_location(blockray)
	else:
		outline.visible = 0

#update()
