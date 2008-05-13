Summary:	GNOME media programs
Summary(fr.UTF-8):	Programmes multimédia de GNOME
Summary(pl.UTF-8):	Programy multimedialne dla GNOME
Name:		gnome-media
Version:	2.23.1.1
Release:	1
License:	GPL v2+/LGPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-media/2.23/%{name}-%{version}.tar.bz2
# Source0-md5:	368544fe513459dac61564c191f43393
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.22.0
BuildRequires:	ORBit2-devel >= 1:2.14.9
%ifnarch sparc sparc64
BuildRequires:	alsa-lib-devel
%endif
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gnome-control-center-devel >= 1:2.22.0
BuildRequires:	esound-devel >= 1:0.2.37
BuildRequires:	gail-devel >= 1.20.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnome-vfs2-devel >= 2.22.0
BuildRequires:	gstreamer-devel >= 0.10.11
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.11
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libbonobo-devel >= 2.22.0
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomeui-devel >= 2.19.1
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.30
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper >= 0.3.11
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	gail >= 1.20.0
Requires:	gstreamer-GConf
Requires:	gstreamer-audiosink
Requires:	libgnomeui >= 2.19.1
Obsoletes:	gnome
Obsoletes:	gnome-media-cd <= 2.23.1.1-1
Obsoletes:	gnome-media-cddb <= 2.23.1.1-1
Obsoletes:	gnome-media-cddb-devel <= 2.23.1.1-1
Obsoletes:	gnome-media-cddb-static <= 2.23.1.1-1
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
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

[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
	mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}
%find_lang %{name}-2.0
%find_lang gnome-sound-recorder --with-gnome --with-omf
%find_lang gnome-volume-control --with-gnome --with-omf
%find_lang gstreamer-properties --with-gnome --with-omf
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
%attr(755,root,root) %ghost %{_libdir}/libgnome-media-profiles.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-media-profiles.so
%{_libdir}/libgnome-media-profiles.la
%{_includedir}/gnome-media
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnome-media-profiles.a

%files sound-recorder -f gnome-sound-recorder.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-sound-recorder
%{_datadir}/gnome-sound-recorder
%{_desktopdir}/gnome-sound-recorder.desktop
%{_iconsdir}/hicolor/*/*/gnome-sound-recorder.*
%{_sysconfdir}/gconf/schemas/gnome-sound-recorder.schemas

%files volume-control -f gnome-volume-control.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-volume-control
%{_datadir}/gnome-media/gnome-volume-control-ui.xml
%{_datadir}/gnome-media/pixmaps/*
%{_desktopdir}/gnome-volume-control.desktop
%{_iconsdir}/hicolor/*/devices/gvc-*.png
%{_iconsdir}/hicolor/*/status/audio-input-microphone-muted.png
%{_sysconfdir}/gconf/schemas/gnome-volume-control.schemas

#%files vumeter
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/vumeter
#%{_desktopdir}/reclevel.desktop
#%{_desktopdir}/vumeter.desktop
#%{_iconsdir}/hicolor/*/*/gnome-reclevel.*
#%{_iconsdir}/hicolor/*/*/gnome-vumeter.*
