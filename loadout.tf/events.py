##################################################
### Run a function at each tick
##################################################
import characters
import items
import tf2
import engine
import pyodide

kills = 0

# The handler function
def tick_handler(event):
    global kills
    item.setStatClock(kills)
    kills += 1


await items.initItems()
character = await characters.selectCharacter(tf2.Demoman)
template = items.getItemTemplate(206)  # gl
if template:
    item = await character.addItem(template)

# Setup a listener
engine.GraphicsEvents.addEventListener("tick", pyodide.ffi.create_proxy(tick_handler))
