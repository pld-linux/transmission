Summary:	A versatile and multi-platform BitTorrent client
Summary(pl.UTF-8):	Wszechstronny i wieloplatformowy klient BitTorrenta
Name:		transmission
Version:	1.20
Release:	1
License:	MIT
Group:		Applications/Communications
Source0:	http://download.m0k.org/transmission/files/transmission-%{version}.tar.bz2
# Source0-md5:	6e0b25b10842fdac8a2206f29e951c0d
URL:		http://transmission.m0k.org/
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libevent-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.357
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	gtk+2
Requires:	gtk+2 >= 2:2.6.0
Obsoletes:	Transmission <= 1.05
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Transmission has been built from the ground up to be a lightweight,
yet powerful BitTorrent client. Its simple, intuitive interface is
designed to integrate tightly with whatever computing environment you
choose to use. Transmission strikes a balance between providing useful
functionality without feature bloat.

%description -l pl.UTF-8
Transmission został stworzony od podstaw, aby być lekkim lecz mającym
duże możliwości klientem BitTorrenta. Jego prosty, intuicyjny
interfejs jest zaprojektowany spójnie z dowolnym środowiskiem wybranym
przez użytkownika. Transmission stawia na równowagę zapewnienia
przydatnej funkcjonalności bez nadmiaru opcji.

%prep
%setup -q -c -n transmission-%{version}
mv transmission-%{version}/* .

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#mv $RPM_BUILD_ROOT/usr{,/share}/man

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/benc2php
%attr(755,root,root) %{_bindir}/transmission
%attr(755,root,root) %{_bindir}/transmissioncli
%attr(755,root,root) %{_bindir}/transmission-daemon
%attr(755,root,root) %{_bindir}/transmission-proxy
%attr(755,root,root) %{_bindir}/transmission-remote
%{_mandir}/man1/*.1*
%{_desktopdir}/transmission.desktop
%{_pixmapsdir}/transmission.png
%{_iconsdir}/hicolor/*/apps/transmission.png
%{_iconsdir}/hicolor/*/apps/transmission.svg
