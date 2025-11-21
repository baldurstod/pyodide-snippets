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
#character.setRagdoll(tf2.IceRagdoll)
#character.setRagdoll(None)
