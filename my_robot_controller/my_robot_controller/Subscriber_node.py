#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class subscriber_node(Node):
    def __init__(self):
        super().__init__("Sub_node")
        self.subscriber_node_ = self.create_subscription(Float32, 'topic', self.data_callback, 10)
        self.get_logger().info("Ultra sonic data recieved")

    def data_callback(self, msg):
        data = msg.data
        if data < 5.0:
            self.get_logger().info("cold")
        elif data >= 5.0 and data < 10.0:
            self.get_logger().info("warm")
        else:
            self.get_logger().info("hot")
        



def main(args = None):
    rclpy.init(args = args)
    node = subscriber_node()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()