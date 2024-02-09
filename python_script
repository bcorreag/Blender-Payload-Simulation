import bpy


# assigning each object a variable name
#flywheel_bottom = bpy.context.scene.objects["Flywheel Bottom"]
#Flywheel_top = bpy.context.scene.objects["Flywheel Top"]
#Ground = bpy.context.scene.objects["Ground"]
#Hinge_bottom = bpy.context.scene.objects["Hinge Bottom"]
#hinge_top = bpy.context.scene.objects["Hinge Top"]
#motor_bottom = bpy.context.scene.objects["Motor_Bottom"]
#motor_top = bpy.context.scene.objects["Motor_top"]
#payload_assembly = bpy.context.scene.objects["Payload Assembly"]
#Payload_hinge = bpy.context.scene.objects["Payload Hinge"]
#Sphere = bpy.context.scene.objects["Sphere"]
#TOP = bpy.context.scene.objects["TOP"]


w1 = 10
w2 = 0

#jump to frame = 0
bpy.ops.screen.frame_jump(end=False)

# angular velocity of bottom motor
bpy.data.objects["Motor_Bottom"].rigid_body_constraint.motor_ang_target_velocity = w1

# angular velocity of top motor
bpy.data.objects["Motor_top"].rigid_body_constraint.motor_ang_target_velocity = w2

 
def timefunc():   
    w1=1
    w2=10
    bpy.data.objects["Motor_Bottom"].rigid_body_constraint.motor_ang_target_velocity = w1
    bpy.data.objects["Motor_top"].rigid_body_constraint.motor_ang_target_velocity = w2
    return None
bpy.app.timers.register(timefunc, first_interval=5)

 
def timefunc():   
    w1=1
    w2=0
    bpy.data.objects["Motor_Bottom"].rigid_body_constraint.motor_ang_target_velocity = w1
    bpy.data.objects["Motor_top"].rigid_body_constraint.motor_ang_target_velocity = w2
    return None
bpy.app.timers.register(timefunc, first_interval=7)



# playing animation
bpy.ops.screen.animation_play()
