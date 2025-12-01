from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    config_path_arg = DeclareLaunchArgument(
        "config_path",
        default_value=get_package_share_directory("transducer_imu_ros_driver")
        + "/params.yaml",
        description="config path",
    )

    imu_node = Node(
        package="transducer_imu_ros_driver",
        executable="transducer_m_imu",
        name="transducer_imu",
        output="screen",
        parameters=[LaunchConfiguration("config_path")],
    )

    return LaunchDescription([config_path_arg, imu_node])
