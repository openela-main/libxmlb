%global glib2_version 2.45.8

Summary:   Library for querying compressed XML metadata
Name:      libxmlb
Version:   0.1.15
Release:   1%{?dist}
License:   LGPLv2+
URL:       https://github.com/hughsie/libxmlb
Source0:   http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz

BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: gtk-doc
BuildRequires: libstemmer-devel
BuildRequires: meson
BuildRequires: gobject-introspection-devel
BuildRequires: python3-setuptools

# needed for the self tests
BuildRequires: shared-mime-info

Requires: glib2%{?_isa} >= %{glib2_version}
Requires: shared-mime-info

%description
XML is slow to parse and strings inside the document cannot be memory mapped as
they do not have a trailing NUL char. The libxmlb library takes XML source, and
converts it to a structured binary representation with a deduplicated string
table -- where the strings have the NULs included.

This allows an application to mmap the binary XML file, do an XPath query and
return some strings without actually parsing the entire document. This is all
done using (almost) zero allocations and no actual copying of the binary data.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%package tests
Summary: Files for installed tests

%description tests
Executable and data files for installed tests.

%prep
%setup -q

%build

%meson \
    -Dgtkdoc=true \
    -Dtests=true

%meson_build

%check
%meson_test

%install
%meson_install

%files
%doc README.md
%license LICENSE
%{_libexecdir}/xb-tool
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/*.typelib
%{_libdir}/libxmlb.so.1*

%files devel
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/libxmlb
%{_includedir}/libxmlb-1
%{_libdir}/libxmlb.so
%{_libdir}/pkgconfig/xmlb.pc

%files tests
%{_libexecdir}/installed-tests/libxmlb/xb-self-test
%{_datadir}/installed-tests/libxmlb/libxmlb.test
%{_datadir}/installed-tests/libxmlb/test.xml.gz.gz.gz
%dir %{_datadir}/installed-tests/libxmlb

%changelog
* Wed Mar 11 2020 Richard Hughes <richard@hughsie.com> 0.1.15-1
- Initial release for RHEL
