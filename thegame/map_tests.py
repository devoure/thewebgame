from nose.tools import *
from thegame.map import *

def test_room():
    gold = Room("GoldRoom",
                """
                This room has gold in it, There is a door to the north

                """)
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "Test the  room")
    north = Room("North", "Test the room")
    south = Room("South", "Test the room")

    center.add_paths({'north':north,
                      'south':south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("Start", "You can go west and down a hole")
    west = Room("Trees", "There are trees, you can go east")
    down = Room("Dungeons", "Its dark down here, you can go up")

    start.add_paths({'west':west, 'down':down})
    west.add_paths({'east':start})
    down.add_paths({'up':start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

def test_gothon_game_map():
    assert_equal(START.go('run'),generic_death)
    assert_equal(START.go('dodge'),generic_death)

    room= START.go('fart')
    assert_equal(room, first_floor)
