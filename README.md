# Interactive Wall

The Interactive Wall is a projector-based multi-touch interface. A projector displays an appli-
cation on a flat wall or matte surface. The RPLIDAR C1 is mounted at the base or side of the
wall, scanning a thin horizontal plane parallel to the wall surface. When a user places a finger on
the wall, the finger enters the laser scan plane and appears as an object significantly closer than
the wall baseline. The software detects this intrusion, identifies its position in physical space,
maps it to screen coordinates, and injects it into the operating system as a genuine touch event.
The PC application responds exactly as if the user touched a real touchscreen.

## System Overview
A sensor mounted at the wall base detects finger intrusions via baseline subtraction. Detected touch coordinates are mapped to screen space using a homography transform and injected into the Linux kernel as genuine multitouch events. A ML gesture classifier built on PyTorch adds swipe, tap, hold, and multi-finger recognition in real time.

## Hardware

- RPLIDAR C1 laser scanner (10Hz, 360°, up to 12m range)
- Standard PC running Ubuntu 24.04 LTS
- Projector (any resolution, tested at 1920×1080)

## Software Stack

- **ROS 2 Jazzy** — sensor driver and node communication
- **sllidar_ros2** — official Slamtec C1 driver
- **Python 3.12** — all processing, ML, and application layers
- **PyQt6** — demo visualization GUI
- **OpenCV** — homography calibration
- **PyTorch** — gesture recognition model
- **uinput** — OS touch event injection

## Project Phases

- [x] Phase 1 — Demo app (wall_grabber.py) with real-time scan visualization
- [ ] Phase 2 — ROS 2 architecture with touch detection and uinput injection
- [ ] Phase 3 — ML gesture recognition layer
- [ ] Phase 4 — Projected interactive application
- [ ] Phase 5 — Final integration, optimization, and demo preparation

## Quick Start

```bash
# Terminal 1 — LiDAR driver
ros2 launch sllidar_ros2 sllidar_c1_launch.py

# Terminal 2 — Touch detector
ros2 run wall_touch touch_detector

# Terminal 3 — uinput injector
sudo ros2 run wall_touch uinput_injector

# Demo app (standalone, no ROS 2 required)
cd demo && python3 wall_grabber.py
```

## Author

Rayhane Nouri — Embedded Software Engineer
