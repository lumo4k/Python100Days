# def rotate():
#     turn_left()
#     turn_left()
#
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# while not at_goal():
#     if wall_in_front() and not wall_on_right():
#         turn_right()
#     elif wall_in_front() and wall_on_right():
#         turn_left()
#         if wall_in_front():
#             turn_left()
#             move()
#             rotate()
#             build_wall()
#
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()