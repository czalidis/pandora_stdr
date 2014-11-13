cmake_minimum_required(VERSION 2.8.3)
project(pandora_stdr)

find_package(catkin REQUIRED)

catkin_package()

# Install launch files
install(DIRECTORY launch rviz resources
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
