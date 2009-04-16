# TODO: use system libevent
Summary:	A versatile and multi-platform BitTorrent client
Summary(hu.UTF-8):	Egy sokoldalú és multiplatformos BitTorrent kliens
Summary(pl.UTF-8):	Wszechstronny i wieloplatformowy klient BitTorrenta
Name:		transmission
Version:	1.52
Release:	1
License:	MIT
Group:		Applications/Communications
Source0:	http://download.m0k.org/transmission/files/%{name}-%{version}.tar.bz2
# Source0-md5:	2a1a628c2a8872934575cb4351bca291
Patch0:		%{name}-ckb_po.patch
URL:		http://transmissionbt.com/
BuildRequires:	curl-devel >= 7.15.0
BuildRequires:	dbus-glib-devel >= 0.70
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool >= 0.35.5
#BuildRequires:	libevent-devel
BuildRequires:	libnotify-devel >= 0.4.4
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel >= 0.9.4
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.357
Obsoletes:	Transmission <= 1.05
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/%{name}/web

%description
Transmission has been built from the ground up to be a lightweight,
yet powerful BitTorrent client. Its simple, intuitive interface is
designed to integrate tightly with whatever computing environment you
choose to use. Transmission strikes a balance between providing useful
functionality without feature bloat.

%description -l hu.UTF-8
Transmission egy könnyűsúlyú de mégis egy erőteljes BitTorrent kliens.
Egyszerű, intuitív felülete szorosan illeszkedik bármilyen
számítógépes környezetbe, amit csak választasz. A Transmission célja
megtalálni a használható funkcionalitást lehetőségek áradata nélkül.

%description -l pl.UTF-8
Transmission został stworzony od podstaw, aby być lekkim lecz mającym
duże możliwości klientem BitTorrenta. Jego prosty, intuicyjny
interfejs jest zaprojektowany spójnie z dowolnym środowiskiem wybranym
przez użytkownika. Transmission stawia na równowagę zapewnienia
przydatnej funkcjonalności bez nadmiaru opcji.

%package gui
Summary:	A versatile and multi-platform BitTorrent client
Summary(pl.UTF-8):	Wszechstronny i wieloplatformowy klient BitTorrenta
Group:		X11/Applications/Communications
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	gtk+2
Requires:	gtk+2 >= 2:2.6.0
Requires:	%{name}-%{version}-%{release}

%description gui
Transmission has been built from the ground up to be a lightweight,
yet powerful BitTorrent client. Its simple, intuitive interface is
designed to integrate tightly with whatever computing environment you
choose to use. Transmission strikes a balance between providing useful
functionality without feature bloat.

%description gui -l hu.UTF-8
Transmission egy könnyűsúlyú de mégis egy erőteljes BitTorrent kliens.
Egyszerű, intuitív felülete szorosan illeszkedik bármilyen
számítógépes környezetbe, amit csak választasz. A Transmission célja
megtalálni a használható funkcionalitást lehetőségek áradata nélkül.

%description gui -l pl.UTF-8
Transmission został stworzony od podstaw, aby być lekkim lecz mającym
duże możliwości klientem BitTorrenta. Jego prosty, intuicyjny
interfejs jest zaprojektowany spójnie z dowolnym środowiskiem wybranym
przez użytkownika. Transmission stawia na równowagę zapewnienia
przydatnej funkcjonalności bez nadmiaru opcji.

%prep
%setup -q -c -n transmission-%{version}
mv transmission-%{version}/* .
%patch0 -p1
%{__rm} po/ckb.po

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name --with-gnome

# unsupported
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/eu

# copy of GPLv2 not needed
%{__rm} $RPM_BUILD_ROOT%{_datadir}/transmission/web/LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%post gui
%update_desktop_database_post
%update_icon_cache hicolor

%postun gui
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/transmissioncli
%attr(755,root,root) %{_bindir}/transmission-daemon
%attr(755,root,root) %{_bindir}/transmission-remote
%{_mandir}/man1/*.1*
%dir %{_datadir}/%{name}
%dir %{_appdir}
%{_appdir}/images
%{_appdir}/javascript
%{_appdir}/stylesheets
%{_appdir}/index.html

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/transmission
%{_desktopdir}/transmission.desktop
%{_pixmapsdir}/transmission.png
%{_iconsdir}/hicolor/*/apps/transmission.png
%{_iconsdir}/hicolor/*/apps/transmission.svg
