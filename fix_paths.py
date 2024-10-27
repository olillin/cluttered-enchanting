from beet import Context

def beet_default(ctx: Context):
    for pack in ctx.packs:
        if not pack.name == "src":
            continue
        
        block_tags = ctx.data.overlays["post_1_21"].block_tags
        tag = block_tags["minecraft:enchantment_power_transmitter"]
        pack.extra['post_1_21/data/minecraft/tags/block/enchantment_power_transmitter.json'] = tag
        del block_tags["minecraft:enchantment_power_transmitter"]