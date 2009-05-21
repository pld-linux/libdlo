Summary:	DisplayLink library
Summary(pl.UTF-8):	Biblioteka DisplayLink
Name:		libdlo
Version:	0.1.0
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://people.freedesktop.org/~berniet/%{name}-%{version}.tar.gz
# Source0-md5:	1b8b20928a14010a3a4c2d507268d33c
URL:		http://libdlo.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
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

cp ~/rpm/BUILD/libdlo-0.1.0/src/libdlo.h ~/rpm/BUILD/libdlo-0.1.0/test/

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	libdir_name=%{_lib}

%{__make} libdir_name=%{_lib}

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
%attr(755,root,root) %{_libdir}/libdlo.so*
%doc AUTHORS COPYING Guide-v104.pdf README

%files devel
%defattr(644,root,root,755)
%{_libdir}/libdlo.la
%{_includedir}/libdlo.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libdlo.a