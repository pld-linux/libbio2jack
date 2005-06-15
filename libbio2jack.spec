%bcond_without	static_libs	# don't build static library
Summary:	Library for simple porting of blocked I/O audio applications to Jack
Summary(pl):	Biblioteka do ³atwego portowania aplikacji z blokuj±cym we/wy d¼wiêku do Jacka
Name:		libbio2jack
Version:	0.7
Release:	2
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/bio2jack/bio2jack-%{version}.tar.gz
# Source0-md5:	fc85546a02af757314be91f0934fcc91
URL:		http://bio2jack.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for enabling easy porting of blocked I/O (OSS/ALSA)
applications to the jack sound server. This library allows the person
porting the code to simply replace the calls into OSS/ALSA with calls
into interface functions of this library. The library buffers a small
amount of audio data and takes care of the rest of the jack
implementation including the linked list of audio data buffers and the
jack callback.

%description -l pl
Biblioteka umo¿liwiaj±ca ³atwe portowanie aplikacji z blokuj±cym we/wy
d¼wiêku (OSS/ALSA) do serwera d¼wiêku jack. Ta biblioteka pozwala
osobie portuj±cej kod po prostu zast±piæ wywo³ania OSS/ALSA
wywo³aniami funkcji interfejsu tej biblioteki. Biblioteka buforuje
niewielk± ilo¶æ danych d¼wiêkowym i dba o resztê implementacji jack,
w³±cznie z powi±zan± list± buforów danych d¼wiêkowych i wywo³aniami
zwrotnymi.

%package devel
Summary:	Header files for bio2jack library
Summary(pl):	Pliki nag³ówkowe biblioteki bio2jack
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	jack-audio-connection-kit-devel

%description devel
Header files for bio2jack library.

%description devel -l pl
Pliki nag³ówkowe biblioteki bio2jack.

%package static
Summary:	Static bio2jack library
Summary(pl):	Statyczna biblioteka bio2jack
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static bio2jack library.

%description static -l pl
Statyczna biblioteka bio2jack.

%prep
%setup -q -n bio2jack
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
