import time
import progressbar_mt
import pycraft_minetest as pm
from pycraft_minetest import blocklist as bl


class Minetest:
    # BLOCKS

    air = bl.AIR.id
    stone = bl.STONE.id
    grass = bl.GRASS.id
    dirt = bl.DIRT.id
    cobblestone = bl.COBBLESTONE.id
    wood_planks = bl.WOOD_PLANKS.id
    sapling = bl.SAPLING.id
    bedrock = bl.BEDROCK.id
    water_flowing = bl.WATER_FLOWING.id
    water = bl.WATER.id
    water_stationary = bl.WATER_STATIONARY.id
    lava_flowing = bl.LAVA_FLOWING.id
    lava = bl.LAVA.id
    lava_stationary = bl.LAVA_STATIONARY.id
    sand = bl.SAND.id
    gravel = bl.GRAVEL.id
    gold_ore = bl.GOLD_ORE.id
    iron_ore = bl.IRON_ORE.id
    coal_ore = bl.COAL_ORE.id
    wood = bl.WOOD.id
    leaves = bl.LEAVES.id
    glass = bl.GLASS.id
    lapis_lazuli_ore = bl.LAPIS_LAZULI_ORE.id
    lapis_lazuli = bl.LAPIS_LAZULI_BLOCK.id
    sandstone = bl.SANDSTONE.id
    bed = bl.BED.id
    cobweb = bl.COBWEB.id
    grass_tall = bl.GRASS_TALL.id
    wool = bl.WOOL.id
    flower_yellow = bl.FLOWER_YELLOW.id
    flower_cyan = bl.FLOWER_CYAN.id
    mushroom_brown = bl.MUSHROOM_BROWN.id
    mushroom_red = bl.MUSHROOM_RED.id
    gold = bl.GOLD_BLOCK.id
    iron = bl.IRON_BLOCK.id
    stone_slab_double = bl.STONE_SLAB_DOUBLE.id
    stone_slab = bl.STONE_SLAB.id
    brick = bl.BRICK_BLOCK.id
    tnt = bl.TNT.id
    bookshelf = bl.BOOKSHELF.id
    moss_stone = bl.MOSS_STONE.id
    obsidian = bl.OBSIDIAN.id
    torch = bl.TORCH.id
    fire = bl.FIRE.id
    stairs_wood = bl.STAIRS_WOOD.id
    chest = bl.CHEST.id
    diamond_ore = bl.DIAMOND_ORE.id
    diamond = bl.DIAMOND_BLOCK.id
    crafting_table = bl.CRAFTING_TABLE.id
    farmland = bl.FARMLAND.id
    furnace_inactive = bl.FURNACE_INACTIVE.id
    furnace_active = bl.FURNACE_ACTIVE.id
    door_wood = bl.DOOR_WOOD.id
    ladder = bl.LADDER.id
    stairs_cobblestone = bl.STAIRS_COBBLESTONE.id
    door_iron = bl.DOOR_IRON.id
    redstone_ore = bl.REDSTONE_ORE.id
    ice = bl.ICE.id
    snow = bl.SNOW_BLOCK.id
    cactus = bl.CACTUS.id
    clay = bl.CLAY.id
    sugar_cane = bl.SUGAR_CANE.id
    fence = bl.FENCE.id
    glowstone = bl.GLOWSTONE_BLOCK.id
    stone_brick = bl.STONE_BRICK.id
    glass_pane = bl.GLASS_PANE.id
    melon = bl.MELON.id
    fence_gate = bl.FENCE_GATE.id
    glowing_obsidian = bl.GLOWING_OBSIDIAN.id
    nether_reactor_core = bl.NETHER_REACTOR_CORE.id

    trapdoor = 167

    my_blocks = {
        'air': air,
        'stone': stone,
        'grass': grass,
        'dirt': dirt,
        'cobblestone': cobblestone,
        'wood_planks': wood_planks,
        'sapling': sapling,
        'bedrock': bedrock,
        'water_flowing': water_flowing,
        'water': water,
        'water_stationary': water_stationary,
        'lava_flowing': lava_flowing,
        'lava': lava,
        'lava_stationary': lava_stationary,
        'sand': sand,
        'gravel': gravel,
        'gold_ore': gold_ore,
        'iron_ore': iron_ore,
        'coal_ore': coal_ore,
        'wood': wood,
        'leaves': leaves,
        'glass': glass,
        'lapis_lazuli_ore': lapis_lazuli_ore,
        'lapis_lazuli': lapis_lazuli,
        'sandstone': sandstone,
        'bed': bed,
        'cobweb': cobweb,
        'grass_tall': grass_tall,
        'wool': wool,
        'flower_yellow': flower_yellow,
        'flower_cyan': flower_cyan,
        'mushroom_brown': mushroom_brown,
        'mushroom_red': mushroom_red,
        'gold': gold,
        'iron': iron,
        'stone_slab_double': stone_slab_double,
        'stone_slab': stone_slab,
        'brick': brick,
        'tnt': tnt,
        'bookshelf': bookshelf,
        'moss_stone': moss_stone,
        'obsidian': obsidian,
        'torch': torch,
        'fire': fire,
        'stairs_wood': stairs_wood,
        'chest': chest,
        'diamond_ore': diamond_ore,
        'diamond': diamond,
        'crafting_table': crafting_table,
        'farmland': farmland,
        'furnace_inactive': furnace_inactive,
        'furnace_active': furnace_active,
        'door_wood': door_wood,
        'ladder': ladder,
        'stairs_cobblestone': stairs_cobblestone,
        'door_iron': door_iron,
        'redstone_ore': redstone_ore,
        'ice': ice,
        'snow': snow,
        'cactus': cactus,
        'clay': clay,
        'sugar_cane': sugar_cane,
        'fence': fence,
        'glowstone': glowstone,
        'stone_brick': stone_brick,
        'glass_pane': glass_pane,
        'melon': melon,
        'fence_gate': fence_gate,
        'glowing_obsidian': glowing_obsidian,
        'nether_reactor_core': nether_reactor_core,
        'trapdoor': trapdoor
    }

    def __init__(self, x_prefix=0, y_prefix=0, z_prefix=0, bot_enabled=False, block='diamond', block_req=None):
        self.block = block
        if bot_enabled:
            self.bot = pm.Turtle(self.my_blocks[self.block])  # material
            self.bot.speed(12)  # max = 12
            self.bot.move(0, 0, 0)

        player_pos = pm.where(pm.player)
        self.player_x = player_pos.x
        self.player_y = player_pos.y
        self.player_z = player_pos.z

        self.x_prefix = x_prefix
        self.y_prefix = y_prefix
        self.z_prefix = z_prefix

        self.block_counter = 0
        self.block_req = block_req
        if self.block_req is not None:
            self.pb = progressbar_mt.ProgressBar(self.block_req)

    def init_progressbar(self):
        if self.block_req is not None:
            self.pb.start_pbar()

    def progressbar_main(self):
        if self.block_req is not None:
            self.pb.main()

    def progressbar_stop(self):
        if self.block_req is not None:
            self.pb.running = False

    def opt_block(self, blck):
        if blck is None:
            return self.block
        else:
            return blck

    def move_rel(self, x=0, y=0, z=0):

        bot_x_pref = self.x_prefix + self.player_x
        bot_y_pref = self.y_prefix + self.player_y
        bot_z_pref = self.z_prefix + self.player_z

        self.bot.goto(x + bot_x_pref, y + bot_y_pref, z + bot_z_pref)

    def block_rel(self, x=0, y=0, z=0, block_type=None, use_block_id=False, count_blocks=True):
        if not use_block_id:
            my_block = self.opt_block(block_type)
        else:
            my_block = block_type

        block_x_pref = self.x_prefix + self.player_x
        block_y_pref = self.y_prefix + self.player_y
        block_z_pref = self.z_prefix + self.player_z

        pm.block(self.my_blocks[my_block] if not use_block_id else my_block, x + block_x_pref, y + block_y_pref,
                 z + block_z_pref, True)
        if count_blocks:
            self.block_counter += 1
            if self.block_req is not None:
                self.pb.set_progress(self.block_counter)

    def time_test(self, x=20, y=-500, z=-20):
        start = time.time()
        self.draw_cuboid(10, 10, 10, x=x, y=y, z=z, count_blocks=False)
        end = time.time()
        return (end - start) / 1000

    def draw_cuboid(self, h, d, w, x=0, y=0, z=0, block_type=None, count_blocks=True):
        my_block = self.opt_block(block_type)

        for height in range(h):
            for depth in range(d):
                for width in range(w):
                    self.block_rel(depth + x, height + y, width + z, my_block, count_blocks=count_blocks)

    def draw_circuit(self, h, d, w, x=0, y=0, z=0, block_type=None):
        my_block = self.opt_block(block_type)

        for height in range(h):
            for depth in range(d):
                for width in range(w):
                    if width % w == 0 or depth % d == 0:
                        self.block_rel(depth + x, height + y, width + z, my_block)
                    elif (width == (0 or w - 1)) or (depth == (0 or d - 1)):
                        self.block_rel(depth + x, height + y, width + z, my_block)

    def draw_from_array(self, array, depth=1, x=0, y=0, z=0, draw_vertical=True, pos_prefix=0):
        if pos_prefix > 0:
            spacing = 1
        else:
            spacing = 0
        for i_depth in range(depth):
            for i_row, row in enumerate(array[::-1]):
                for i_val, val in enumerate(row):
                    if val == 1:
                        expression = i_row + ((pos_prefix + spacing) * -1)
                        self.block_rel((expression + x) if not draw_vertical else (i_depth + x),
                                       (i_depth + y) if not draw_vertical else (expression + y),
                                       i_val + z, count_blocks=False)
        if pos_prefix > 1:
            return len(array) + 1
        else:
            return len(array)

    def draw_pyramid(self, d, w, x=0, y=0, z=0, block_type=None):
        my_block = self.opt_block(block_type)

        height = 0
        while True:
            depth = d - (2 * height)
            width = w - (2 * height)

            if depth < 1 or width < 1:
                break
            self.draw_cuboid(1, depth, width, height + x, height + y, height + z, my_block)
            height += 1

    def move_forward(self, distance=0):
        self.bot.forward(distance)

    def bot_disappear(self, x=0, y=0, z=500):
        self.bot.move(x, y, -z)
