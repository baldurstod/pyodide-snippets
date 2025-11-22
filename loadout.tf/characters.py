##################################################
### Add a character
##################################################
import characters
import tf2

character = await characters.selectCharacter(
    tf2.Scout  # a number can be also be used: 0-9 for humans, 100-109 for bots
)

##################################################
### Change the team
##################################################
import characters
import tf2

character = await characters.selectCharacter(tf2.Scout)
character.setTeam(tf2.Blu)  # default team is Red

##################################################
### Set invulnerable
##################################################
import characters
import tf2

character = await characters.selectCharacter(tf2.Scout)
character.setInvulnerable(True)

##################################################
### Gold / ice ragdoll
##################################################
import characters
import tf2

character = await characters.selectCharacter(tf2.Scout)
character.setRagdoll(tf2.GoldRagdoll)
# character.setRagdoll(tf2.IceRagdoll)
# character.setRagdoll(None)

##################################################
### Several characters method 1
##################################################
import characters
import tf2

characters.useDisposition(3)
for i in range(3):
    await characters.selectCharacter(tf2.Scout)

##################################################
### Several characters method 2
##################################################
import characters
import tf2

characters.setSlotsCount(3)
# When we use setSlotsCount, we have to position each slot
for i in range(3):
    slot = characters.getSlot(i)
    if slot:
        slot.setPosition([i * 50 - 50, 0, 0])
        await characters.selectCharacter(tf2.Scout, i)

##################################################
### Remove a character
##################################################
import characters
import tf2
import time

characters.setSlotsCount(3)
# When we use setSlotsCount, we have to position each slot
for i in range(3):
    slot = characters.getSlot(i)
    if slot:
        slot.setPosition([i * 50 - 50, 0, 0])
        await characters.selectCharacter(tf2.Scout, i)

time.sleep(2)
characters.removeCharacter(1)

##################################################
### Copy the current character
##################################################
import characters
import tf2
import time

characters.useDisposition(2)  # Add a second slot
character_from = characters.getCurrentCharacter()
if character_from:
    # Create a second character with the class of the first
    character_to = await characters.selectCharacter(character_from.characterClass)
    character_to.setTeam(tf2.Blu)
    character_to.copy(character_from)  # Copy items, effects, ...

##################################################
### Set pose parameter
##################################################
import characters
import tf2

character = await characters.selectCharacter(tf2.Scout)
character.setUserAnim("run_primary")
# Other parameters are: move_y, body_yaw, body_pitch, r_arm, r_hand_grip
character.setPoseParameter("move_x", 1)
template = items.getItemTemplate(200)
if template:
    item = await character.addItem(template)
