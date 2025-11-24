##################################################
### Set a warpaint on a weapon
##################################################
import items
import characters
import tf2
import math

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
        "orientation": [0, 0, 0, 1],
    },
    172: {  # Scotsman's Skullcutter
        "position": [25, 0, 10],
        "orientation": [0, 0, 1, 1],
    },
    194: {  # knife
        "position": [-95, 0, -24],
        "orientation": [0, 0, 0, 1],
    },
    197: {  # wrench
        "position": [-92, 0, 18],
        "orientation": [0, 0, 0, 1],
    },
    199: {  # shotgun
        "position": [-75, 0, 109],
        "orientation": [0, 0, 0, 1],
    },
    200: {  # scattergun
        "position": [-116, 0, 63],
        "orientation": [0, 0, 0, 1],
    },
    201: {  # sniper rifle
        "position": [-32, 0, 103],
        "orientation": [0, 0, 0, 1],
    },
    202: {  # minigun
        "position": [-34, 0, -26],
        "orientation": [0, 0, 0, 1],
    },
    203: {  # smg
        "position": [-70.5, 0, 77],
        "orientation": [0, 0, 0, 1],
    },
    205: {  # rocket launcher
        "position": [-2, 0, 77],
        "orientation": [0, 0, 0, 1],
    },
    206: {  # grenade launcher
        "position": [-109, 0, 5],
        "orientation": [0, 0, 0, 1],
    },
    207: {  # sticky launcher
        "position": [-49, 0, 11],
        "orientation": [0, 0, 0, 1],
    },
    208: {  # flamethrower
        "position": [28, 0, -44],
        "orientation": [0, 0, 0, 1],
    },
    209: {  # pistol
        "position": [-20, 0, 68],
        "orientation": [0, 0, 0, 1],
    },
    210: {  # revolver
        "position": [-14, 0, 54],
        "orientation": [0, 0, 0, 1],
    },
    211: {  # medigun
        "position": [3, 0, 63],
        "orientation": [0, 0, 0, 1],
    },
    214: {  # powerjack
        "position": [87, 0, -24],
        "orientation": [0, 0, 0, 1],
    },
    215: {  # degreaser
        "position": [-89, 0, -8],
        "orientation": [0, 0, 0, 1],
    },
    220: {  # shortstop
        "position": [-88, 0, 82],
        "orientation": [0, 0, 0, 1],
    },
    221: {  # holy mackerel
        "position": [-104, 0, 18],
        "orientation": [0, 0, 0, 1],
    },
    228: {  # black box
        "position": [6, 0, -15],
        "orientation": [0, 0, 0, 1],
    },
    304: {  # amputator
        "position": [30, 0, -8],
        "orientation": [0, 0, 0, 1],
    },
    305: {  # crusader crossbow
        "position": [-109, 0, 49],
        "orientation": [0, 0, 0, 1],
    },
    308: {  # loch n load
        "position": [45, 0, -24],
        "orientation": [0, 0, 0, 1],
    },
    312: {  # brass beast
        "position": [-49, 0, 50],
        "orientation": [0, 0, 0, 1],
    },
    326: {  # back scratcher
        "position": [-80, 0, 40],
        "orientation": [0, 0, 1, 1],
    },
    327: {  # Claidheamohmor
        "position": [41, 0, 14],
        "orientation": [0, 0, 1, 1],
    },
    329: {  # jag
        "position": [-120, 0, 18],
        "orientation": [0, 0, 0, 1],
    },
    351: {  # detonator
        "position": [-60, 0, 60],
        "orientation": [0, 0, 0, 1],
    },
    401: {  # Shahanshah
        "position": [-115, 0, -33],
        "orientation": [0, -1, 0, 1],
    },
    402: {  # bazaar bargain
        "position": [-24, 0, 93],
        "orientation": [0, 0, 0, 1],
    },
    404: {  # persian persuader
        "position": [-68, 0, 17],
        "orientation": [0, 0, -1, 1],
    },
    415: {  # reserve shooter
        "position": [-113, 0, -50],
        "orientation": [0, 0, 0, 1],
    },
    424: {  # tomislav
        "position": [-116, 0, 107],
        "orientation": [0, 0, 0, 1],
    },
    425: {  # family business
        "position": [43, 0, 104],
        "orientation": [0, 0, 0, 1],
    },
    447: {  # disciplinary action
        "position": [30, 0, 4],
        "orientation": [0, 0, 0, 1],
    },
    448: {  # soda popper
        "position": [-63, 0, -29],
        "orientation": [0, 0, 0, 1],
    },
    449: {  # winger
        "position": [19, 0, 71],
        "orientation": [0, 0, 0, 1],
    },
    740: {  # scorch shot
        "position": [61, 0, -8],
        "orientation": [0, 0, 0, 1],
    },
    996: {  # loose canon
        "position": [63, 0, 52],
        "orientation": [0, 0, 0, 1],
    },
    997: {  # rescue ranger
        "position": [54.4, 0, 35],
        "orientation": [0, 0, 0, 1],
    },
    1104: {  # air strike
        "position": [-58, 0, -42],
        "orientation": [0, 0, 0, 1],
    },
    1151: {  # iron bomber
        "position": [60, 0, 69],
        "orientation": [0, 0, 0, 1],
    },
    1153: {  # panic attack
        "position": [59.4, 0, 23],
        "orientation": [0, 0, 0, 1],
    },
    1178: {  # dragon's fury
        "position": [25, 0, 87],
        "orientation": [0, 0, 0, 1],
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

            item.setWarpaint(303, 0, 0)

            if model:
                model.setPosition(pos["position"])
                model.setOrientation(pos["orientation"])

                if character_id == 1 and not pos.get("rotate_z", True) == False:
                    model.rotateGlobalZ(math.pi)

await setup_weapons(0)
await setup_weapons(1)
