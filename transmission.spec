#
# Conditional build:
%bcond_without	gtk		# without GTK GUI
%bcond_with	gtk4		# use GTK4 for GTK GUI
%bcond_without	qt		# without Qt GUI
%bcond_with	qt6		# use Qt6 for Qt GUI
%bcond_without	systemd		# without systemd unit

%define		qtver	5.6

Summary:	A versatile and multi-platform BitTorrent client
Summary(hu.UTF-8):	Egy sokoldalú és multiplatformos BitTorrent kliens
Summary(pl.UTF-8):	Wszechstronny i wieloplatformowy klient BitTorrenta
Name:		transmission
Version:	4.0.6
Release:	1
License:	MIT
Group:		Applications/Communications
Source0:	https://github.com/transmission/transmission/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	8132b9f012b8e6309911c80ee9fd00f7
Source1:	%{name}.sysconfig
Source2:	%{name}.init
URL:		http://transmissionbt.com/
BuildRequires:	cmake >= 3.12
BuildRequires:	curl-devel >= 7.28.0
BuildRequires:	gettext-tools
%if %{with gtk}
%if %{with gtk4}
BuildRequires:	glibmm2.68-devel >= 2.60.0
BuildRequires:	gtkmm4-devel >= 3.24.0
%else
BuildRequires:	glibmm-devel >= 2.60.0
BuildRequires:	gtkmm3-devel >= 3.24.0
BuildRequires:	libayatana-appindicator-gtk3-devel
%endif
%endif
BuildRequires:	libb64-devel
BuildRequires:	libdeflate-devel >= 1.7
BuildRequires:	libevent-devel >= 2.1.0
BuildRequires:	libnatpmp-devel
BuildRequires:	libpsl-devel >= 0.21.1
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	lsb-release
BuildRequires:	miniupnpc-devel >= 1.7
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.742
%{?with_systemd:BuildRequires:	systemd-devel}
BuildRequires:	tar >= 1:1.22
BuildRequires:	xfsprogs-devel
BuildRequires:	xz
%if %{with qt}
%if %{with qt6}
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Network-devel >= %{qtver}
BuildRequires:	Qt6Svg-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	qt6-linguist >= %{qtver}
%else
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Svg-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	qt5-linguist >= %{qtver}
%endif
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Transmission has been built from the ground up to be a lightweight,
yet powerful BitTorrent client. Its simple, intuitive interface is
designed to integrate tightly with whatever computing environment you
choose to use. Transmission strikes a balance between providing useful
functionality without feature bloat.

%description -l hu.UTF-8
Transmission egy könnyűsúlyú, de mégis egy erőteljes BitTorrent
kliens. Egyszerű, intuitív felülete szorosan illeszkedik bármilyen
számítógépes környezetbe, amit csak választasz. A Transmission célja
megtalálni a használható funkcionalitást lehetőségek áradata nélkül.

%description -l pl.UTF-8
Transmission został stworzony od podstaw, aby być lekkim lecz mającym
duże możliwości klientem BitTorrenta. Jego prosty, intuicyjny
interfejs jest zaprojektowany spójnie z dowolnym środowiskiem wybranym
przez użytkownika. Transmission stawia na równowagę zapewnienia
przydatnej funkcjonalności bez nadmiaru opcji.

%package cli
Summary:	Command line implementation for BitTorrent client
Summary(pl.UTF-8):	Implementacja w wierszu poleceń dla klienta BitTorrenta
Group:		Applications/Networking
Requires:	%{name}-common = %{version}-%{release}
Requires:	curl-libs >= 7.28.0
Requires:	libdeflate >= 1.7
Requires:	libevent >= 2.1.0
Requires:	libpsl >= 0.21.1
Requires:	miniupnpc >= 1.7
Requires:	openssl >= 0.9.7

%description cli
Transmission has been built from the ground up to be a lightweight,
yet powerful BitTorrent client. Its simple, intuitive interface is
designed to integrate tightly with whatever computing environment you
choose to use. Transmission strikes a balance between providing useful
functionality without feature bloat.

Command line implementation for BitTorrent client.

%description cli -l hu.UTF-8
Transmission egy könnyűsúlyú, de mégis egy erőteljes BitTorrent
kliens. Egyszerű, intuitív felülete szorosan illeszkedik bármilyen
számítógépes környezetbe, amit csak választasz. A Transmission célja
megtalálni a használható funkcionalitást lehetőségek áradata nélkül.

