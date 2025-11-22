##################################################
### Add a cosmetic unusual
##################################################
import characters
import items
import tf2

# Init effects
await items.initItems()

character = await characters.selectCharacter(tf2.Demoman)
# Get the effect template
[_, template] = items.getEffectTemplateById(9) # green energy
if template:
	# Add the effect
    character.addEffect(template)

##################################################
### Add a taunt unusual
##################################################
import characters
import items
import tf2

# Init effects
await items.initItems()

character = await characters.selectCharacter(tf2.Demoman)
# Get the effect template
[_, template] = items.getEffectTemplateById(3005) # Fountain of Delight
if template:
	# Add the taunt effect
    character.setTauntEffect(template)

##################################################
### Add a killstreak effect
##################################################
import characters
import items
import tf2

# Init effects
await items.initItems()

character = await characters.selectCharacter(tf2.Demoman)
# Get the effect template
[_, template] = items.getEffectTemplateById(22005) # Flames level 2
if template:
	# Add the killstreak effect
    character.setKillsteakEffect(template, tf2.KillstreakColor.VillainousViolet)

##################################################
### Setup decapitation eye effect
##################################################
import characters
import items
import tf2

# Init effects
await items.initItems()

character = await characters.selectCharacter(tf2.Demoman) # Note: this also works on other classes
character.setDecapitationLevel(4)
