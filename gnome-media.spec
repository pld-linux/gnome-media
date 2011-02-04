Summary:	GNOME media programs
Summary(fr.UTF-8):	Programmes multimédia de GNOME
Summary(pl.UTF-8):	Programy multimedialne dla GNOME
Name:		gnome-media
Version:	2.32.0
Release:	2
License:	GPL v2+/LGPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-media/2.32/%{name}-%{version}.tar.bz2
# Source0-md5:	06fc8c67add34c98bc484e0dbc404d41
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gstreamer-devel >= 0.10.23
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.23
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libcanberra-gtk-devel >= 0.13
BuildRequires:	libgladeui-devel
BuildRequires:	libtool
BuildRequires:	libunique-devel
BuildRequires:	libxml2-devel >= 1:2.6.30
BuildRequires:	libxml2-progs
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9.16
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper >= 0.3.11
BuildRequires:	sed >= 4.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	gstreamer-GConf
Requires:	gstreamer-audiosink
Obsoletes:	gnome
Obsoletes:	gnome-media-cd
Obsoletes:	gnome-media-cddb
Obsoletes:	gnome-media-cddb-devel
Obsoletes:	gnome-media-cddb-static
Obsoletes:	gnome-media-vumeter
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Group:		X11/Libraries

%description libs
This package contains gnome-media library.

%description libs -l pl.UTF-8
Pakiet ten zawiera bibliotekę gnome-media.

%package devel
Summary:	gnome-media devel files
Summary(pl.UTF-8):	Pliki nagłówkowe gnome-media
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	GConf2-devel >= 2.24.0
Requires:	gtk+2-devel >= 2:2.16.0

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
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer-audio-effects-base >= 0.10.11
Requires:	gstreamer-audiosink
Suggests:	gnome-media-volume-control
Obsoletes:	grecord
Conflicts:	gnome-media <= 0:2.8.0-5

%description sound-recorder
Sound recorder.

%description sound-recorder -l pl.UTF-8
Rejestrator dźwięku.

%package static
Summary:	gnome-media static libraries
Summary(pl.UTF-8):	Biblioteki statyczne gnome-media
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
gnome-media static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne gnome-media.

%package volume-control
Summary:	Volume controler
Summary(pl.UTF-8):	Regulator głośności
Group:		X11/Applications/Multimedia
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer-pulseaudio
Requires:	pulseaudio >= 0.9.20-2
Requires:	pulseaudio-alsa
Requires:	pulseaudio-gconf
Suggests:	alsa-plugins-pulse
Conflicts:	gnome-media <= 0:2.8.0-5

%description volume-control
Volume control.

%description volume-control -l pl.UTF-8
Regulator głośności.

%package -n glade3-gnome-media
Summary:	gnome-media support for Glade 3
Summary(pl.UTF-8):	Wsparcie dla gnome-media w Glade 3
Group:		Development/Building
Requires:	glade3

%description -n glade3-gnome-media
gnome-media support for Glade 3.

%description -n glade3-gnome-media -l pl.UTF-8
Wsparcie dla gnome-media w Glade 3.

%prep
%setup -q

%{__sed} -i -e 's/en@shaw//' po/LINGUAS
rm -f po/en@shaw.po

%build
%{__gnome_doc_common}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -f $RPM_BUILD_ROOT%{_libdir}/glade3/modules/*.{a,la}

%find_lang %{name}-2.0
%find_lang gnome-audio-profiles --with-gnome --with-omf
%find_lang gnome-sound-recorder --with-gnome --with-omf
%find_lang gstreamer-properties --with-gnome --with-omf
cat gstreamer-properties.lang >> %{name}-2.0.lang
cat gnome-audio-profiles.lang >> %{name}-2.0.lang

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

%postun volume-control
%update_icon_cache hicolor

%files -f %{name}-2.0.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/gnome-audio-profiles-properties
%attr(755,root,root) %{_bindir}/gstreamer-properties
%{_desktopdir}/gstreamer-properties.desktop
%dir %{_datadir}/gnome-media
%{_datadir}/gnome-media/*.ui
%{_datadir}/gstreamer-properties
%{_iconsdir}/hicolor/*/*/gstreamer-properties.*
%{_sysconfdir}/gconf/schemas/gnome-audio-profiles.schemas

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-media-profiles.so.*.*.*
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

%files volume-control
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-volume-control
%attr(755,root,root) %{_bindir}/gnome-volume-control-applet
%{_datadir}/gnome-media/icons
%dir %{_datadir}/gnome-media/sounds
%{_datadir}/gnome-media/sounds/gnome-sounds-default.xml
%{_desktopdir}/gnome-volume-control.desktop
%dir %{_datadir}/sounds/gnome
%dir %{_datadir}/sounds/gnome/default
%dir %{_datadir}/sounds/gnome/default/alerts
%{_datadir}/sounds/gnome/default/alerts/*.ogg
%{_sysconfdir}/xdg/autostart/gnome-volume-control-applet.desktop
%{_iconsdir}/hicolor/*/*/multimedia-volume-control.*

%files -n glade3-gnome-media
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/glade3/modules/libgnome-media-profiles.so
%{_datadir}/glade3/catalogs/gnome-media-profiles.xml
