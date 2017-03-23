from data import locations

directions = {
    'west': (-1, 0),
    'east': (1, 0),
    'north': (0, -1),
    'south': (0, 1),
}

position = (0, 0)

pocket = []

while True:
    location = locations[position]['name']
    print 'you are at the %s' % location
    description = locations[position]['description']
    print description

    items = locations[position]['objects']
    print 'you can pick up here:'
    for i in items:
        print i

    item = raw_input('what would you like to pick up?\n')
    if item not in items:
        print 'sorry, this item is not available'
    elif item in pocket:
        print 'you have this item in your pocket already'
    else:
        pocket.append(item)
        print 'you have in your pocket:'
        for i in pocket:
            print i

    valid_directions = {}
    for k, v in directions.iteritems():
        possible_position = (position[0] + v[0], position[1] + v[1])
        possible_location = locations.get(possible_position)
        if possible_location:
            print 'to the %s is a %s' % (k, possible_location['name'])
            valid_directions[k] = possible_position

    direction = raw_input('which direction do you want to go?\n')
    new_position = valid_directions.get(direction)
    if new_position:
        position = new_position
    else:
        print "sorry, that isn't a valid direction"