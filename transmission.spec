#
# Conditional build:
%bcond_with	verchange	# changes client version identification to 2.42

Summary:	A versatile and multi-platform BitTorrent client
Summary(hu.UTF-8):	Egy sokoldalú és multiplatformos BitTorrent kliens
Summary(pl.UTF-8):	Wszechstronny i wieloplatformowy klient BitTorrenta
Name:		transmission
Version:	2.94
Release:	4
License:	MIT
Group:		Applications/Communications
Source0:	https://github.com/transmission/transmission-releases/raw/master/%{name}-%{version}.tar.xz
# Source0-md5:	c92829294edfa391c046407eeb16358a
Source1:	%{name}.sysconfig
Source2:	%{name}.init
Patch0:		%{name}-ckb_po.patch
Patch2:		%{name}-version.patch
URL:		http://transmissionbt.com/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	curl-devel >= 7.16.3
BuildRequires:	dbus-glib-devel >= 0.70
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gtk+3-devel >= 3.4.0
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libcanberra-gtk-devel
BuildRequires:	libevent-devel >= 2.0.10
BuildRequires:	libnotify-devel >= 0.4.4
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	lsb-release
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	pkgconfig
BuildRequires:	qt5-build
BuildRequires:	qt5-qmake
BuildRequires:	rpmbuild(macros) >= 1.357
BuildRequires:	sqlite3-devel
BuildRequires:	systemd-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	util-linux
BuildRequires:	which
BuildRequires:	xfsprogs-devel
BuildRequires:	xz
BuildRequires:	zlib-devel >= 1.2.3
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

%package init
Summary:	Daemon package for BitTorrent client
Summary(pl.UTF-8):	Pakiet demona dla klienta BitTorrenta
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description init
Daemon package for BitTorrent client.

%description init -l pl.UTF-8
Pakiet demona dla klienta BitTorrenta.

%package gui
Summary:	A versatile and multi-platform BitTorrent client
Summary(pl.UTF-8):	Wszechstronny i wieloplatformowy klient BitTorrenta
Group:		X11/Applications/Networking
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name} = %{version}-%{release}
Requires:	glib2 >= 1:2.32.0
Requires:	gtk+3 >= 3.2.0

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
# doesn't require base

%description gui-qt
A GUI to Transmission based on Qt 5.

%description gui-qt -l pl.UTF-8
Graficzny interfejs do Transmission oparty na Qt 5.

%prep
%setup -qc
%{__mv} %{name}-%{version}/* .
%patch0 -p1
%if %{with verchange}
%patch2 -p1
./update-version-h.sh
%endif

%{__rm} po/ckb.po
%{__sed} -i 's/\(^CONFIG.*\)\( debug\)/\1/' qt/qtr.pro

%build
%configure \
	--with-gtk \
	--disable-silent-rules \
	--enable-cli
%{__make}

cd qt
qmake-qt5
%{__make}
cd -

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{sysconfig,rc.d/init.d} \
	$RPM_BUILD_ROOT%{_sysconfdir}/%{name} \
	$RPM_BUILD_ROOT/var/lib/%{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}

install qt/transmission-qt $RPM_BUILD_ROOT%{_bindir}
install qt/transmission-qt.desktop $RPM_BUILD_ROOT%{_desktopdir}
install gtk/transmission.png $RPM_BUILD_ROOT%{_pixmapsdir}/transmission-qt.png

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{ta_LK,ta}

%find_lang %{name} --all-name --with-gnome

# copy of GPLv2 not needed
%{__rm} $RPM_BUILD_ROOT%{_appdir}/LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%post init
/sbin/chkconfig --add transmission
%service transmission restart

%preun init
if [ "$1" = "0" ]; then
        %service transmission stop
        /sbin/chkconfig --del transmission
fi

%post gui
%update_desktop_database_post
%update_icon_cache hicolor

%postun gui
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/transmission-cli
%attr(755,root,root) %{_bindir}/transmission-create
%attr(755,root,root) %{_bindir}/transmission-daemon
%attr(755,root,root) %{_bindir}/transmission-edit
%attr(755,root,root) %{_bindir}/transmission-remote
%attr(755,root,root) %{_bindir}/transmission-show
%{_mandir}/man1/transmission-cli.1*
%{_mandir}/man1/transmission-create.1*
%{_mandir}/man1/transmission-daemon.1*
%{_mandir}/man1/transmission-edit.1*
%{_mandir}/man1/transmission-remote.1*
%{_mandir}/man1/transmission-show.1*
%dir %{_datadir}/%{name}
%dir %{_appdir}
%{_appdir}/images
%{_appdir}/javascript
%{_appdir}/style
%{_appdir}/index.html

%files init
%defattr(644,root,root,755)
%attr(751,root,daemon) %dir %{_sysconfdir}/%{name}
#%attr(640,root,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*
%attr(640,root,daemon) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%attr(750,daemon,root) %dir /var/lib/%{name}

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/transmission-gtk
%{_mandir}/man1/transmission-gtk.1*
%{_desktopdir}/transmission-gtk.desktop
%{_pixmapsdir}/transmission.png
%{_iconsdir}/hicolor/*/apps/transmission.png
%{_iconsdir}/hicolor/*/apps/transmission.svg

%files gui-qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/transmission-qt
%{_desktopdir}/transmission-qt.desktop
%{_pixmapsdir}/transmission-qt.png
