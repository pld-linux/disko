Summary:	Disko - multimedia framework on top of DirectFB
Summary(pl.UTF-8):	Disko - szkielet multimedialny oparty na DirectFB
Name:		disko
Version:	1.1.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://www.directfb.org/downloads/Libs/%{name}-%{version}.tar.bz2
# Source0-md5:	d34dfecc32590025caaa47a59225651f
Patch0:		%{name}-libdir.patch
URL:		http://www.directfb.org/index.php?path=Projects/Disko
BuildRequires:	DirectFB-devel >= 1:1.2.0
BuildRequires:	alsa-lib-devel
BuildRequires:	curl-devel
BuildRequires:	libsigc++-devel >= 2.0
BuildRequires:	libxml2-devel >= 1:2.6
BuildRequires:	pkgconfig >= 1:0.9
BuildRequires:	sqlite3-devel
BuildRequires:	unixODBC-devel
BuildRequires:	xine-lib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Disko is an application framework for digital media devices.

%description -l pl.UTF-8
Disko to szkielet aplikacji dla cyfrowych urządzeń multimedialnych.

%package devel
Summary:	Header files for the Disko libraries
Summary(pl.UTF-8):	Pliki nagłówkowe dla bibliotek Disko
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	DirectFB-devel >= 1:1.2.0
Requires:	alsa-lib-devel
Requires:	curl-devel
Requires:	libsigc++-devel >= 2.0
Requires:	libxml2-devel >= 1:2.6
Requires:	sqlite3-devel
Requires:	unixODBC-devel
Requires:	xine-lib-devel

%description devel
Header files for Disko libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla bibliotek Disko.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{rpmcflags} -fPIC" \
%{__make} \
	CXX="%{__cxx}" \
	DEBUG_FLAG_SET=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	libdir=%{_libdir} \
	incdir=%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post 	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libmmsbase.so
%attr(755,root,root) %{_libdir}/libmmsconfig.so
%attr(755,root,root) %{_libdir}/libmmscore.so
%attr(755,root,root) %{_libdir}/libmmsdata.so
%attr(755,root,root) %{_libdir}/libmmsgui.so
%attr(755,root,root) %{_libdir}/libmmsinput.so
%attr(755,root,root) %{_libdir}/libmmsmedia.so
%attr(755,root,root) %{_libdir}/libmmstools.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/mmsbase
%{_includedir}/mmsconfig
%{_includedir}/mmscore
%{_includedir}/mmsdata
%{_includedir}/mmsgui
%{_includedir}/mmsinput
%{_includedir}/mmsmedia
%{_includedir}/mmstools
%{_includedir}/mms.h
%{_pkgconfigdir}/disko.pc
