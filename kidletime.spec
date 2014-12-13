%define major 5
%define libname %mklibname KF5IdleTime %{major}
%define devname %mklibname KF5IdleTime -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kidletime
Version: 5.5.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/frameworks/%{version}/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 idle time library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5

%description
KIdleTime provides notifications of device's idle time.

KIdleTime is a platform-independent framework that allows detecting and
notifying of idle time events of the device. It can, for example be
used to start an action (or a job) after a certain amount of user
inactivity.

%package -n %{libname}
Summary: The KDE Frameworks 5 idle time library
Group: System/Libraries

%description -n %{libname}
KIdleTime provides notifications of device's idle time.

KIdleTime is a platform-independent framework that allows detecting and
notifying of idle time events of the device. It can, for example be
used to start an action (or a job) after a certain amount of user
inactivity.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
KIdleTime provides notifications of device's idle time.

KIdleTime is a platform-independent framework that allows detecting and
notifying of idle time events of the device. It can, for example be
used to start an action (or a job) after a certain amount of user
inactivity.

%prep
%setup -q
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5IdleTime
%{_libdir}/qt5/mkspecs/modules/*
