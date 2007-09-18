Summary:	GNOME media programs
Summary(fr.UTF-8):	Programmes multimédia de GNOME
Summary(pl.UTF-8):	Programy multimedialne dla GNOME
Name:		gnome-media
Version:	2.20.0
Release:	1
License:	GPL v2+/LGPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-media/2.20/%{name}-%{version}.tar.bz2
# Source0-md5:	d9206606050953a37bce61a3b1644137
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-configure.patch
Patch2:		%{name}-glsink.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.19.1
BuildRequires:	ORBit2-devel >= 1:2.14.9
%ifnarch sparc sparc64
BuildRequires:	alsa-lib-devel
%endif
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gnome-control-center-devel >= 1:2.20.0
BuildRequires:	esound-devel >= 1:0.2.37
BuildRequires:	gail-devel >= 1.20.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnome-vfs2-devel >= 2.20.0
BuildRequires:	gstreamer-devel >= 0.10.11
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.11
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libbonobo-devel >= 2.20.0
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomeui-devel >= 2.19.1
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.30
BuildRequires:	nautilus-cd-burner-devel >= 2.20.0
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper >= 0.3.11
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	gail >= 1.20.0
Requires:	gstreamer-GConf
Requires:	gstreamer-audiosink
Requires:	libgnomeui >= 2.19.1
Requires:	nautilus-cd-burner-libs >= 2.20.0
Obsoletes:	gnome
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gnomehelpdir	%{_datadir}/gnome/help

%description
GNOME media programs. GNOME is the GNU Network Object Model
Environment. That's a fancy name but really GNOME is a nice GUI
desktop environment. It makes using your computer easy, powerful, and
easy to configure.

%description -l fr.UTF-8
Programmes multimédia GNOME.

GNOME (GNU Network Object Model Environment) est un environnement
graphique de type bureau. Il rends l'utilisation de votre ordinateur
plus facile, agréable et eficace, et est facile à configurer.

%description -l pl.UTF-8
Programy multimedialne dla GNOME.

%package libs
Summary:	gnome-media library
Summary(pl.UTF-8):	Biblioteka gnome-media
Group:		Development/Libraries
Requires:	libgnomeui >= 2.19.1

%description libs
This package contains gnome-media library.

%description libs -l pl.UTF-8
Pakiet ten zawiera bibliotekę gnome-media.

%package cd
Summary:	CD player
Summary(pl.UTF-8):	Odtwarzacz CD
Group:		X11/Applications/Multimedia
Requires(post):	GConf2
Requires(post):	scrollkeeper
Requires:	%{name}-cddb = %{epoch}:%{version}-%{release}
Requires:	gstreamer-audio-effects-base >= 0.10.11
Requires:	gstreamer-audiosink
Requires:	gstreamer-cdparanoia >= 0.10.11
Conflicts:	gnome-media <= 0:2.8.0-5

%description cd
CD player.

%description cd -l pl.UTF-8
Odtwarzacz CD.

%package cddb
Summary:	CD database server
Summary(pl.UTF-8):	Serwer bazy danych płyt CD
Group:		X11/Applications/Multimedia
Requires(post):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-media <= 0:2.8.0-5

%description cddb
CD database server.

%description cddb -l pl.UTF-8
Serwer bazy danych płyt CD.

%package cddb-devel
Summary:	gnome-media-cddb devel file
Summary(pl.UTF-8):	Pliki nagłówkowe gnome-media-cddb
Group:		X11/Development/Libraries
Requires:	%{name}-cddb = %{epoch}:%{version}-%{release}
Conflicts:	gnome-media-devel <= 0:2.8.0-5

%description cddb-devel
gnome-media-cddb devel files.

%description cddb-devel -l pl.UTF-8
Pliki nagłówkowe gnome-media-cddb.

%package cddb-static
Summary:	gnome-media-cddb static libraries
Summary(pl.UTF-8):	Biblioteki statyczne gnome-media-cddb
Group:		X11/Development/Libraries
Requires:	%{name}-cddb-devel = %{epoch}:%{version}-%{release}
Conflicts:	gnome-media-static <= 0:2.8.0-5

%description cddb-static
gnome-media-cddb static libraries.

%description cddb-static -l pl.UTF-8
Biblioteki statyczne gnome-media-cddb.

%package devel
Summary:	gnome-media devel files
Summary(pl.UTF-8):	Pliki nagłówkowe gnome-media
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
gnome-media devel files.

%description devel -l pl.UTF-8
Pliki nagłówkowe gnome-media.

%package sound-recorder
Summary:	Sound recorder
Summary(pl.UTF-8):	Rejestrator dźwięku
Group:		X11/Applications/Multimedia
Requires(post):	GConf2
Requires(post):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gstreamer-audio-effects-base >= 0.10.11
Requires:	gstreamer-audiosink
Obsoletes:	grecord
Conflicts:	gnome-media <= 0:2.8.0-5
Suggests:	gnome-media-volume-control

%description sound-recorder
Sound recorder.

%description sound-recorder -l pl.UTF-8
Rejestrator dźwięku.

%package static
Summary:	gnome-media static libraries
Summary(pl.UTF-8):	Biblioteki statyczne gnome-media
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
gnome-media static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne gnome-media.