%description cli -l pl.UTF-8
Transmission został stworzony od podstaw, aby być lekkim lecz mającym
duże możliwości klientem BitTorrenta. Jego prosty, intuicyjny
interfejs jest zaprojektowany spójnie z dowolnym środowiskiem wybranym
przez użytkownika. Transmission stawia na równowagę zapewnienia
przydatnej funkcjonalności bez nadmiaru opcji.

Implementacja w wierszu poleceń dla klienta BitTorrenta.

%package common
Summary:	Common files for Transmission BitTorrent client
Summary(pl.UTF-8):	Pliki wspólne dla klienta BitTorrenta Transmission
Group:		Applications/Networking
BuildArch:	noarch

%description common
Common files for Transmission BitTorrent client.

%description common -l pl.UTF-8
Pliki wspólne dla klienta BitTorrenta Transmission.

%package daemon
Summary:	Daemon package for BitTorrent client
Summary(pl.UTF-8):	Pakiet demona dla klienta BitTorrenta
Group:		Networking/Daemons
Requires:	%{name}-common = %{version}-%{release}
Requires:	curl-libs >= 7.28.0
Requires:	libdeflate >= 1.7
Requires:	libevent >= 2.1.0
Requires:	libpsl >= 0.21.1
Requires:	miniupnpc >= 1.7
Requires:	openssl >= 0.9.7
%{?with_systemd:Requires:	systemd-units >= 38}
Provides:	group(transmission)
Provides:	user(transmission)
Obsoletes:	Transmission <= 1.05
Obsoletes:	transmission < 3.00-2
Obsoletes:	transmission-init < 3.00-2

%description daemon
Transmission has been built from the ground up to be a lightweight,
yet powerful BitTorrent client. Its simple, intuitive interface is
designed to integrate tightly with whatever computing environment you
choose to use. Transmission strikes a balance between providing useful
functionality without feature bloat.

Daemon package for BitTorrent client.

%description daemon -l hu.UTF-8
Transmission egy könnyűsúlyú, de mégis egy erőteljes BitTorrent
kliens. Egyszerű, intuitív felülete szorosan illeszkedik bármilyen
számítógépes környezetbe, amit csak választasz. A Transmission célja
megtalálni a használható funkcionalitást lehetőségek áradata nélkül.

%description daemon -l pl.UTF-8
Transmission został stworzony od podstaw, aby być lekkim lecz mającym
duże możliwości klientem BitTorrenta. Jego prosty, intuicyjny
interfejs jest zaprojektowany spójnie z dowolnym środowiskiem wybranym
przez użytkownika. Transmission stawia na równowagę zapewnienia
przydatnej funkcjonalności bez nadmiaru opcji.

Pakiet demona dla klienta BitTorrenta.

%package gui
Summary:	A versatile and multi-platform BitTorrent client
Summary(pl.UTF-8):	Wszechstronny i wieloplatformowy klient BitTorrenta
Group:		X11/Applications/Networking
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name}-common = %{version}-%{release}
Requires:	curl-libs >= 7.28.0
%if %{with gtk4}
Requires:	glibmm2.68 >= 2.60.0
Requires:	gtkmm4 >= 3.24.0
%else
Requires:	glibmm >= 2.60.0
Requires:	gtkmm3 >= 3.24.0
%endif
Requires:	libcanberra-gtk3
Requires:	libdeflate >= 1.7
Requires:	libevent >= 2.1.0
Requires:	libpsl >= 0.21.1
Requires:	miniupnpc >= 1.7
Requires:	openssl >= 0.9.7

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

%package gui-qt
Summary:	A GUI to Transmission based on Qt 5
Summary(pl.UTF-8):	Graficzny interfejs do Transmission oparty na Qt 5
Group:		X11/Applications/Networking
Requires:	%{name}-common = %{version}-%{release}
%if %{with qt6}
Requires:	Qt6Core >= %{qtver}
Requires:	Qt6DBus >= %{qtver}
Requires:	Qt6Gui >= %{qtver}
Requires:	Qt6Network >= %{qtver}
Requires:	Qt6Svg >= %{qtver}
Requires:	Qt6Widgets >= %{qtver}
%else
Requires:	Qt5Core >= %{qtver}
Requires:	Qt5DBus >= %{qtver}
Requires:	Qt5Gui >= %{qtver}
Requires:	Qt5Network >= %{qtver}
Requires:	Qt5Svg >= %{qtver}
Requires:	Qt5Widgets >= %{qtver}
%endif
Requires:	curl-libs >= 7.28.0
Requires:	libcanberra-gtk3
Requires:	libdeflate >= 1.7
Requires:	libevent >= 2.1.0
Requires:	libpsl >= 0.21.1
Requires:	miniupnpc >= 1.7
Requires:	openssl >= 0.9.7

