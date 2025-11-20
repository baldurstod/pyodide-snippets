##################################################
### Add a character
##################################################
import characters
import tf2

character = await characters.selectCharacter(
    tf2.Scout  # a number can be also be used: 0-9 for humans, 100-109 for bots
)

# Change the team
character.setTeam(tf2.Blu)  # default team is Red


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
template = items.getItemTemplate("47")
if template:
    item = await character.addItem(template)
	# Change the paint color
    item.setPaint(tf2.Paints.PinkAsHell)
