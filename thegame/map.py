class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths ={}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)


room35 = Room("Room35",
              """
              Terrorists have invaded Kimandi Appartment
              You, the only sole survivor is trying to escape
              You crafted a plan to sneak to the ground floor
              Activate the Kill plan by blowing the entire appartment
              By using the Kill Bomb hence killing all terrorists and
              Make your escape to the sunset, Are you up to the task?
              \n
              Suddenly your room's door is blasted open
              A short,one eyed, odd looking terrorist is standing at the door way
              He is holding an Ak-47
              He is about to aim towards you and make you toast
              What do you do?(run,dodge,scream,fart)
              """)

first_floor = Room("First Floor",
                   """
                   You combat roll outside
                   Pick up the gun
                   You see 2 other terrorist at one end
                   What do you do?(shoot, sneak)
                   """)

ground_floor = Room("Ground Floor",
                    """
                    You stealthy drop down the stairs
                    You see 2 other terrorist at the foot of the stairs
                    What do you do?(shoot, sneak)
                    """)

kill_plan = Room("Kill Plan",
                 """
                 You combat roll and manneuver to the other side of the stairs
                 You look for any other terrorist
                 its dead silent at this end, you are all alone
                 You enter the landlord's room silently to activate the killplan
                 You get to the locker where its hidden, you have to enter the keycode
                 The code is 3 digits (hint:The number of spartan soldiers)
                 if you get the code wrong 3 times it locks forever
                 and you are doomed..
                 """)

kill_bomb = Room ("Kill Bomb",
                  """
                  You find three terrorist catching a smoke
                  Talking about last night pl game where samatta scored a hatrick
                  They turn and see you holding the bomb
                  what do you do?
                  (throw bomb , place bomb)
                  """)


escape = Room ("Escape",
               """
               You quickly jump over the fence
               You find 5 escape pods ,which do you choose
               """)

the_end_winner = Room("The End",
                      """
                      You jump into pod 2 and hit the eject button
                      The pod easily slides out into the outside
                      Blasts you off into the sky
                      A parachute opens up and guides the pod to land
                      You won! Congratulation
                      """)

the_end_loser = Room ("The end",
                      """
                      You jump into the random pod and hit ejects
                      It blasts you into the sky
                      The parachute jams and fails to open as you start to descend in great speed
                      You hit the ground with a big thud
                      The pod explodes and you die
                      HAHAHA you lost! Better luck next time
                      """)

generic_death = Room("death", "You died.")

room35.add_paths({
                  'fart':first_floor,
                  'run':generic_death,
                  'dodge':generic_death,
                  'scream':generic_death})

first_floor.add_paths({
                     'sneak':ground_floor,
                     'shoot':generic_death})

ground_floor.add_paths({
                       'sneak':kill_plan,
                       'shoot':generic_death
                        })

kill_plan.add_paths({
                     '300':kill_bomb,
                     '*':generic_death})

kill_bomb.add_paths({
                     'throw bomb':generic_death,
                     'place bomb':escape })

escape.add_paths({
                  '2':the_end_winner,
                  '*':the_end_loser})

START = room35


