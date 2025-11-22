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

##################################################
### Generate thumbnails
##################################################
import characters
import items
import tf2
import engine
import loadout
import entities
import time
import source1

camera = entities.Camera.new(  # Create a camera
    {
        "position": [0, 200, 50],
        "parent": loadout.scene,
        "verticalFov": 10,
        "autoResize": True,
    }
)

# Create a control for the camera
orbitControl = entities.OrbitControl.new(camera)
orbitControl.target.setPosition([0, 0, 10])

# Create a scene to render the thumbnails
scene = entities.Scene.new(
    {
        "background": entities.ColorBackground.new(
            {"color": [0x21 / 255, 0x25 / 255, 0x2B / 255, 1]}
        )
    }
)
# scene.background = entities.ColorBackground.new({"color": [0x21 / 255, 0x25 / 255, 0x2B / 255, 1]})

# Remove the canvas if already existing
engine.Graphics.removeCanvas("thumbnails")

# Create a new canvas
canvas = engine.Graphics.addCanvas(
    {
        "name": "thumbnails",
        "layouts": [
            engine.CanvasLayout.new(
                "thumbnails",
                [
                    engine.CanvasView.new(
                        {
                            "name": "main",
                            "scene": scene,
                            "camera": camera,
                        }
                    ),
                ],
            ),
        ],
        "autoResize": False,
        "useLayout": "thumbnails",
        "width": 256,
        "height": 256,
    }
)

await source1.createParticleSystem("tf2", "superrare_greenenergy", scene)
time.sleep(2)
engine.Graphics.exportCanvas("thumbnails", "superrare_greenenergy.png")