%description gui-qt
A GUI to Transmission based on Qt 5.

%description gui-qt -l pl.UTF-8
Graficzny interfejs do Transmission oparty na Qt 5.

%package utils
Summary:	Utilities for Transmission BitTorrent client
Summary(pl.UTF-8):	Narzędzia dla klienta BitTorrenta Transmission
Group:		Applications/Networking

%description utils
Utilities for Transmission BitTorrent client.

%description utils -l pl.UTF-8
Narzędzia dla klienta BitTorrenta Transmission.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DENABLE_CLI:BOOL=ON \
	%{cmake_on_off gtk ENABLE_GTK} \
	-DUSE_GTK_VERSION=%{?with_gtk4:4}%{!?with_gtk4:3} \
	%{cmake_on_off qt ENABLE_QT} \
	-DUSE_QT_VERSION=%{?with_qt6:6}%{!?with_qt6:5} \
	%{cmake_on_off systemd ENABLE_SYSTEMD}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{sysconfig,rc.d/init.d} \
	$RPM_BUILD_ROOT%{_sysconfdir}/%{name} \
	$RPM_BUILD_ROOT/var/lib/%{name} \
	%{?with_systemd:$RPM_BUILD_ROOT%{systemdunitdir}}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}

%if %{with systemd}
cp -p daemon/transmission-daemon.service $RPM_BUILD_ROOT%{systemdunitdir}
%endif

%if %{with gtk}
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{ceb,jbo,pt_PT}

%find_lang %{name} --all-name --with-gnome
%endif

%if %{with qt}
%find_lang %{name} --with-qm -o %{name}-qt.lang
%endif


%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun daemon -- transmission < 3.00-2
if [ -d /var/lib/transmission ] ; then
	chown -R transmission:transmission /var/lib/transmission || :
fi

%pre daemon
%groupadd -g 339 transmission
%useradd -u 339 -r -d /var/lib/transmission -s /bin/false -c "Transmission user" -g transmission transmission

%post daemon
/sbin/chkconfig --add transmission
%service transmission restart
%{?with_systemd:%systemd_post transmission-daemon.service}

%preun daemon
if [ "$1" = "0" ]; then
	%service transmission stop
	/sbin/chkconfig --del transmission
fi
%{?with_systemd:%systemd_preun transmission-daemon.service}

%postun daemon
if [ "$1" = "0" ]; then
	%userremove transmission
	%groupremove transmission
fi
%{?with_systemd:%systemd_reload}

%post gui
%update_desktop_database_post
%update_icon_cache hicolor

%postun gui
%update_desktop_database_postun
%update_icon_cache hicolor

%files cli
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/transmission-cli
%{_mandir}/man1/transmission-cli.1*

%files common
%defattr(644,root,root,755)
%doc AUTHORS README.md
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/public_html

%files daemon
%defattr(644,root,root,755)
%attr(751,root,daemon) %dir %{_sysconfdir}/%{name}
%attr(640,root,daemon) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%attr(755,root,root) %{_bindir}/transmission-daemon
%{?with_systemd:%{systemdunitdir}/transmission-daemon.service}
%{_mandir}/man1/transmission-daemon.1*
%attr(750,transmission,transmission) %dir /var/lib/%{name}

%if %{with gtk}
%files gui -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/transmission-gtk
%{_mandir}/man1/transmission-gtk.1*
%{_desktopdir}/transmission-gtk.desktop
%{_iconsdir}/hicolor/scalable/apps/transmission.svg
%{_iconsdir}/hicolor/scalable/apps/transmission-devel.svg
%{_iconsdir}/hicolor/symbolic/apps/transmission-symbolic.svg
%{_datadir}/metainfo/transmission-gtk.metainfo.xml
%endif

%if %{with qt}
%files gui-qt -f %{name}-qt.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/transmission-qt
%dir %{_datadir}/%{name}/translations
%{_desktopdir}/transmission-qt.desktop
%{_mandir}/man1/transmission-qt.1*
%endif

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/transmission-create
%attr(755,root,root) %{_bindir}/transmission-edit
%attr(755,root,root) %{_bindir}/transmission-remote
%attr(755,root,root) %{_bindir}/transmission-show
%{_mandir}/man1/transmission-create.1*
%{_mandir}/man1/transmission-edit.1*
%{_mandir}/man1/transmission-remote.1*
%{_mandir}/man1/transmission-show.1*
