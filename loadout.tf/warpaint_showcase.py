##################################################
### Set a warpaint on a weapon
##################################################
import items
import characters
import tf2
import math
import entities
import loadout

await items.initItems()

empty_characters = [None, None]
characters.setSlotsCount(2)
for i in range(2):
    slot = characters.getSlot(i)
    if slot:
        slot.setPosition([i * 200 - 100, 0, 0])
        slot.setOrientation([0, 0, 0, 1])
        empty_characters[i] = await characters.selectCharacter(tf2.Empty, i)

weapons = {
    37: {  # ubersaw
        "position": [53, 0, 9],
    },
    172: {  # Scotsman's Skullcutter
        "position": [24, 0, 10],
        "orientation": [0, 0, 1, 1],
    },
    194: {  # knife
        "position": [-95, 0, -24],
        "orientation": [0, 0, 1, 0],
    },
    197: {  # wrench
        "position": [-92, 0, 18],
        "orientation": [0, 0, 1, 0],
    },
    199: {  # shotgun
        "position": [-75, 0, 109],
    },
    200: {  # scattergun
        "position": [-116, 0, 63],
    },
    201: {  # sniper rifle
        "position": [-32, 0, 103],
    },
    202: {  # minigun
        "position": [-34, 0, -26],
    },
    203: {  # smg
        "position": [-70.5, 0, 77],
    },
    205: {  # rocket launcher
        "position": [-2, 0, 77],
    },
    206: {  # grenade launcher
        "position": [-109, 0, 5],
    },
    207: {  # sticky launcher
        "position": [-49, 0, 11],
    },
    208: {  # flamethrower
        "position": [28, 0, -44],
    },
    209: {  # pistol
        "position": [-20, 0, 68],
    },
    210: {  # revolver
        "position": [-14, 0, 54],
    },
    211: {  # medigun
        "position": [3, 0, 63],
    },
    214: {  # powerjack
        "position": [90, 0, -24],
        "orientation": [0, 0, 1, 0],
    },
    215: {  # degreaser
        "position": [-89, 0, -8],
    },
    220: {  # shortstop
        "position": [-88, 0, 82],
    },
    221: {  # holy mackerel
        "position": [-107, 0, 18],
        "orientation": [0, 0, 0.4, -0.9],
    },
    228: {  # black box
        "position": [6, 0, -15],
    },
    304: {  # amputator
        "position": [30, 0, -8],
    },
    305: {  # crusader crossbow
        "position": [-109, 0, 49],
    },
    308: {  # loch n load
        "position": [45, 0, -24],
    },
    312: {  # brass beast
        "position": [-49, 0, 50],
    },
    326: {  # back scratcher
        "position": [-80, 0, 40],
        "orientation": [0, 0, -1, 1],
    },
    327: {  # Claidheamohmor
        "position": [42, 0, 14],
        "orientation": [0, 0, 1, 1],
    },
    329: {  # jag
        "position": [-117, 0, 18],
        "orientation": [0, 0, 1, 0],
    },
    351: {  # detonator
        "position": [-60, 0, 60],
    },
    401: {  # Shahanshah
        "position": [-115, 0, -33],
        "orientation": [1, 0, 1, 0],
    },
    402: {  # bazaar bargain
        "position": [-24, 0, 93],
    },
    404: {  # persian persuader
        "position": [-66, 0, 15],
        "orientation": [0, 0, -1, -1],
    },
    415: {  # reserve shooter
        "position": [-113, 0, -50],
    },
    424: {  # tomislav
        "position": [-116, 0, 107],
    },
    425: {  # family business
        "position": [43, 0, 104],
    },
    447: {  # disciplinary action
        "position": [31, 0, 4],
        "orientation": [0, 0, -0.36, -0.93],
    },
    448: {  # soda popper
        "position": [-63, 0, -29],
    },
    449: {  # winger
        "position": [19, 0, 71],
    },
    740: {  # scorch shot
        "position": [61, 0, -8],
    },
    996: {  # loose canon
        "position": [63, 0, 52],
    },
    997: {  # rescue ranger
        "position": [54.4, 0, 35],
    },
    1104: {  # air strike
        "position": [-58, 0, -42],
    },
    1151: {  # iron bomber
        "position": [60, 0, 69],
    },
    1153: {  # panic attack
        "position": [59.4, 0, 23],
    },
    1178: {  # dragon's fury
        "position": [25, 0, 87],
    },
    9536: {  # Paintkit
        "position": [0, 0, 0],
        "orientation": [0, 0, 1, 0],
        "rotate_z": False,
    },
}


async def setup_weapons(character_id):
    character = empty_characters[character_id]
    for x in weapons:
        pos = weapons[x]
        print(pos)

        if character_id == 1:
            pos["position"][0] = -pos["position"][0]

        template = items.getItemTemplate(x)
        if template:

            item = await character.addItem(template)
            model = await item.getModel()

            item.setWarpaint(303, 4, 123456)

            if model:
                model.setPosition(pos["position"])
                model.setOrientation(pos.get("orientation", [0, 0, 0, 1]))

                if character_id == 1 and not pos.get("rotate_z", True) == False:
                    model.rotateGlobalZ(math.pi)


await setup_weapons(0)
await setup_weapons(1)

entities.Text3D.new(
    {"text": "Offside", "parent": loadout.scene, "position": [-140, 0, 125], "size": 20}
)
entities.Text3D.new(
    {"text": "Playside", "parent": loadout.scene, "position": [55, 0, 125], "size": 20}
)
