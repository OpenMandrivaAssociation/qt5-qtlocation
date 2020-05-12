%define api %(echo %{version} |cut -d. -f1)
%define major %api
%define beta rc2

%define qtlocation %mklibname qt%{api}location %{major}
%define qtlocationd %mklibname qt%{api}location -d
%define qtlocation_p_d %mklibname qt%{api}location-private -d

%define qtpositioning %mklibname qt%{api}positioning %{major}
%define qtpositioningd %mklibname qt%{api}positioning -d
%define qtpositioning_p_d %mklibname qt%{api}positioning-private -d

%define qtpositioningquick %mklibname qt%{api}positioningquick %{major}
%define qtpositioningquickd %mklibname qt%{api}positioningquick -d
%define qtpositioningquick_p_d %mklibname qt%{api}positioning-privatequick -d

%define _qt5_prefix %{_libdir}/qt%{api}

Name:		qt5-qtlocation
Version:	5.15.0
%if "%{beta}" != ""
Release:	0.%{beta}.1
%define qttarballdir qtlocation-everywhere-src-%{version}-%{beta}
Source0:	http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%{beta}/submodules/%{qttarballdir}.tar.xz
%else
Release:	1
%define qttarballdir qtlocation-everywhere-src-%{version}
Source0:	http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
%endif
Summary:	Qt Location
Group:		Development/KDE and Qt
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		http://www.qt.io
Patch0:		qtlocation-everywhere-src-5.6.0-G_VALUE_INIT.patch
Patch1:		qtlocation-clang10-c++20.patch
# Updated 3rd party component to fix QTBUG-82273
Source1:	https://raw.githubusercontent.com/mapbox/earcut.hpp/master/include/mapbox/earcut.hpp
BuildRequires:	qt5-qtbase-devel >= %{version}
BuildRequires:	pkgconfig(Qt5Core) = %{version}
BuildRequires:	pkgconfig(Qt5Gui) >= %{version}
BuildRequires:	pkgconfig(Qt5Qml) >= %{version}
BuildRequires:	pkgconfig(Qt5Svg) >= %{version}
BuildRequires:	pkgconfig(Qt5XmlPatterns) >= %{version}
BuildRequires:	pkgconfig(Qt5Multimedia) >= %{version}
BuildRequires:	pkgconfig(Qt5Quick) >= %{version}
BuildRequires:	qt5-qtqml-private-devel >= %{version}
BuildRequires:	qt5-qtquick-private-devel >= %{version}
BuildRequires:	qt5-qtqmlmodels-private-devel
BuildRequires:	pkgconfig(geoclue-2.0)
BuildRequires:	pkgconfig(gypsy)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(icu-uc)
BuildRequires:	pkgconfig(libssl)
BuildRequires:	pkgconfig(libcrypto)
BuildRequires:	boost-devel
# For the Provides: generator
BuildRequires:	cmake >= 3.11.0-1

%description
Qt is a GUI software toolkit which simplifies the task of writing and
maintaining GUI (Graphical User Interface) applications for the X
Window System. Qt is written in C++ and is fully object-oriented.

%files
%{_qt5_prefix}/qml/QtLocation
%{_qt5_plugindir}/geoservices
%{_libdir}/qt5/qml/Qt/labs/location

#------------------------------------------------------------------------------

%package -n	qt5-qtpositioning
Summary:	Qt%{api} Positioning Component Library
Group:		System/Libraries
Requires:	%{qtpositioning} = %{version}
Provides:	qt5positioning = %{version}
Provides:	qt5-positioning = %{version}

%description -n qt5-qtpositioning
Qt%{api} Component Library.

The Positioning module provides positioning
information via QML and C++ interfaces.

%files -n qt5-qtpositioning
%{_qt5_prefix}/qml/QtPositioning
%{_qt5_plugindir}/position

#------------------------------------------------------------------------------

%package -n %{qtpositioning}
Summary: Qt%{api} Component Library
Group: System/Libraries
Requires: qt5-qtpositioning = %{EVRD}

%description -n %{qtpositioning}
Qt%{api} Component Library.

The Positioning module provides positioning
information via QML and C++ interfaces.

%files -n %{qtpositioning}
%{_qt5_libdir}/libQt5Positioning.so.%{api}*

#------------------------------------------------------------------------------

%package -n %{qtpositioningd}
Summary: Devel files needed to build apps based on QtPositioning
Group: Development/KDE and Qt
Requires: %{qtpositioning} = %version

%description -n %{qtpositioningd}
Devel files needed to build apps based on Qt Positioning.

%files -n %{qtpositioningd}
%{_qt5_libdir}/libQt5Positioning.prl
%{_qt5_libdir}/libQt5Positioning.so
%{_qt5_libdir}/pkgconfig/Qt5Positioning.pc
%{_qt5_libdir}/cmake/Qt5Positioning
%{_qt5_exampledir}/positioning
%{_qt5_prefix}/mkspecs/modules/qt_lib_positioning.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_location_private.pri
%{_qt5_includedir}/QtPositioning
%exclude %{_qt5_includedir}/QtPositioning/%version

