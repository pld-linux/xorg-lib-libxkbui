Summary:	xkbui library
Summary(pl.UTF-8):	Biblioteka xkbui
Name:		xorg-lib-libxkbui
Version:	1.0.2
Release:	5
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libxkbui-%{version}.tar.bz2
# Source0-md5:	1143e456f7429e18e88f2eadb2f2b6b1
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xkbui library.

%description -l pl.UTF-8
Biblioteka xkbui.

%package devel
Summary:	Header files for libxkbui library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libxkbui
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXt-devel
Requires:	xorg-lib-libxkbfile-devel

%description devel
xkbui library.

This package contains the header files needed to develop programs that
use libxkbui.

%description devel -l pl.UTF-8
Biblioteka xkbui.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libxkbui.

%package static
Summary:	Static libxkbui library
Summary(pl.UTF-8):	Biblioteka statyczna libxkbui
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
xkbui library.

This package contains the static libxkbui library.

%description static -l pl.UTF-8
Biblioteka xkbui.

Pakiet zawiera statyczną bibliotekę libxkbui.

%prep
%setup -q -n libxkbui-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libxkbui.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxkbui.so
%{_libdir}/libxkbui.la
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xkbui.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxkbui.a
