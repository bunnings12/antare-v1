
### File 2: firmware/swarm_cooperative_lift.py
```python
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import numpy as np

class CooperativeLift(Node):
    def __init__(self, drone_id):
        super().__init__(f'drone_{drone_id}')
        self.pub = self.create_publisher(Twist, f'/drone{drone_id}/cmd_vel', 10)
        self.timer = self.create_timer(0.05, self.control_loop)
        self.drone_id = drone_id
        self.target_height = 2.0
        self.payload_mass = 15.0 / 4.0  # 4 drones

    def control_loop(self):
        msg = Twist()
        # Super simple: proportional height + shared load
        error = self.target_height - 0.0  # replace with real pose later
        base_thrust = 9.81 * (4.0 + self.payload_mass/4.0)  # vehicle + share
        msg.linear.z = base_thrust + 3.0 * error
        self.pub.publish(msg)

def main():
    rclpy.init()
    node = CooperativeLift(drone_id=1)  # spawn 4 instances externally
    rclpy.spin(node)

if __name__ == '__main__':
    main()
