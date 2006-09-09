Summary:	GNOME media programs
Summary(fr):	Programmes multimédia de GNOME
Summary(pl):	Programy multimedialne dla GNOME
Name:		gnome-media
Version:	2.16.1
Release:	2
License:	GPL v2+/LGPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-media/2.16/%{name}-%{version}.tar.bz2
# Source0-md5:	4fa1e8e8bd31e2db1cb49679170a98a8
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-configure.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	ORBit2-devel >= 1:2.14.3
%ifnarch sparc sparc64
BuildRequires:	alsa-lib-devel
%endif
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	control-center-devel >= 1:2.16.0
BuildRequires:	esound-devel >= 1:0.2.36
BuildRequires:	gail-devel >= 1.9.2
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gnome-vfs2-devel >= 2.16.0
BuildRequires:	gstreamer-devel >= 0.10.9
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.9
BuildRequires:	intltool >= 0.35
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.16.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	nautilus-cd-burner-devel >= 2.16.0
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper >= 0.3.11
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	gail >= 1.9.2
Requires:	gstreamer-GConf
Requires:	gstreamer-audiosink
Requires:	libgnomeui >= 2.16.0
Requires:	nautilus-cd-burner-libs >= 2.16.0
Obsoletes:	gnome
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gnomehelpdir	%{_datadir}/gnome/help

%description
GNOME media programs. GNOME is the GNU Network Object Model
Environment. That's a fancy name but really GNOME is a nice GUI
desktop environment. It makes using your computer easy, powerful, and
easy to configure.

%description -l fr
Programmes multimédia GNOME.

GNOME (GNU Network Object Model Environment) est un environnement
graphique de type bureau. Il rends l'utilisation de votre ordinateur
plus facile, agréable et eficace, et est facile à configurer.

%description -l pl
Programy multimedialne dla GNOME.

%package libs
Summary:	gnome-media library
Summary(pl):	Biblioteka gnome-media
Group:		Development/Libraries
Requires:	libgnomeui >= 2.16.0

%description libs
This package contains gnome-media library.

%description libs -l pl
Pakiet ten zawiera bibliotekê gnome-media.

%package cd
Summary:	CD player
Summary(pl):	Odtwarzacz CD
Group:		X11/Applications/Multimedia
Requires(post):	GConf2
Requires(post):	scrollkeeper
Requires:	%{name}-cddb = %{epoch}:%{version}-%{release}
Requires:	gstreamer-audio-effects-base >= 0.10.9
Requires:	gstreamer-audiosink
Requires:	gstreamer-cdparanoia >= 0.10.9
Conflicts:	gnome-media <= 0:2.8.0-5

%description cd
CD player.

%description cd -l pl
Odtwarzacz CD.

%package cddb
Summary:	CD database server
Summary(pl):	Serwer bazy danych p³yt CD
Group:		X11/Applications/Multimedia
Requires(post):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-media <= 0:2.8.0-5

%description cddb
CD database server.

%description cddb -l pl
Serwer bazy danych p³yt CD.

%package cddb-devel
Summary:	gnome-media-cddb devel file
Summary(pl):	Pliki nag³ówkowe gnome-media-cddb
Group:		X11/Development/Libraries
Requires:	%{name}-cddb = %{epoch}:%{version}-%{release}
Conflicts:	gnome-media-devel <= 0:2.8.0-5

%description cddb-devel
gnome-media-cddb devel files.

%description cddb-devel -l pl
Pliki nag³ówkowe gnome-media-cddb.

%package cddb-static
Summary:	gnome-media-cddb static libraries
Summary(pl):	Biblioteki statyczne gnome-media-cddb
Group:		X11/Development/Libraries
Requires:	%{name}-cddb-devel = %{epoch}:%{version}-%{release}
Conflicts:	gnome-media-static <= 0:2.8.0-5

%description cddb-static
gnome-media-cddb static libraries.

%description cddb-static -l pl
Biblioteki statyczne gnome-media-cddb.

%package devel
Summary:	gnome-media devel files
Summary(pl):	Pliki nag³ówkowe gnome-media
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
gnome-media devel files.

%description devel -l pl
Pliki nag³ówkowe gnome-media.

%package sound-recorder
Summary:	Sound recorder
Summary(pl):	Rejestrator d¼wiêku
Group:		X11/Applications/Multimedia
Requires(post):	GConf2
Requires(post):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gstreamer-audio-effects-base >= 0.10.9
Requires:	gstreamer-audiosink
Obsoletes:	grecord
Conflicts:	gnome-media <= 0:2.8.0-5

%description sound-recorder
Sound recorder.

%description sound-recorder -l pl
Rejestrator d¼wiêku.

%package static
Summary:	gnome-media static libraries
Summary(pl):	Biblioteki statyczne gnome-media
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
gnome-media static libraries.

%description static -l pl
Biblioteki statyczne gnome-media.

%package volume-control
Summary:	Volume controler
Summary(pl):	Regulator g³o¶no¶ci
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gstreamer-audio-effects-base >= 0.10.9
Requires:	gstreamer-audiosink
Conflicts:	gnome-media <= 0:2.8.0-5