%package volume-control
Summary:	Volume controler
Summary(pl.UTF-8):	Regulator głośności
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gstreamer-audio-effects-base >= 0.10.11
Requires:	gstreamer-audiosink
Conflicts:	gnome-media <= 0:2.8.0-5

%description volume-control
Volume control.

%description volume-control -l pl.UTF-8
Regulator głośności.

%package vumeter
Summary:	Volume monitor
Summary(pl.UTF-8):	Monitor głośności
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gstreamer-audiosink
Conflicts:	gnome-media <= 0:2.8.0-5

%description vumeter
Volume monitor.

%description vumeter -l pl.UTF-8
Monitor głośności.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__gnome_doc_common}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -f $RPM_BUILD_ROOT%{_libdir}/libglade/2.0/*.{la,a}

%find_lang %{name}-2.0
%find_lang gnome-cd --with-gnome
%find_lang gnome-sound-recorder --with-gnome
%find_lang gnome-volume-control --with-gnome
%find_lang gstreamer-properties --with-gnome
cat gstreamer-properties.lang >> %{name}-2.0.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%scrollkeeper_update_post
%gconf_schema_install gnome-audio-profiles.schemas

%preun
%gconf_schema_uninstall gnome-audio-profiles.schemas

%postun
%update_icon_cache hicolor
%scrollkeeper_update_postun

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post cd
%scrollkeeper_update_post
%gconf_schema_install gnome-cd.schemas

%preun cd
%gconf_schema_uninstall gnome-cd.schemas

%postun cd
%scrollkeeper_update_postun

%post cddb
/sbin/ldconfig
%update_icon_cache hicolor
%gconf_schema_install CDDB-Slave2.schemas

%preun cddb
%gconf_schema_uninstall CDDB-Slave2.schemas

%postun cddb
/sbin/ldconfig
%update_icon_cache hicolor

%post sound-recorder
%update_icon_cache hicolor
%scrollkeeper_update_post
%gconf_schema_install gnome-sound-recorder.schemas

%preun sound-recorder
%gconf_schema_install gnome-sound-recorder.schemas

%postun sound-recorder
%update_icon_cache hicolor
%scrollkeeper_update_postun

%post volume-control
%update_icon_cache hicolor
%scrollkeeper_update_post

%postun volume-control
%update_icon_cache hicolor
%scrollkeeper_update_postun

%files -f %{name}-2.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gnome-audio-profiles-properties
%attr(755,root,root) %{_bindir}/gstreamer-properties
%attr(755,root,root) %{_libdir}/libglade/2.0/*.so
%{_desktopdir}/gstreamer-properties.desktop
%dir %{_datadir}/gnome-media
%dir %{_datadir}/gnome-media/pixmaps
%{_datadir}/gnome-media/glade
%{_datadir}/gstreamer-properties
%{_iconsdir}/hicolor/*/*/gstreamer-properties.*
%{_sysconfdir}/gconf/schemas/gnome-audio-profiles.schemas

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-media-profiles.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-media-profiles.so
%{_libdir}/libgnome-media-profiles.la
%{_includedir}/gnome-media
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnome-media-profiles.a

%files cd -f gnome-cd.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-cd
%{_desktopdir}/gnome-cd.desktop
%{_pixmapsdir}/gnome-cd/*
%{_sysconfdir}/gconf/schemas/gnome-cd.schemas

%files cddb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cddb-slave2-properties
%attr(755,root,root) %{_libdir}/CDDBSlave2
%attr(755,root,root) %{_libdir}/cddb-track-editor
%attr(755,root,root) %{_libdir}/libcddb-slave2.so.*.*
%{_datadir}/idl/GNOME_Media_CDDBSlave2.idl
%{_desktopdir}/cddb-slave.desktop
%{_libdir}/bonobo/servers/GNOME_Media_CDDBSlave2.server
%dir %{_pixmapsdir}/gnome-cd
%{_iconsdir}/hicolor/*/*/gnome-cd.*
%{_sysconfdir}/gconf/schemas/CDDB-Slave2.schemas

%files cddb-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcddb-slave2.so
%{_libdir}/libcddb-slave2.la
%{_includedir}/cddb-slave2

%files cddb-static
%defattr(644,root,root,755)
%{_libdir}/libcddb-slave2.a

%files sound-recorder -f gnome-sound-recorder.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-sound-recorder
%{_datadir}/gnome-sound-recorder
%{_desktopdir}/gnome-sound-recorder.desktop
%{_iconsdir}/hicolor/*/*/gnome-grecord.*
%{_sysconfdir}/gconf/schemas/gnome-sound-recorder.schemas

%files volume-control -f gnome-volume-control.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-volume-control
%{_datadir}/gnome-media/pixmaps/*
%{_desktopdir}/gnome-volume-control.desktop
%{_sysconfdir}/gconf/schemas/gnome-volume-control.schemas

%files vumeter
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vumeter
%{_desktopdir}/reclevel.desktop
%{_desktopdir}/vumeter.desktop
%{_iconsdir}/hicolor/*/*/gnome-reclevel.*
%{_iconsdir}/hicolor/*/*/gnome-vumeter.*
