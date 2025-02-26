from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    control = Node(
        package="control",
        executable="control",
        output = 'screen'
    )
    gait = Node(
        package="control",
        executable="gait_publisher",
        output = 'screen'
    )
    neck_control = Node(
        package="control",
        executable="neck_control",
        output = 'screen'
    )

    vision_node = Node(
        package="vision_pkg",
        executable="detect",
        output="screen"
    )

    gamecontroller = Node(
        package="game_controller",
        executable="connect",
        output="screen"
    )

    motors = Node(
        package="motors_pkg",
        executable="motors_communication",
        output="screen"
    )

    imu = Node(
        package="um7",
        executable="um7_node",
        output="screen"
    )


    ld.add_action(control)
    ld.add_action(gait)
    ld.add_action(neck_control)
    ld.add_action(vision_node)
    ld.add_action(gamecontroller)
    ld.add_action(motors)
    ld.add_action(imu)
    
    
    return ld