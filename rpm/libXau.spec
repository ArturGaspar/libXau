Name:       libXau
Version:    1.0.11
Release:    1%{?dist}
Summary:    Functions for handling Xauthority files and entries
License:    MIT
URL:        https://gitlab.freedesktop.org/xorg/lib/libxau
Source0:    https://gitlab.freedesktop.org/xorg/lib/libxau/-/archive/%{name}-%{version}/libxau-%{name}-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto)

%description
%{summary}.

%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package doc
Summary:    Documentation for %{name}
Requires:   %{name} = %{version}-%{release}

%description doc
%{summary}.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%license COPYING
%{_includedir}/X11/Xauth.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/xau.pc

%files doc
%license COPYING
%{_mandir}/man3/Xau*.3*
