Summary:	thrulay
Summary(pl.UTF-8):	thrulay
Name:		thrulay
Version:	0.8
Release:	0.1
License:	BSD Like (see included LICENSE)
Group:		Applications
Source0:	http://shlang.com/thrulay/%{name}-%{version}.tar.gz
# Source0-md5:	725fb13344608a652e818bcd16fe9ef6
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-mandir.patch
URL:		http://www.internet2.edu/~shalunov/thrulay/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The program thrulay is used to measure the capacity of a network by
sending a bulk TCP stream over it.

%description -l pl.UTF-8
Narzędzie służące do mierzenia pojemności sieci przez wysyłanie przez
nią strumieni TCP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO LICENSE
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_sbindir}/%{name}d
%{_mandir}/man?/%{name}*
