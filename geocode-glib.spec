#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : geocode-glib
Version  : 3.23.90
Release  : 2
URL      : http://ftp.gnome.org/pub/GNOME/sources/geocode-glib/3.23/geocode-glib-3.23.90.tar.xz
Source0  : http://ftp.gnome.org/pub/GNOME/sources/geocode-glib/3.23/geocode-glib-3.23.90.tar.xz
Summary  : Helper library for geocoding services
Group    : Development/Tools
License  : LGPL-2.0
Requires: geocode-glib-lib
Requires: geocode-glib-doc
Requires: geocode-glib-data
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
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
Requires: geocode-glib-lib
Requires: geocode-glib-data
Provides: geocode-glib-devel

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
Requires: geocode-glib-data

%description lib
lib components for the geocode-glib package.


%prep
%setup -q -n geocode-glib-3.23.90

%build
export LANG=C
export SOURCE_DATE_EPOCH=1491485899
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1491485899
rm -rf %{buildroot}
%make_install

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
%defattr(-,root,root,-)
/usr/share/gtk-doc/html/geocode-glib-1.0/GeocodeBackend.html
/usr/share/gtk-doc/html/geocode-glib-1.0/GeocodeBoundingBox.html
/usr/share/gtk-doc/html/geocode-glib-1.0/GeocodeForward.html
/usr/share/gtk-doc/html/geocode-glib-1.0/GeocodeLocation.html
/usr/share/gtk-doc/html/geocode-glib-1.0/GeocodeNominatim.html
/usr/share/gtk-doc/html/geocode-glib-1.0/GeocodePlace.html
/usr/share/gtk-doc/html/geocode-glib-1.0/GeocodeReverse.html
/usr/share/gtk-doc/html/geocode-glib-1.0/annotation-glossary.html
/usr/share/gtk-doc/html/geocode-glib-1.0/api-index-full.html
/usr/share/gtk-doc/html/geocode-glib-1.0/ch01.html
/usr/share/gtk-doc/html/geocode-glib-1.0/geocode-glib-1.0.devhelp2
/usr/share/gtk-doc/html/geocode-glib-1.0/geocode-glib-geocode-error.html
/usr/share/gtk-doc/html/geocode-glib-1.0/geocode-glib-geocode-mock-backend.html
/usr/share/gtk-doc/html/geocode-glib-1.0/home.png
/usr/share/gtk-doc/html/geocode-glib-1.0/index.html
/usr/share/gtk-doc/html/geocode-glib-1.0/left-insensitive.png
/usr/share/gtk-doc/html/geocode-glib-1.0/left.png
/usr/share/gtk-doc/html/geocode-glib-1.0/right-insensitive.png
/usr/share/gtk-doc/html/geocode-glib-1.0/right.png
/usr/share/gtk-doc/html/geocode-glib-1.0/style.css
/usr/share/gtk-doc/html/geocode-glib-1.0/up-insensitive.png
/usr/share/gtk-doc/html/geocode-glib-1.0/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgeocode-glib.so.0
/usr/lib64/libgeocode-glib.so.0.0.0
