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
