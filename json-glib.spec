#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : json-glib
Version  : 1.4.4
Release  : 27
URL      : https://download.gnome.org/sources/json-glib/1.4/json-glib-1.4.4.tar.xz
Source0  : https://download.gnome.org/sources/json-glib/1.4/json-glib-1.4.4.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: json-glib-bin = %{version}-%{release}
Requires: json-glib-data = %{version}-%{release}
Requires: json-glib-lib = %{version}-%{release}
Requires: json-glib-libexec = %{version}-%{release}
Requires: json-glib-license = %{version}-%{release}
Requires: json-glib-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glib-dev
BuildRequires : glib-dev32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
Patch1: 0001-change-mesontest-to-two-words.patch

%description
JSON-GLib
===============================================================================

%package bin
Summary: bin components for the json-glib package.
Group: Binaries
Requires: json-glib-data = %{version}-%{release}
Requires: json-glib-libexec = %{version}-%{release}
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


%package dev32
Summary: dev32 components for the json-glib package.
Group: Default
Requires: json-glib-lib32 = %{version}-%{release}
Requires: json-glib-bin = %{version}-%{release}
Requires: json-glib-data = %{version}-%{release}
Requires: json-glib-dev = %{version}-%{release}

%description dev32
dev32 components for the json-glib package.


%package lib
Summary: lib components for the json-glib package.
Group: Libraries
Requires: json-glib-data = %{version}-%{release}
Requires: json-glib-libexec = %{version}-%{release}
Requires: json-glib-license = %{version}-%{release}

%description lib
lib components for the json-glib package.


%package lib32
Summary: lib32 components for the json-glib package.
Group: Default
Requires: json-glib-data = %{version}-%{release}
Requires: json-glib-license = %{version}-%{release}

%description lib32
lib32 components for the json-glib package.


%package libexec
Summary: libexec components for the json-glib package.
Group: Default
Requires: json-glib-license = %{version}-%{release}

%description libexec
libexec components for the json-glib package.


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


%prep
%setup -q -n json-glib-1.4.4
cd %{_builddir}/json-glib-1.4.4
%patch1 -p1
pushd ..
cp -a json-glib-1.4.4 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586898830
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%install
export SOURCE_DATE_EPOCH=1586898830
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/json-glib
cp %{_builddir}/json-glib-1.4.4/COPYING %{buildroot}/usr/share/package-licenses/json-glib/e60c2e780886f95df9c9ee36992b8edabec00bcc
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
%find_lang json-glib-1.0

%files
%defattr(-,root,root,-)
/usr/lib32/girepository-1.0/Json-1.0.typelib

%files bin
%defattr(-,root,root,-)
/usr/bin/json-glib-format
/usr/bin/json-glib-validate

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Json-1.0.typelib
/usr/share/gir-1.0/*.gir
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

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libjson-glib-1.0.so
/usr/lib32/pkgconfig/32json-glib-1.0.pc
/usr/lib32/pkgconfig/json-glib-1.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libjson-glib-1.0.so.0
/usr/lib64/libjson-glib-1.0.so.0.400.4

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libjson-glib-1.0.so.0
/usr/lib32/libjson-glib-1.0.so.0.400.4

%files libexec
%defattr(-,root,root,-)
/usr/libexec/installed-tests/json-glib-1.0/array
/usr/libexec/installed-tests/json-glib-1.0/boxed
/usr/libexec/installed-tests/json-glib-1.0/builder
/usr/libexec/installed-tests/json-glib-1.0/generator
/usr/libexec/installed-tests/json-glib-1.0/gvariant
/usr/libexec/installed-tests/json-glib-1.0/invalid
/usr/libexec/installed-tests/json-glib-1.0/node
/usr/libexec/installed-tests/json-glib-1.0/object
/usr/libexec/installed-tests/json-glib-1.0/parser
/usr/libexec/installed-tests/json-glib-1.0/path
/usr/libexec/installed-tests/json-glib-1.0/reader
/usr/libexec/installed-tests/json-glib-1.0/serialize-complex
/usr/libexec/installed-tests/json-glib-1.0/serialize-full
/usr/libexec/installed-tests/json-glib-1.0/serialize-simple
/usr/libexec/installed-tests/json-glib-1.0/stream-load.json

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/json-glib/e60c2e780886f95df9c9ee36992b8edabec00bcc

%files locales -f json-glib-1.0.lang
%defattr(-,root,root,-)

