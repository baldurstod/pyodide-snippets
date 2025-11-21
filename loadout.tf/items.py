##################################################
### Add an item
##################################################
import characters
import items
import tf2

# Init item list
await items.initItems()
# await items.initTournamentMedals() # uncomment if you need tournanment medals
# await items.initWorkshopItems() # uncomment if you need workshop items
character = await characters.selectCharacter(tf2.Demoman)
template = items.getItemTemplate(47)
if template:
    item = await character.addItem(template)
    # Change the paint color
    item.setPaint(tf2.Paints.PinkAsHell)

##################################################
### Add a weapon
##################################################
import characters
import items
import tf2

await items.initItems()
character = await characters.selectCharacter(tf2.Demoman)
template = items.getItemTemplate(206)  # gl
if template:
    item = await character.addItem(template)
    item.showFestivizer(True)
    item.critBoost()

##################################################
### Add a stat clock
##################################################
import characters
import items
import tf2

await items.initItems()
character = await characters.selectCharacter(tf2.Demoman)
template = items.getItemTemplate(206)  # gl
if template:
    item = await character.addItem(template)
    item.setKillCount(1234)  # item.setKillCount(None) to remove the stat clock

##################################################
### Add a specialized killstreak
##################################################
import characters
import items
import tf2

await items.initItems()
character = await characters.selectCharacter(tf2.Demoman)
template = items.getItemTemplate(206)  # gl
if template:
    item = await character.addItem(template)
    item.setSheen(tf2.KillstreakColor.VillainousViolet)

##################################################
### Set a warpaint on a weapon
##################################################
import characters
import items
import tf2

await items.initItems()
character = await characters.selectCharacter(tf2.Demoman)
template = items.getItemTemplate(206)  # gl
if template:
    item = await character.addItem(template)
    # Warpaint id, wear and seed
    # Wear has a value of 0 (FN) to 4 (BS)
    item.setWarpaint(200, 0, 0)
