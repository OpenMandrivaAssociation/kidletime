%define major 5
%define libname %mklibname KF5IdleTime %{major}
%define devname %mklibname KF5IdleTime -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kidletime
Version:	5.67.0
Release:	2
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 idle time library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(xscrnsaver)
BuildRequires: pkgconfig(xcb-sync)
# For QCH docs
BuildRequires: doxygen
BuildRequires: qt5-assistant

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

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_datadir}/qlogging-categories5/kidletime.categories
%dir %{_libdir}/qt5/plugins/kf5/org.kde.kidletime.platforms
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}
%{_libdir}/qt5/plugins/kf5/org.kde.kidletime.platforms/KF5IdleTimeXcbPlugin0.so
%{_libdir}/qt5/plugins/kf5/org.kde.kidletime.platforms/KF5IdleTimeXcbPlugin1.so

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5IdleTime
%{_libdir}/qt5/mkspecs/modules/*

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
