from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'hw4_3'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nathann',
    maintainer_email='nathann@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'py_hw4_3_spawner = hw4_3.turtle_spawner:main',
            'py_hw4_3_controller = hw4_3.turtle_controller:main',
            'py_hw4_3_service = hw4_3.turtle_service:main'
        ],
    },
)