#------------------------------------------------------------------------------

%package -n %{qtpositioning_p_d}
Summary: Devel files needed to build apps based on QtPositioning
Group:    Development/KDE and Qt
Requires: %{qtpositioningd} = %version
Provides: qt5-positioning-private-devel = %version

%description -n %{qtpositioning_p_d}
Devel files needed to build apps based on QtPositioning.

%files -n %{qtpositioning_p_d}
%{_qt5_includedir}/QtPositioning/%version
%{_qt5_prefix}/mkspecs/modules/qt_lib_positioning_private.pri

#------------------------------------------------------------------------------

%package -n %{qtpositioningquick}
Summary: Qt%{api}Quick positioning Library
Group: System/Libraries

%description -n %{qtpositioningquick}
Qt%{api}Quick positioning Library.

The Positioning module provides positioning
information via QML and C++ interfaces.

%files -n %{qtpositioningquick}
%{_qt5_libdir}/libQt5PositioningQuick.so.%{api}*

#------------------------------------------------------------------------------

%package -n %{qtpositioningquickd}
Summary: Devel files needed to build apps based on QtPositioningQuick
Group: Development/KDE and Qt
Requires: %{qtpositioningquick} = %version

%description -n %{qtpositioningquickd}
Devel files needed to build apps based on Qt PositioningQuick.

%files -n %{qtpositioningquickd}
%{_qt5_includedir}/QtPositioningQuick
%{_qt5_libdir}/libQt5PositioningQuick.so
%{_libdir}/libQt5PositioningQuick.prl
%exclude %{_qt5_includedir}/QtPositioningQuick/%version
%{_qt5_prefix}/mkspecs/modules/qt_lib_positioningquick.pri
%{_libdir}/cmake/Qt5PositioningQuick
%{_libdir}/pkgconfig/Qt5PositioningQuick.pc

#------------------------------------------------------------------------------

%package -n %{qtpositioningquick_p_d}
Summary: Devel files needed to build apps based on QtPositioningQuick
Group:    Development/KDE and Qt
Requires: %{qtpositioningquickd} = %version
Provides: qt5-positioningquick-private-devel = %version

%description -n %{qtpositioningquick_p_d}
Devel files needed to build apps based on QtPositioningQuick.

%files -n %{qtpositioningquick_p_d}
%{_qt5_includedir}/QtPositioningQuick/%version
%{_qt5_prefix}/mkspecs/modules/qt_lib_positioningquick_private.pri

#------------------------------------------------------------------------------

%package -n %{qtlocation}
Summary: Qt%{api} Component Library
Group: System/Libraries

%description -n %{qtlocation}
Qt%{api} Component Library.

The Location module provides location information via QML and C++ interfaces.

%files -n %{qtlocation}
%{_qt5_libdir}/libQt5Location.so.%{api}*

#------------------------------------------------------------------------------

%package -n %{qtlocationd}
Summary: Devel files needed to build apps based on QtLocation
Group: Development/KDE and Qt
Requires: %{qtlocation} = %version

%description -n %{qtlocationd}
Devel files needed to build apps based on Qt Location.

%files -n %{qtlocationd}
%{_qt5_libdir}/cmake/Qt5Location
%{_qt5_libdir}/libQt5Location.prl
%{_qt5_libdir}/libQt5Location.so
%{_qt5_libdir}/pkgconfig/Qt5Location.pc
%{_qt5_includedir}/QtLocation
%{_qt5_exampledir}/location
%exclude %{_qt5_includedir}/QtLocation/%version
%{_qt5_prefix}/mkspecs/modules/qt_lib_location.pri

#------------------------------------------------------------------------------

%prep
%autosetup -n %qttarballdir -p1

# Get rid of outdated bundled boost, let's use system boost
rm -rf src/3rdparty/mapbox-gl-native/deps/boost
sed -i -e '/boost/d' src/3rdparty/mapbox-gl-native/mapbox-gl-native.pro

# And update outdated bundled earcut
cp -f %{S:1} src/3rdparty/earcut/
cp -f %{S:1} src/3rdparty/mapbox-gl-native/deps/earcut/0.12.4/include/mapbox/
# And adapt to new upstream sources...
sed -i -e 's,qt_mapbox,mapbox,g' src/location/declarativemaps/qdeclarativepolygonmapitem.cpp

%build
%qmake_qt5
%make_build

#------------------------------------------------------------------------------
%install
%make_install INSTALL_ROOT=%{buildroot}

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %{buildroot}%{_qt5_libdir}
for prl_file in libQt5*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd

# .la and .a files, die, die, die.
rm -f %{buildroot}%{_qt5_libdir}/lib*.la
