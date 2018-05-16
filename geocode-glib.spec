#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : geocode-glib
Version  : 3.25.4.1
Release  : 8
URL      : https://download.gnome.org/sources/geocode-glib/3.25/geocode-glib-3.25.4.1.tar.xz
Source0  : https://download.gnome.org/sources/geocode-glib/3.25/geocode-glib-3.25.4.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.0
Requires: geocode-glib-lib
Requires: geocode-glib-bin
Requires: geocode-glib-data
BuildRequires : glibc-bin
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : meson
BuildRequires : ninja
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : python3

%description
geocode-glib is a convenience library for the geocoding (finding longitude,
and latitude from an address) and reverse geocoding (finding an address from
coordinates). It uses Nominatim service to achieve that. It also caches
(reverse-)geocoding requests for faster results and to avoid unnecessary server
load.

%package bin
Summary: bin components for the geocode-glib package.
Group: Binaries
Requires: geocode-glib-data

%description bin
bin components for the geocode-glib package.


%package data
Summary: data components for the geocode-glib package.
Group: Data

%description data
data components for the geocode-glib package.


%package dev
Summary: dev components for the geocode-glib package.
Group: Development
Requires: geocode-glib-lib
Requires: geocode-glib-bin
Requires: geocode-glib-data
Provides: geocode-glib-devel

%description dev
dev components for the geocode-glib package.


%package lib
Summary: lib components for the geocode-glib package.
Group: Libraries
Requires: geocode-glib-data

%description lib
lib components for the geocode-glib package.


%prep
%setup -q -n geocode-glib-3.25.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522958346
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1522958346
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/libexec/installed-tests/geocode-glib/geo-uri
/usr/libexec/installed-tests/geocode-glib/geocode-glib
/usr/libexec/installed-tests/geocode-glib/locale_format.json
/usr/libexec/installed-tests/geocode-glib/locale_name.json
/usr/libexec/installed-tests/geocode-glib/mock-backend
/usr/libexec/installed-tests/geocode-glib/nominatim-area.json
/usr/libexec/installed-tests/geocode-glib/nominatim-no-results.json
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

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgeocode-glib.so.0
/usr/lib64/libgeocode-glib.so.0.0.0
