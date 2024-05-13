cmake_minimum_required(VERSION 3.15...3.27)

set(PROJECT_NAME st_ext)
project(${PROJECT_NAME} CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Python 3.8 COMPONENTS Interpreter Development.Module REQUIRED)

if (NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
  set(CMAKE_BUILD_TYPE Release CACHE STRING "Choose the type of build." FORCE)
  set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release" "MinSizeRel" "RelWithDebInfo")
endif()

add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/ext/nanobind)

nanobind_add_module(${PROJECT_NAME} st_ext.cpp)

find_package(audiofile REQUIRED)
find_package(glog REQUIRED)
find_package(SoundTouch REQUIRED)
target_link_libraries(${PROJECT_NAME} PRIVATE
  audiofile::audiofile
  glog::glog
  soundtouch::soundtouch
)
