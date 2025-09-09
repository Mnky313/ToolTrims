TOOLS = [
    "wooden_pickaxe",
    "stone_pickaxe",
    "iron_pickaxe",
    "golden_pickaxe",
    "diamond_pickaxe",
    "netherite_pickaxe",
    "wooden_pickaxe",
    "stone_axe",
    "iron_axe",
    "golden_axe",
    "diamond_axe",
    "netherite_axe",
    "wooden_shovel",
    "stone_shovel",
    "iron_shovel",
    "golden_shovel",
    "diamond_shovel",
    "netherite_shovel",
    "wooden_hoe",
    "stone_hoe",
    "iron_hoe",
    "golden_hoe",
    "diamond_hoe",
    "netherite_hoe",
    "wooden_sword",
    "stone_sword",
    "iron_sword",
    "golden_sword",
    "diamond_sword",
    "netherite_sword"
]
TRIMS = [
    "bolt",
    "coast",
    "dune",
    "eye",
    "flow",
    "host",
    "raiser",
    "rib",
    "sentry",
    "shaper",
    "silence",
    "snout",
    "spire",
    "tide",
    "vex",
    "ward",
    "wayfinder",
    "wild"
]
RESOURCES = [
    "quartz",
    "netherite_ingot",
    "redstone",
    "copper_ingot",
    "gold_ingot",
    "emerald",
    "diamond",
    "lapis_lazuli",
    "amethyst_shard",
    "iron_ingot",
    "resin_brick"
]



for tool in TOOLS:
    for trim in TRIMS:
        for resource in RESOURCES:
            resource_name = resource.split("_")[0]
            if "bow" not in tool:
                tool_type = tool.split("_")[1]
            else:
                tool_type = tool
            with open(f'ToolTrims_RP/assets/katzteam/models/item/{tool}_{trim}_{resource_name}.json','w') as out:
                out.write(f'''{{
    "parent": "minecraft:item/generated",
    "textures": {{
        "layer0": "minecraft:item/{tool}",
        "layer1": "katzteam:item/{tool_type}_{trim}_{resource_name}"
    }}
}}''')
            with open(f'ToolTrims_RP/assets/katzteam/items/{tool}_{trim}_{resource_name}.json','w') as out:
                out.write(f'''{{
    "model": {{
        "type": "minecraft:model",
        "model": "katzteam:item/{tool}_{trim}_{resource_name}"
    }}
}}''')
            # Only generate recipes for bow/crossbow once, don't include _pulling
            if "bow_p" not in tool:
                with open(f'ToolTrims_DP/data/katzteam/recipe/{tool}_{trim}_{resource_name}.json','w') as out:
                    out.write(f'''{{
    "type": "minecraft:smithing_transform",
    "template": "minecraft:{trim}_armor_trim_smithing_template",
    "base": "minecraft:{tool}",
    "addition": "minecraft:{resource}",
    "result": {{
        "id": "minecraft:{tool}",
        "components": {{
            "minecraft:item_model": "katzteam:{tool}_{trim}_{resource_name}"
        }}
    }}
}}''')