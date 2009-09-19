Summary:	A versatile and multi-platform BitTorrent client
Summary(hu.UTF-8):	Egy sokoldalú és multiplatformos BitTorrent kliens
Summary(pl.UTF-8):	Wszechstronny i wieloplatformowy klient BitTorrenta
Name:		transmission
Version:	1.75
Release:	1
License:	MIT
Group:		Applications/Communications
Source0:	http://download.m0k.org/transmission/files/%{name}-%{version}.tar.bz2
# Source0-md5:	ec09b76ca941f5c389d8dd4f469f1fa6
Source1:	%{name}.sysconfig
Source2:	%{name}.init
Patch0:		%{name}-ckb_po.patch
Patch1:		%{name}-qtr_details.patch
Patch2:		%{name}-preallocate_syscall.patch
URL:		http://transmissionbt.com/
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel >= 7.16.3
BuildRequires:	dbus-glib-devel >= 0.70
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libevent-devel >= 1.4.5
BuildRequires:	libnotify-devel >= 0.4.4
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.4
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.357
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	xfsprogs-devel
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
Transmission egy könnyűsúlyú, de mégis egy erőteljes BitTorrent kliens.
Egyszerű, intuitív felülete szorosan illeszkedik bármilyen
számítógépes környezetbe, amit csak választasz. A Transmission célja
megtalálni a használható funkcionalitást lehetőségek áradata nélkül.

%description -l pl.UTF-8
Transmission został stworzony od podstaw, aby być lekkim lecz mającym
duże możliwości klientem BitTorrenta. Jego prosty, intuicyjny
interfejs jest zaprojektowany spójnie z dowolnym środowiskiem wybranym
przez użytkownika. Transmission stawia na równowagę zapewnienia
przydatnej funkcjonalności bez nadmiaru opcji.

%package init
Summary:	daemon package for BitTorrent client
Group:		Daemon
Requires:	%{name} = %{version}-%{release}

%description init
Transmission has been built from the ground up to be a lightweight,
yet powerful BitTorrent client. Its simple, intuitive interface is
designed to integrate tightly with whatever computing environment you
choose to use. Transmission strikes a balance between providing useful
functionality without feature bloat.

%package gui
Summary:	A versatile and multi-platform BitTorrent client
Summary(pl.UTF-8):	Wszechstronny i wieloplatformowy klient BitTorrenta
Group:		X11/Applications/Communications
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	gtk+2
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2 >= 2:2.6.0

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
Summary:	A GUI to Transmission based on Qt4
Group:		X11/Applications/Communications
# doesn't require base

%description gui-qt
A GUI to Transmission based on Qt4.

%prep
%setup -q -c -n transmission-%{version}
mv transmission-%{version}/* .
%patch0 -p1
%patch1 -p1
%patch2 -p1
%{__rm} po/ckb.po

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

cd qt
%{__sed} -i 's/CONFIG += qt thread debug/CONFIG += qt thread/' qtr.pro
qmake-qt4
%{__make}
cd -

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{%{name},sysconfig,rc.d/init.d} \
	$RPM_BUILD_ROOT/var/lib/%{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}

# unsupported
%{__rm} -rf $RPM_BUILD_ROOT%{_localedir}/eu

%find_lang %{name} --all-name --with-gnome

install qt/qtr $RPM_BUILD_ROOT%{_bindir}

# copy of GPLv2 not needed
%{__rm} $RPM_BUILD_ROOT%{_datadir}/transmission/web/LICENSE

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
%attr(755,root,root) %{_bindir}/transmissioncli
%attr(755,root,root) %{_bindir}/transmission-daemon
%attr(755,root,root) %{_bindir}/transmission-remote
%{_mandir}/man1/transmissioncli.1*
%{_mandir}/man1/transmission-daemon.1*
%{_mandir}/man1/transmission-remote.1*
%dir %{_datadir}/%{name}
%dir %{_appdir}
%{_appdir}/images
%{_appdir}/javascript
%{_appdir}/stylesheets
%{_appdir}/index.html

%files init
%defattr(644,root,root,755)
%attr(751,root,daemon) %dir /etc/%{name}
#%attr(640,root,daemon) %config(noreplace) %verify(not md5 mtime size) /etc/%{name}/*
%attr(640,root,daemon) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%attr(750,daemon,root) %dir /var/lib/%{name}

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/transmission
%{_mandir}/man1/transmission.1*
%{_desktopdir}/transmission.desktop
%{_pixmapsdir}/transmission.png
%{_iconsdir}/hicolor/*/apps/transmission.png
%{_iconsdir}/hicolor/*/apps/transmission.svg

%files gui-qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qtr
