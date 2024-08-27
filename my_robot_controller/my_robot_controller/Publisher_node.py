#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class publisher_node(Node):
    def __init__(self):
        super().__init__("Pub_node")
        self.cmd_vel_pub_ = self.create_publisher(Float32, 'topic', 10)
        self.timer = self.create_timer(1, self.send_sensor_data)
        self.get_logger().info("Ultra sonic data sent")
        self.count = 0.0

    def send_sensor_data(self):
        msg = Float32()
        msg.data = self.count
        self.cmd_vel_pub_.publish(msg)
        self.count += 1

def main(args = None):
    rclpy.init(args = args)
    node = publisher_node()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()