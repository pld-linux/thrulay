#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	thrulay - measuring capacity of a network
Summary(pl.UTF-8):	thrulay - określanie przepustowości sieci
Name:		thrulay
Version:	0.9
Release:	1
License:	BSD-like (see included LICENSE)
Group:		Networking
Source0:	http://downloads.sourceforge.net/thrulay/%{name}-%{version}.tar.bz2
# Source0-md5:	3c01c221aae8ad8ab850b2408de841a0
Patch0:		%{name}-link.patch
Patch1:		%{name}-am.patch
URL:		https://sourceforge.net/projects/thrulay/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The program thrulay is used to measure the capacity of a network by
sending a bulk TCP stream over it.

%description -l pl.UTF-8
Narzędzie służące do mierzenia pojemności sieci przez wysyłanie przez
nią strumieni TCP.

%package devel
Summary:	Header files for thrulay library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki thrulay
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for thrulay library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki thrulay.

%package static
Summary:	Static thrulay library
Summary(pl.UTF-8):	Statyczna biblioteka thrulay
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static thrulay library.

%description static -l pl.UTF-8
Statyczna biblioteka thrulay.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README TODO
%attr(755,root,root) %{_bindir}/thrulay
%attr(755,root,root) %{_sbindir}/thrulayd
%attr(755,root,root) %{_libdir}/libthrulay.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libthrulay.so.0
%{_mandir}/man1/thrulay.1*
%{_mandir}/man8/thrulayd.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libthrulay.so
%{_libdir}/libthrulay.la
%{_includedir}/thrulay

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libthrulay.a
%endif
