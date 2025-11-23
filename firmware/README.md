# Firmware – Cooperative Lift Demo (runs today)

This is the first real code for Antares 🟥.

## What it does
- Spawns 4 virtual drones in Gazebo  
- Attaches a 15 kg payload with cables  
- Runs simple decentralized force-sharing controller  
- Holds the payload stable at 2 m height  

## Run in <5 min (Ubuntu 22.04/24.04 tested)
```bash
git clone https://github.com/bunnings12/antare-v1
cd antare-v1/firmware
./install_deps.sh    # (coming in next commit)
ros2 launch swarm_cooperative_lift demo.launch.py
