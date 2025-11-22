##################################################
### Add a particle system
##################################################
import source1
import loadout

await source1.createParticleSystem("tf2", "superrare_greenenergy", loadout.scene)

##################################################
### Attach a particle system to a bone
##################################################
import source1
import loadout

sentry = await source1.createModel(
    "tf2", "models/buildables/sentry3.mdl", loadout.scene
)
if sentry:
    sentry.playSequence("idle_off")

    muzzle_l = sentry.getAttachment("muzzle_l")
    if muzzle_l:
        await source1.createParticleSystem("tf2", "superrare_greenenergy", muzzle_l)

    muzzle_r = sentry.getAttachment("muzzle_r")
    if muzzle_r:
        await source1.createParticleSystem("tf2", "superrare_greenenergy", muzzle_r)

##################################################
### Attach a muzzle effect
##################################################
import source1
import loadout
import characters
import items
import tf2

await items.initItems()
character = await characters.selectCharacter(tf2.Pyro)

template = items.getItemTemplate(208)  # flamethrower
# Add an item
item = await character.addItem(template)
# Get the item model
model = await item.getModel()
# Get the muzzle attachment
muzzle = model.getAttachment("muzzle")
# Create the effect an parent it to the attachment
await source1.createParticleSystem("tf2", "flamethrower_halloween", muzzle)
