##################################################
### Add a sentry model
##################################################
import source1
import loadout
import time

sentry = await source1.createModel(
    "tf2", "models/buildables/sentry3.mdl", loadout.scene
)
if sentry:
    sentry.playSequence("idle_off")
    sentry.setSkin(1)
    telescope_bone = sentry.getBoneByName("upper_telescope_01")
    if telescope_bone:
        telescope_bone.rotateY(10)

##################################################
### Add a sentry model
##################################################
import source1
import loadout
import time
import engine
import pyodide
import glmatrix
import math


# The handler function
def tick_handler(event):
    global telescope_bone
    telescope_bone.resetRotation()
    telescope_bone.rotateY(math.sin(event.detail.time * 0.001))


sentry = await source1.createModel(
    "tf2", "models/buildables/sentry3.mdl", loadout.scene
)
if sentry:
    sentry.playSequence("idle_off")
    sentry.setSkin(1)
    telescope_bone = sentry.getBoneByName("upper_telescope_01")
    if telescope_bone:
        engine.GraphicsEvents.addEventListener(
            "tick", pyodide.ffi.create_proxy(tick_handler)
        )
