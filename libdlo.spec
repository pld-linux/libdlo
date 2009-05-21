Summary:	DisplayLink library
Summary(pl.UTF-8):	Biblioteka DisplayLink
Name:		libdlo
Version:	0.1.0
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://people.freedesktop.org/~berniet/%{name}-%{version}.tar.gz
# Source0-md5:	1b8b20928a14010a3a4c2d507268d33c
URL:		http://freedesktop.org/wiki/Software/libdlo
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libusb-compat-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdlo is an open-source implementation of DisplayLink USB graphics
software.

%description -l pl.UTF-8
libdlo jest otwartą implementacją DisplayLink USB graphics software.

%package devel
Summary:	Header files for libdlo library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libdlo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libdlo library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libdlo.

%package static
Summary:	Static libdlo library
Summary(pl.UTF-8):	Statyczna biblioteka libdlo
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libdlo library.

%description static -l pl.UTF-8
Statyczna biblioteka libdlo.

%prep
%setup -q
%{__sed} -i -e 's/${libdir_name}/${libdir}/g' configure.ac
%{__sed} -i -e 's/libdlo.h/..\/src\/libdlo.h/g' test/test1.c

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
	libdir_name=%{_lib}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING Guide-v104.pdf README
%attr(755,root,root) %{_libdir}/libdlo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdlo.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdlo.so
%{_libdir}/libdlo.la
%{_includedir}/libdlo.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libdlo.a
