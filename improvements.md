Neville - idk 4+ year
Mixture: Search castle for items, and fight monsters for items.  Collect items to win.
Dying - respawn somewhere (near where you start hopefully), maybe small penalty (lose ingredients)
	or game over
Locked chests/doors, need to learn spell vs indididual keys vs nonunique keys (maybe spell casts)
Containers - search to find stuff? Random loot in them? (Search through professors office for stuff, tie in with inspect)
Currency - buy "quality of life" things - health potions, spell casts, maybe one item for potion
Saving maybe - Rememberall
Rooms monsters can be in - forest (maybe hagrid's house as key location), sections in castle? @ Hagrid's house fast travel to room in castle.
Crafting - Dunk skin from animal in fountain, gain attributes
Hermione being condescending when you're too slow

complex rooms (light levels impact monster defenses) - 3
player attributes (stats) strength, hitpoints,  - 3
leveling up - 4

Potion - Liquid luck
ingrediants - 7 things
1 - Buy with coins (tincture of thyme)
2 - Hidden in room (occamy eggshell)
3 - Combat (murtlab tentacle)
4 - grow (event happening tie in) (squill bulb) 
5 - do something for hagrid maybe combat (ashwinder egg)
6 - starts with (powdered common rue)

BUG:
possibly "help" in combat changes what room you're in and quits out of combat
when @ 1 mana stops from casting spell
picking up 3 magic keys, dropping 2, then unlocking something
rats/pixies can go into the water
werewolf appears in castle lol
Want it to print situation more frequently
Pixie drop gillyweed early
Defense against the dark arts displaying items when there are none, and transfiguration courtyard
----
You are in the Dark Forest.

This room contains the following monsters:
Giant Spider

You can go in the following directions:
west
south

What would you like to do? go south
Traceback (most recent call last):
  File "main.1.py", line 864, in <module>
    createWorld(False)
  File "main.1.py", line 269, in createWorld
    templist[-1].moveTo(target)
IndexError: list index out of range

----
TODO:
Crafting common items - better book
abbreviations for more than just "use" ( so we can say "use small", and if only one item starts with small, we're good)

use (consumable) items during combat (no, don't want to have to allow to show inventory)

"populate" world more - random npcs (very little dialogue/give out small free stuff)

rememberall - nah


Mark handled much of the random element of gameplay (monsters, spawning, 
fighting, looting, updating, the Dark Forest map). Alisa wrote for the more 
uniform parts (the castle map, NPCs and interaction, quests, item display, 
keys, locks). We created the game side by side in Cloud9, so running the code 
often involved checking for errors as we wrote in a single workspace. We would
let each other know of bugs and talk out solutions or fix them on the spot.

1 drop A
1 wait M
1 me M
2 bigger world A
2 inventory maximum size M
2 inspect M/A
2 auto-generating monsters M
2 victory condition A
2 healing items M
2 locked doors A
2 containers M
2 stacking items A
2 regeneration M
3 random world M
3 loot M
3 more monsters M
3 special rooms M/A
3 player attributes M
1-3 command abbreviations M
4 currency M
4 crafting M/A
4 magic M
4 characters A

menu system M
quests A
trading A
