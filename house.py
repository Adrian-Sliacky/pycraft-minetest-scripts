import colorama
import minetest
import math
import time
from threading import Thread

"""INPUT"""
floors = 1  # min = 1
floor_height = 5  # min = 2
depth = 10  # min = 3
width = 10  # min = 3
torch_spacing = 6  # min = 1
flat_roof = False
claim_space = True
draw_from_center = False
plate_material = 'stone'
wall_material = 'wood_planks'
roof_material = 'wood_planks'
window_material = 'glass_pane'
torch_material = 'torch'
door_material = 'trapdoor'
"""INPUT"""

plate_height = 1
claim_gap = 3

inner_depth = depth - 2
inner_width = width - 2

"""block reqs."""
plate_req = plate_height * (floors + 1) * depth * width

circuit_req = ((2 * (depth + width)) - 4) * floors * floor_height

torch_req = 0
if floor_height > 2:
    for row in range(inner_depth):
        for th in range(inner_width):
            if th % torch_spacing == 0 and row % torch_spacing == 0:
                torch_req += 1
torch_req = torch_req * floors

if floor_height > 2:
    win_req = ((((floor_height - 2) * (width - 2)) * 2) * floors) - ((floor_height - 2) * (width - 2)) + (
            (((floor_height - 2) * (depth - 2)) * 2) * floors) + (
                      (((((floor_height - 2) * (math.floor((width - (
                          5 if width % 2 == 0 else 6)) / 2)))) if width > 6 else 0)) * 2)
else:
    win_req = 0

if width % 2 == 0:
    door_req = 2 * 2
else:
    door_req = 1 * 2

if flat_roof:
    roof_height = 0
    roof_req = 0
else:
    loc_height = 0
    roof_req = 0
    while True:
        loc_depth = depth - (2 * loc_height) + 2
        loc_width = width - (2 * loc_height) + 2

        if loc_depth < 1 or loc_width < 1:
            break

        roof_req += (loc_depth * loc_width)
        loc_height += 1
    roof_height = loc_height

if claim_space:
    if flat_roof:
        val = 0
    else:
        val = roof_height
    claim_space_req = (((floors * (floor_height + plate_height)) + val) + claim_gap) * (depth + (2 * claim_gap)) * (
            width + (2 * claim_gap))
else:
    claim_space_req = 0

req = claim_space_req + roof_req + win_req + plate_req + door_req + torch_req + circuit_req

"""block reqs. end"""
mt = minetest.Minetest(5, 0, (-(width / 2) + 1) if draw_from_center else 0, block_req=req)

test_time = mt.time_test()
time_estimate = test_time * req

mt.init_progressbar()

t1 = Thread(target=mt.progressbar_main)
t1.start()

start = time.time()
if claim_space:
    if flat_roof:
        val = 0
    else:
        val = roof_height
    mt.draw_cuboid(((floors * (floor_height + plate_height)) + val) + claim_gap, depth + (2 * claim_gap),
                   width + (2 * claim_gap),
                   x=-claim_gap, z=-claim_gap,
                   block_type='air')

curr_y = -plate_height
mt.draw_cuboid(plate_height, depth, width, y=curr_y, block_type=plate_material)
curr_y += plate_height
mt.draw_circuit(floor_height, depth, width, y=curr_y, block_type=wall_material)
curr_y += floor_height

if width % 2 == 0:
    mt.draw_cuboid(2, 1, 2, y=(curr_y - floor_height), z=(width / 2) - 1, block_type=door_material)
else:
    mt.draw_cuboid(2, 1, 1, y=(curr_y - floor_height), z=math.floor(width / 2), block_type=door_material)

mt.draw_cuboid(plate_height, depth, width, y=curr_y, block_type=plate_material)
curr_y += plate_height

for i in range(floors - 1):
    mt.draw_circuit(floor_height, depth, width, y=curr_y, block_type=wall_material)
    curr_y += floor_height
    mt.draw_cuboid(plate_height, depth, width, y=curr_y, block_type=plate_material)
    curr_y += plate_height

if floor_height > 2:
    for floor in range(floors):
        y_index = ((floor_height + plate_height) * (floor + 1)) - 2

        for row in range(inner_depth):
            for th in range(inner_width):
                if th % torch_spacing == 0 and row % torch_spacing == 0:
                    mt.block_rel(row + 1, y_index, th + 1, block_type=torch_material)

        # if width % 2 == 0:
        #     for row in range(torch_rows):
        #         for i in range(2):
        #             mt.block_rel(x=math.floor(depth / 2) + row, y=y_index,
        #                          z=(width / 2) + i - 1,
        #                          block_type=torch_material)
        # else:
        #     for row in range(torch_rows):
        #         mt.block_rel(x=math.floor(depth / 2) + row, y=y_index, z=math.floor(width / 2),
        #                      block_type=torch_material)
        """
        windows:
        """
        # front
        if floor > 0:
            mt.draw_cuboid(floor_height - 2, 1, width - 2, y=(floor_height + plate_height) * floor + 1, z=1,
                           block_type=window_material)
        elif width > 6:
            mt.draw_cuboid(floor_height - 2, 1, math.floor((width - (5 if width % 2 == 0 else 6)) / 2),
                           y=(floor_height + plate_height) * floor + 1, z=1,
                           block_type=window_material)

            mt.draw_cuboid(floor_height - 2, 1, math.floor((width - (5 if width % 2 == 0 else 6)) / 2),
                           y=(floor_height + plate_height) * floor + 1,
                           z=(4 if width % 2 == 0 else 5) + math.floor((width - (4 if width % 2 == 0 else 5)) / 2),
                           block_type=window_material)

        # back
        mt.draw_cuboid(floor_height - 2, 1, width - 2, x=depth - 1, y=(floor_height + plate_height) * floor + 1, z=1,
                       block_type=window_material)

        # left
        mt.draw_cuboid(floor_height - 2, depth - 2, 1, x=1, y=(floor_height + plate_height) * floor + 1,
                       block_type=window_material)

        # right
        mt.draw_cuboid(floor_height - 2, depth - 2, 1, x=1, y=(floor_height + plate_height) * floor + 1, z=width - 1,
                       block_type=window_material)

if not flat_roof:
    mt.draw_pyramid(depth + 2, width + 2, x=-1, y=curr_y, z=-1, block_type=roof_material)
end = time.time()

mt.progressbar_stop()
t1.join()

print(colorama.Fore.RESET)
# print(
#     f"""
#     block counter: {mt.block_counter}; code: {claim_space_req, roof_req, win_req, plate_req, door_req, torch_req,
#                                               circuit_req}
#                                         total code: {req}
#
#                                         diff: {req - mt.block_counter}
#
#                                         time: {end - start}
#
#                                         time_est: {time_estimate}
#
#                                         diff: {(((end - start) / time_estimate) - 1) * 100}%
#     """)
