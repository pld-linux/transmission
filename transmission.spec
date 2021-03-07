#
# Conditional build:
%bcond_without	gtk		# without GTK GUI
%bcond_without	qt		# without Qt GUI
%bcond_without	systemd		# without systemd unit
%bcond_with	verchange	# changes client version identification to 2.42

%define		qtver	5.2

Summary:	A versatile and multi-platform BitTorrent client
Summary(hu.UTF-8):	Egy sokoldalú és multiplatformos BitTorrent kliens
Summary(pl.UTF-8):	Wszechstronny i wieloplatformowy klient BitTorrenta
Name:		transmission
Version:	3.00
Release:	2
License:	MIT
Group:		Applications/Communications
Source0:	https://github.com/transmission/transmission-releases/raw/master/%{name}-%{version}.tar.xz
# Source0-md5:	a23a32672b83c89b9b61e90408f53d98
Source1:	%{name}.sysconfig
Source2:	%{name}.init
Patch0:		%{name}-ckb_po.patch
Patch2:		%{name}-version.patch
URL:		http://transmissionbt.com/
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	curl-devel >= 7.16.3
BuildRequires:	gettext-tools
%if %{with gtk}
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gtk+3-devel >= 3.4.0
%endif
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libevent-devel >= 2.0.10
BuildRequires:	libnatpmp-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	lsb-release
BuildRequires:	miniupnpc-devel >= 1.7
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.357
BuildRequires:	systemd-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	util-linux
BuildRequires:	which
BuildRequires:	xfsprogs-devel
BuildRequires:	xz
BuildRequires:	zlib-devel >= 1.2.3
%if %{with qt}
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	qt5-qmake >= %{qtver}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/%{name}/web

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
Requires:	curl-libs >= 7.16.3
Requires:	libevent >= 2.0.10
Requires:	miniupnpc >= 1.7
Requires:	openssl >= 0.9.7
Requires:	zlib >= 1.2.3

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
Requires:	curl-libs >= 7.16.3
Requires:	libevent >= 2.0.10
Requires:	miniupnpc >= 1.7
Requires:	openssl >= 0.9.7
%{?with_systemd:Requires:	systemd-units >= 38}
Requires:	zlib >= 1.2.3
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
Requires:	curl-libs >= 7.16.3
Requires:	glib2 >= 1:2.32.0
Requires:	gtk+3 >= 3.4.0
Requires:	libcanberra-gtk3
Requires:	libevent >= 2.0.10
Requires:	miniupnpc >= 1.7
Requires:	openssl >= 0.9.7
Requires:	zlib >= 1.2.3

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
Requires:	Qt5Core >= %{qtver}
Requires:	Qt5DBus >= %{qtver}
Requires:	Qt5Gui >= %{qtver}
Requires:	Qt5Network >= %{qtver}
Requires:	Qt5Widgets >= %{qtver}
Requires:	curl-libs >= 7.16.3
Requires:	libcanberra-gtk3
Requires:	libevent >= 2.0.10
Requires:	miniupnpc >= 1.7
Requires:	openssl >= 0.9.7
Requires:	zlib >= 1.2.3

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
%patch0 -p1
%if %{with verchange}
%patch2 -p1
./update-version-h.sh
%endif

%{__rm} po/ckb.po
%{__sed} -i 's/\(^CONFIG.*\)\( debug\)/\1/' qt/qtr.pro

%build
%configure \
	%{__with_without gtk} \
	--disable-silent-rules \
	--enable-cli \
	--enable-external-natpmp
%{__make}

%if %{with qt}
cd qt
qmake-qt5
%{__make}
cd -
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{sysconfig,rc.d/init.d} \
	$RPM_BUILD_ROOT%{_sysconfdir}/%{name} \
	$RPM_BUILD_ROOT/var/lib/%{name} \
	%{?with_systemd:$RPM_BUILD_ROOT%{systemdunitdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}

%if %{with systemd}
cp -p daemon/transmission-daemon.service $RPM_BUILD_ROOT%{systemdunitdir}
%endif

%if %{with qt}
install qt/transmission-qt $RPM_BUILD_ROOT%{_bindir}
install qt/transmission-qt.desktop $RPM_BUILD_ROOT%{_desktopdir}
install gtk/transmission.png $RPM_BUILD_ROOT%{_pixmapsdir}/transmission-qt.png
%endif
%if %{with gtk}
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/jbo

%find_lang %{name} --all-name --with-gnome
%endif

# copy of GPLv2 not needed
%{__rm} $RPM_BUILD_ROOT%{_appdir}/LICENSE

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
%doc AUTHORS NEWS.md README.md
%dir %{_datadir}/%{name}
%dir %{_appdir}
%{_appdir}/images
%{_appdir}/javascript
%{_appdir}/style
%{_appdir}/index.html

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
%{_pixmapsdir}/transmission.png
%{_iconsdir}/hicolor/*/apps/transmission.svg
%{_datadir}/appdata/transmission-gtk.appdata.xml
%endif

%if %{with qt}
%files gui-qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/transmission-qt
%{_desktopdir}/transmission-qt.desktop
%{_pixmapsdir}/transmission-qt.png
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
