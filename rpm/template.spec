Name:           ros-melodic-sbpl-lattice-planner
Version:        0.3.3
Release:        1%{?dist}
Summary:        ROS sbpl_lattice_planner package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/sbpl_lattice_planner
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-costmap-2d
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-nav-core
Requires:       ros-melodic-nav-msgs
Requires:       ros-melodic-pluginlib
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-sbpl
Requires:       ros-melodic-tf2
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-costmap-2d
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-nav-core
BuildRequires:  ros-melodic-nav-msgs
BuildRequires:  ros-melodic-pluginlib
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-sbpl
BuildRequires:  ros-melodic-tf2

%description
The sbpl_lattice_planner is a global planner plugin for move_base and wraps the
SBPL search-based planning library.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Tue Oct 15 2019 Martin Günther <martin.guenther@dfki.de> - 0.3.3-1
- Autogenerated by Bloom

* Wed Jan 16 2019 Martin Günther <martin.guenther@dfki.de> - 0.3.2-0
- Autogenerated by Bloom

* Wed Sep 05 2018 Martin Günther <martin.guenther@dfki.de> - 0.3.1-0
- Autogenerated by Bloom

* Tue Sep 04 2018 Martin Günther <martin.guenther@dfki.de> - 0.3.0-0
- Autogenerated by Bloom

* Mon Sep 03 2018 Martin Günther <martin.guenther@dfki.de> - 0.2.0-0
- Autogenerated by Bloom

