import tcod as libtcod

def handle_keys(key):
	# Movement keys
	if key.vk == libtcod.KEY_UP:
		return {'move': (0, -1)}
	elif key.vk == libtcod.KEY_DOWN:
		return {'move': (0, 1)}
	elif key.vk == libtcod.KEY_LEFT:
		return {'move': (-1, 0)}
	elif key.vk == libtcod.KEY_RIGHT:
		return {'move': (1, 0)}

	# alt+enter fullscreen
	if key.vk == libtcod.KEY_ENTER and key.lalt:
		return {'fullscreen': True}

	# escape exit
	if key.vk == libtcod.KEY_ESCAPE:
		return {'exit': True}

	# no key
	return {}

