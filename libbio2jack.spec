Summary:	Library for simple porting of blocked I/O audio applications to Jack
Name:		libbio2jack
Version:	0.4
Release:	0.1
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/sourceforge/bio2jack/bio2jack-%{version}.tar.gz
# Source0-md5:	5716454ab1a5115604af18b5078f99be
URL:		http://bio2jack.sourceforge.net/
BuildRequires:	jack-audio-connection-kit-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for enabling easy porting of blocked io(OSS/ALSA)
applications to the jack sound server. This library allows the person
porting the code to simply replace the calls into OSS/ALSA with calls
into interface functions of this library. The library buffers a small
amount of audio data and takes care of the rest of the jack
implementation including the linked list of audio data buffers and the
jack callback.

%package devel
Summary:	Header files for bio2jack library
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for bio2jack library.

%package static
Summary:	Static bio2jack library
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static bio2jack library.

%prep
%setup -q -n bio2jack
rm -rf .libs

%build
%{__libtoolize}
#%{__aclocal}
#%{__autoconf}
#%{__autoheader}
#%{__automake}
%configure
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D bio2jack.h $RPM_BUILD_ROOT%{_includedir}/bio2jack.h

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
%{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
