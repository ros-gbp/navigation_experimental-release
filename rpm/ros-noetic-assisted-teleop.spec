%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-assisted-teleop
Version:        0.3.4
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS assisted_teleop package

License:        BSD
URL:            http://wiki.ros.org/assisted_teleop
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-noetic-actionlib
Requires:       ros-noetic-angles
Requires:       ros-noetic-base-local-planner
Requires:       ros-noetic-costmap-2d
Requires:       ros-noetic-filters
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-message-filters
Requires:       ros-noetic-move-base-msgs
Requires:       ros-noetic-pluginlib
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-roslib
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-tf2-ros
BuildRequires:  eigen3-devel
BuildRequires:  ros-noetic-actionlib
BuildRequires:  ros-noetic-angles
BuildRequires:  ros-noetic-base-local-planner
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-costmap-2d
BuildRequires:  ros-noetic-filters
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-message-filters
BuildRequires:  ros-noetic-move-base-msgs
BuildRequires:  ros-noetic-pluginlib
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-roslib
BuildRequires:  ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-tf2-ros
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The assisted_teleop node subscribes to a desired trajectory topic
(geometry_msgs/Twist) and uses TrajectoryPlannerROS to find a valid trajectory
close to the desired trajectory before republishing. Useful for filtering teleop
commands while avoiding obstacles. This package also contains
LaserScanMaxRangeFilter, which is a LaserScan filter plugin that takes max range
values in a scan and turns them into valid values that are slightly less than
max range.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Fri Jun 19 2020 Martin Günther <martin.guenther@dfki.de> - 0.3.4-1
- Autogenerated by Bloom
