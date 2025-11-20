##################################################
### Add a secondary view
##################################################
import loadout
import engine
import entities
import characters
import tf2

character = await characters.selectCharacter(tf2.Demoman)
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
orbitControl.target.setPosition([0, 0, 50])

canvas = loadout.getCanvas()  # Get the loadout rendering canvas
layout = canvas.getLayout("loadout")  # Get the canvas regular layout
layout.addView(  # Add a view to this layout
    engine.CanvasView.new(
        {
            "name": "secondary",  # Name must be unique in this layout
            "scene": loadout.scene,  # We use the regular scene for this view
            "camera": camera,  # Use the camera we created above
            "clearDepth": True,
            "viewport": engine.Viewport.new(  # Set the viewport to be the bottom left ninth
                {
                    "x": 0,
                    "y": 0,
                    "width": 1 / 3,
                    "height": 1 / 3,
                }
            ),
        }
    )
)
