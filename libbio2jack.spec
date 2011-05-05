#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Library for simple porting of blocked I/O audio applications to JACK
Summary(pl.UTF-8):	Biblioteka do łatwego portowania aplikacji z blokującym we/wy dźwięku do JACK
Name:		libbio2jack
Version:	0.9
Release:	2
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/bio2jack/bio2jack-%{version}.tar.gz
# Source0-md5:	00b64a99856cb35f1170c97ecb6bc431
Patch0:		%{name}-GetJackLatency.patch
URL:		http://bio2jack.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for enabling easy porting of blocked I/O (OSS/ALSA)
applications to the JACK sound server. This library allows the person
porting the code to simply replace the calls into OSS/ALSA with calls
into interface functions of this library. The library buffers a small
amount of audio data and takes care of the rest of the JACK
implementation including the linked list of audio data buffers and the
JACK callback.

%description -l pl.UTF-8
Biblioteka umożliwiająca łatwe portowanie aplikacji z blokującym we/wy
dźwięku (OSS/ALSA) do serwera dźwięku JACK. Ta biblioteka pozwala
osobie portującej kod po prostu zastąpić wywołania OSS/ALSA
wywołaniami funkcji interfejsu tej biblioteki. Biblioteka buforuje
niewielką ilość danych dźwiękowych i dba o resztę implementacji JACK,
włącznie z powiązaną listą buforów danych dźwiękowych i wywołaniami
zwrotnymi.

%package devel
Summary:	Header files for bio2jack library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki bio2jack
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	jack-audio-connection-kit-devel

%description devel
Header files for bio2jack library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki bio2jack.

%package static
Summary:	Static bio2jack library
Summary(pl.UTF-8):	Statyczna biblioteka bio2jack
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static bio2jack library.

%description static -l pl.UTF-8
Statyczna biblioteka bio2jack.

%prep
%setup -q -n bio2jack
%patch0 -p1
rm -rf .libs

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make} clean
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D bio2jack.h $RPM_BUILD_ROOT%{_includedir}/bio2jack.h
install -D bio2jack-config $RPM_BUILD_ROOT%{_bindir}/bio2jack-config

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
%attr(755,root,root) %{_bindir}/bio2jack-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
