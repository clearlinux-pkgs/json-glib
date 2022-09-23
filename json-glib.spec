#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : json-glib
Version  : 1.6.6
Release  : 34
URL      : https://download.gnome.org/sources/json-glib/1.6/json-glib-1.6.6.tar.xz
Source0  : https://download.gnome.org/sources/json-glib/1.6/json-glib-1.6.6.tar.xz
Summary  : GObject-Introspection based documentation generator
Group    : Development/Tools
License  : Apache-2.0 CC-BY-SA-3.0 CC0-1.0 GPL-3.0 LGPL-2.1 MIT OFL-1.1
Requires: json-glib-bin = %{version}-%{release}
Requires: json-glib-data = %{version}-%{release}
Requires: json-glib-lib = %{version}-%{release}
Requires: json-glib-license = %{version}-%{release}
Requires: json-glib-locales = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : glib-dev
BuildRequires : gobject-introspection-dev

%description
JSON-GLib
===============================================================================

%package bin
Summary: bin components for the json-glib package.
Group: Binaries
Requires: json-glib-data = %{version}-%{release}
Requires: json-glib-license = %{version}-%{release}

%description bin
bin components for the json-glib package.


%package data
Summary: data components for the json-glib package.
Group: Data

%description data
data components for the json-glib package.


%package dev
Summary: dev components for the json-glib package.
Group: Development
Requires: json-glib-lib = %{version}-%{release}
Requires: json-glib-bin = %{version}-%{release}
Requires: json-glib-data = %{version}-%{release}
Provides: json-glib-devel = %{version}-%{release}
Requires: json-glib = %{version}-%{release}

%description dev
dev components for the json-glib package.


%package lib
Summary: lib components for the json-glib package.
Group: Libraries
Requires: json-glib-data = %{version}-%{release}
Requires: json-glib-license = %{version}-%{release}

%description lib
lib components for the json-glib package.


%package license
Summary: license components for the json-glib package.
Group: Default

%description license
license components for the json-glib package.


%package locales
Summary: locales components for the json-glib package.
Group: Default

%description locales
locales components for the json-glib package.


%package tests
Summary: tests components for the json-glib package.
Group: Default
Requires: json-glib = %{version}-%{release}

%description tests
tests components for the json-glib package.


%prep
%setup -q -n json-glib-1.6.6
cd %{_builddir}/json-glib-1.6.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1629758884
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/json-glib
cp %{_builddir}/json-glib-1.6.6/COPYING %{buildroot}/usr/share/package-licenses/json-glib/e60c2e780886f95df9c9ee36992b8edabec00bcc
cp %{_builddir}/json-glib-1.6.6/subprojects/gi-docgen/LICENSES/Apache-2.0.txt %{buildroot}/usr/share/package-licenses/json-glib/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/json-glib-1.6.6/subprojects/gi-docgen/LICENSES/CC-BY-SA-3.0.txt %{buildroot}/usr/share/package-licenses/json-glib/fb41626a3005c2b6e14b8b3f5d9d0b19b5faaa51
cp %{_builddir}/json-glib-1.6.6/subprojects/gi-docgen/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/json-glib/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/json-glib-1.6.6/subprojects/gi-docgen/LICENSES/GPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/json-glib/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/json-glib-1.6.6/subprojects/gi-docgen/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/json-glib/220906dfcc3d3b7f4e18cf8a22454c628ca0ea2e
cp %{_builddir}/json-glib-1.6.6/subprojects/gi-docgen/LICENSES/OFL-1.1.txt %{buildroot}/usr/share/package-licenses/json-glib/8b8a351a8476e37a2c4d398eb1e6c8403f487ea4
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang json-glib-1.0

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/json-glib-format
/usr/bin/json-glib-validate

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Json-1.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/json-glib-1.0/json-glib/json-builder.h
/usr/include/json-glib-1.0/json-glib/json-enum-types.h
/usr/include/json-glib-1.0/json-glib/json-generator.h
/usr/include/json-glib-1.0/json-glib/json-glib.h
/usr/include/json-glib-1.0/json-glib/json-gobject.h
/usr/include/json-glib-1.0/json-glib/json-gvariant.h
/usr/include/json-glib-1.0/json-glib/json-parser.h
/usr/include/json-glib-1.0/json-glib/json-path.h
/usr/include/json-glib-1.0/json-glib/json-reader.h
/usr/include/json-glib-1.0/json-glib/json-types.h
/usr/include/json-glib-1.0/json-glib/json-utils.h
/usr/include/json-glib-1.0/json-glib/json-version-macros.h
/usr/include/json-glib-1.0/json-glib/json-version.h
/usr/lib64/libjson-glib-1.0.so
/usr/lib64/pkgconfig/json-glib-1.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libjson-glib-1.0.so.0
/usr/lib64/libjson-glib-1.0.so.0.600.6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/json-glib/220906dfcc3d3b7f4e18cf8a22454c628ca0ea2e
/usr/share/package-licenses/json-glib/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/json-glib/31a3d460bb3c7d98845187c716a30db81c44b615
/usr/share/package-licenses/json-glib/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/json-glib/8b8a351a8476e37a2c4d398eb1e6c8403f487ea4
/usr/share/package-licenses/json-glib/e60c2e780886f95df9c9ee36992b8edabec00bcc
/usr/share/package-licenses/json-glib/fb41626a3005c2b6e14b8b3f5d9d0b19b5faaa51

%files tests
%defattr(-,root,root,-)
/usr/libexec/installed-tests/json-glib-1.0/array
/usr/libexec/installed-tests/json-glib-1.0/boxed
/usr/libexec/installed-tests/json-glib-1.0/builder
/usr/libexec/installed-tests/json-glib-1.0/generator
/usr/libexec/installed-tests/json-glib-1.0/gvariant
/usr/libexec/installed-tests/json-glib-1.0/invalid
/usr/libexec/installed-tests/json-glib-1.0/invalid.json
/usr/libexec/installed-tests/json-glib-1.0/node
/usr/libexec/installed-tests/json-glib-1.0/object
/usr/libexec/installed-tests/json-glib-1.0/parser
/usr/libexec/installed-tests/json-glib-1.0/path
/usr/libexec/installed-tests/json-glib-1.0/reader
/usr/libexec/installed-tests/json-glib-1.0/serialize-complex
/usr/libexec/installed-tests/json-glib-1.0/serialize-full
/usr/libexec/installed-tests/json-glib-1.0/serialize-simple
/usr/libexec/installed-tests/json-glib-1.0/skip-bom.json
/usr/libexec/installed-tests/json-glib-1.0/stream-load.json
/usr/share/installed-tests/json-glib-1.0/array.test
/usr/share/installed-tests/json-glib-1.0/boxed.test
/usr/share/installed-tests/json-glib-1.0/builder.test
/usr/share/installed-tests/json-glib-1.0/generator.test
/usr/share/installed-tests/json-glib-1.0/gvariant.test
/usr/share/installed-tests/json-glib-1.0/invalid.test
/usr/share/installed-tests/json-glib-1.0/node.test
/usr/share/installed-tests/json-glib-1.0/object.test
/usr/share/installed-tests/json-glib-1.0/parser.test
/usr/share/installed-tests/json-glib-1.0/path.test
/usr/share/installed-tests/json-glib-1.0/reader.test
/usr/share/installed-tests/json-glib-1.0/serialize-complex.test
/usr/share/installed-tests/json-glib-1.0/serialize-full.test
/usr/share/installed-tests/json-glib-1.0/serialize-simple.test

%files locales -f json-glib-1.0.lang
%defattr(-,root,root,-)

