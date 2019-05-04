#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : geocode-glib
Version  : 3.26.1
Release  : 11
URL      : https://download.gnome.org/sources/geocode-glib/3.26/geocode-glib-3.26.1.tar.xz
Source0  : https://download.gnome.org/sources/geocode-glib/3.26/geocode-glib-3.26.1.tar.xz
Summary  : Helper library for geocoding services
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.0
Requires: geocode-glib-data = %{version}-%{release}
Requires: geocode-glib-lib = %{version}-%{release}
Requires: geocode-glib-libexec = %{version}-%{release}
Requires: geocode-glib-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : gtk-doc
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libsoup-2.4)

%description
geocode-glib is a convenience library for the geocoding (finding longitude,
and latitude from an address) and reverse geocoding (finding an address from
coordinates). It uses Nominatim service to achieve that. It also caches
(reverse-)geocoding requests for faster results and to avoid unnecessary server
load.

%package data
Summary: data components for the geocode-glib package.
Group: Data

%description data
data components for the geocode-glib package.


%package dev
Summary: dev components for the geocode-glib package.
Group: Development
Requires: geocode-glib-lib = %{version}-%{release}
Requires: geocode-glib-data = %{version}-%{release}
Provides: geocode-glib-devel = %{version}-%{release}
Requires: geocode-glib = %{version}-%{release}

%description dev
dev components for the geocode-glib package.


%package doc
Summary: doc components for the geocode-glib package.
Group: Documentation

%description doc
doc components for the geocode-glib package.


%package lib
Summary: lib components for the geocode-glib package.
Group: Libraries
Requires: geocode-glib-data = %{version}-%{release}
Requires: geocode-glib-libexec = %{version}-%{release}
Requires: geocode-glib-license = %{version}-%{release}

%description lib
lib components for the geocode-glib package.


%package libexec
Summary: libexec components for the geocode-glib package.
Group: Default
Requires: geocode-glib-license = %{version}-%{release}

%description libexec
libexec components for the geocode-glib package.


%package license
Summary: license components for the geocode-glib package.
Group: Default

%description license
license components for the geocode-glib package.


%prep
%setup -q -n geocode-glib-3.26.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556999177
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/geocode-glib
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/geocode-glib/COPYING.LIB
cp icons/maki/LICENSE.txt %{buildroot}/usr/share/package-licenses/geocode-glib/icons_maki_LICENSE.txt
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GeocodeGlib-1.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/icons/gnome/scalable/places/poi-airport.svg
/usr/share/icons/gnome/scalable/places/poi-bar.svg
/usr/share/icons/gnome/scalable/places/poi-building.svg
/usr/share/icons/gnome/scalable/places/poi-bus-stop.svg
/usr/share/icons/gnome/scalable/places/poi-car.svg
/usr/share/icons/gnome/scalable/places/poi-light-rail-station.svg
/usr/share/icons/gnome/scalable/places/poi-marker.svg
/usr/share/icons/gnome/scalable/places/poi-place-of-worship.svg
/usr/share/icons/gnome/scalable/places/poi-railway-station.svg
/usr/share/icons/gnome/scalable/places/poi-restaurant.svg
/usr/share/icons/gnome/scalable/places/poi-school.svg
/usr/share/icons/gnome/scalable/places/poi-town.svg

%files dev
%defattr(-,root,root,-)
/usr/include/geocode-glib-1.0/geocode-glib/geocode-backend.h
/usr/include/geocode-glib-1.0/geocode-glib/geocode-bounding-box.h
/usr/include/geocode-glib-1.0/geocode-glib/geocode-enum-types.h
/usr/include/geocode-glib-1.0/geocode-glib/geocode-error.h
/usr/include/geocode-glib-1.0/geocode-glib/geocode-forward.h
/usr/include/geocode-glib-1.0/geocode-glib/geocode-glib.h
/usr/include/geocode-glib-1.0/geocode-glib/geocode-location.h
/usr/include/geocode-glib-1.0/geocode-glib/geocode-mock-backend.h
/usr/include/geocode-glib-1.0/geocode-glib/geocode-nominatim.h
/usr/include/geocode-glib-1.0/geocode-glib/geocode-place.h
/usr/include/geocode-glib-1.0/geocode-glib/geocode-reverse.h
/usr/lib64/libgeocode-glib.so
/usr/lib64/pkgconfig/geocode-glib-1.0.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/geocode-glib/GeocodeBackend.html
/usr/share/gtk-doc/html/geocode-glib/GeocodeBoundingBox.html
/usr/share/gtk-doc/html/geocode-glib/GeocodeForward.html
/usr/share/gtk-doc/html/geocode-glib/GeocodeLocation.html
/usr/share/gtk-doc/html/geocode-glib/GeocodeNominatim.html
/usr/share/gtk-doc/html/geocode-glib/GeocodePlace.html
/usr/share/gtk-doc/html/geocode-glib/GeocodeReverse.html
/usr/share/gtk-doc/html/geocode-glib/annotation-glossary.html
/usr/share/gtk-doc/html/geocode-glib/api-index-full.html
/usr/share/gtk-doc/html/geocode-glib/ch01.html
/usr/share/gtk-doc/html/geocode-glib/geocode-glib-geocode-error.html
/usr/share/gtk-doc/html/geocode-glib/geocode-glib-geocode-mock-backend.html
/usr/share/gtk-doc/html/geocode-glib/geocode-glib.devhelp2
/usr/share/gtk-doc/html/geocode-glib/home.png
/usr/share/gtk-doc/html/geocode-glib/index.html
/usr/share/gtk-doc/html/geocode-glib/left-insensitive.png
/usr/share/gtk-doc/html/geocode-glib/left.png
/usr/share/gtk-doc/html/geocode-glib/right-insensitive.png
/usr/share/gtk-doc/html/geocode-glib/right.png
/usr/share/gtk-doc/html/geocode-glib/style.css
/usr/share/gtk-doc/html/geocode-glib/up-insensitive.png
/usr/share/gtk-doc/html/geocode-glib/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgeocode-glib.so.0
/usr/lib64/libgeocode-glib.so.0.0.0

%files libexec
%defattr(-,root,root,-)
/usr/libexec/installed-tests/geocode-glib/geo-uri
/usr/libexec/installed-tests/geocode-glib/geocode-glib
/usr/libexec/installed-tests/geocode-glib/locale_format.json
/usr/libexec/installed-tests/geocode-glib/locale_name.json
/usr/libexec/installed-tests/geocode-glib/mock-backend
/usr/libexec/installed-tests/geocode-glib/nominatim-area.json
/usr/libexec/installed-tests/geocode-glib/nominatim-data-type-change.json
/usr/libexec/installed-tests/geocode-glib/nominatim-no-results.json
/usr/libexec/installed-tests/geocode-glib/nominatim-place_rank.json
/usr/libexec/installed-tests/geocode-glib/nominatim-rio.json
/usr/libexec/installed-tests/geocode-glib/osm_type0.json
/usr/libexec/installed-tests/geocode-glib/osm_type1.json
/usr/libexec/installed-tests/geocode-glib/osm_type2.json
/usr/libexec/installed-tests/geocode-glib/pub.json
/usr/libexec/installed-tests/geocode-glib/rev.json
/usr/libexec/installed-tests/geocode-glib/rev_fail.json
/usr/libexec/installed-tests/geocode-glib/search.json
/usr/libexec/installed-tests/geocode-glib/search_lat_long.json
/usr/libexec/installed-tests/geocode-glib/xep.json

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/geocode-glib/COPYING.LIB
/usr/share/package-licenses/geocode-glib/icons_maki_LICENSE.txt
