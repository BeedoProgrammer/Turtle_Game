from setuptools import find_packages, setup

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='beedo',
    maintainer_email='beedo@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "Pub_node = my_robot_controller.Publisher_node:main",
            "Sub_node = my_robot_controller.Subscriber_node:main",
            "Main_Turtle = my_robot_controller.turtle_catch:main"
        ],
    },
)