%description volume-control
Volume control.

%description volume-control -l pl
Regulator g³o¶no¶ci.

%package vumeter
Summary:	Volume monitor
Summary(pl):	Monitor g³o¶no¶ci
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gstreamer-audiosink
Conflicts:	gnome-media <= 0:2.8.0-5

%description vumeter
Volume monitor.

%description vumeter -l pl
Monitor g³o¶no¶ci.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/tk

%find_lang %{name}-2.0
%find_lang gnome-cd --with-gnome
%find_lang gnome-sound-recorder --with-gnome
%find_lang gnome-volume-control --with-gnome
%find_lang grecord --with-gnome
%find_lang gstreamer-properties --with-gnome
cat gstreamer-properties.lang >> %{name}-2.0.lang
cat grecord.lang >> gnome-sound-recorder.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%gconf_schema_install gnome-audio-profiles.schemas

%preun
%gconf_schema_uninstall gnome-audio-profiles.schemas

%postun
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
%gconf_schema_install CDDB-Slave2.schemas

%preun cddb
%gconf_schema_uninstall CDDB-Slave2.schemas

%postun cddb -p /sbin/ldconfig

%post sound-recorder
%scrollkeeper_update_post
%gconf_schema_install gnome-sound-recorder.schemas
%banner %{name} -e << EOF
For full functionality, you need to install gnome-media-volume-control.
EOF

%preun sound-recorder
%gconf_schema_install gnome-sound-recorder.schemas

%postun sound-recorder
%scrollkeeper_update_postun

%post volume-control
%scrollkeeper_update_post

%postun volume-control
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
%dir %{_omf_dest_dir}/%{name}
%{_omf_dest_dir}/%{name}/gstreamer-properties-C.omf
%lang(uk) %{_omf_dest_dir}/%{name}/gstreamer-properties-uk.omf
%{_pixmapsdir}/gstreamer-properties.png
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
%{_omf_dest_dir}/%{name}/gnome-cd-C.omf
%lang(de) %{_omf_dest_dir}/%{name}/gnome-cd-de.omf
%lang(es) %{_omf_dest_dir}/%{name}/gnome-cd-es.omf
%lang(fr) %{_omf_dest_dir}/%{name}/gnome-cd-fr.omf
%lang(it) %{_omf_dest_dir}/%{name}/gnome-cd-it.omf
%lang(ja) %{_omf_dest_dir}/%{name}/gnome-cd-ja.omf
%lang(ko) %{_omf_dest_dir}/%{name}/gnome-cd-ko.omf
%lang(nl) %{_omf_dest_dir}/%{name}/gnome-cd-nl.omf
%lang(sv) %{_omf_dest_dir}/%{name}/gnome-cd-sv.omf
%lang(uk) %{_omf_dest_dir}/%{name}/gnome-cd-uk.omf
%lang(zh_CN) %{_omf_dest_dir}/%{name}/gnome-cd-zh_CN.omf
%lang(zh_TW) %{_omf_dest_dir}/%{name}/gnome-cd-zh_TW.omf
%{_pixmapsdir}/gnome-cd/*
%exclude %{_pixmapsdir}/gnome-cd/cd.png
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
%{_pixmapsdir}/gnome-cd/cd.png
%{_pixmapsdir}/gnome-cd.png
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
%{_pixmapsdir}/gnome-grecord.png
%{_sysconfdir}/gconf/schemas/gnome-sound-recorder.schemas
%{_omf_dest_dir}/%{name}/grecord-C.omf
%lang(de) %{_omf_dest_dir}/%{name}/grecord-de.omf
%lang(es) %{_omf_dest_dir}/%{name}/grecord-es.omf
%lang(fr) %{_omf_dest_dir}/%{name}/grecord-fr.omf
%lang(it) %{_omf_dest_dir}/%{name}/grecord-it.omf
%lang(ja) %{_omf_dest_dir}/%{name}/grecord-ja.omf
%lang(ko) %{_omf_dest_dir}/%{name}/grecord-ko.omf
%lang(sv) %{_omf_dest_dir}/%{name}/grecord-sv.omf
%lang(uk) %{_omf_dest_dir}/%{name}/grecord-uk.omf
%lang(zh_CN) %{_omf_dest_dir}/%{name}/grecord-zh_CN.omf
%lang(zh_TW) %{_omf_dest_dir}/%{name}/grecord-zh_TW.omf

%files volume-control -f gnome-volume-control.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-volume-control
%{_datadir}/gnome-media/pixmaps/*
%{_desktopdir}/gnome-volume-control.desktop
%{_omf_dest_dir}/%{name}/gnome-volume-control-C.omf
%lang(uk) %{_omf_dest_dir}/%{name}/gnome-volume-control-uk.omf
%{_pixmapsdir}/gnome-mixer.png
%{_sysconfdir}/gconf/schemas/gnome-volume-control.schemas

%files vumeter
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vumeter
%{_desktopdir}/reclevel.desktop
%{_desktopdir}/vumeter.desktop
%{_pixmapsdir}/gnome-reclevel.png
%{_pixmapsdir}/gnome-vumeter.png
