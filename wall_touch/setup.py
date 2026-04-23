from setuptools import find_packages, setup
import os 
from glob import glob 
package_name = 'wall_touch'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),(os.path.join('share', package_name, 'launch'),
            glob('launch/*.py')),
        (os.path.join('share', package_name, 'config'),
            glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rayhanenouri',
    maintainer_email='rayhane.nouri1@gmail.com',
    description='Interactive wall detection touch ',
    license='MIT',
    
   tests_require=['pytest'],
    entry_points={'console_scripts': [
            'baseline_calibrator = wall_touch.baseline_calibration_node:main',
            'touch_detector      = wall_touch.touch_detector_node:main',
            'uinput_injector     = wall_touch.uinput_node:main',
        ],
    },
)
