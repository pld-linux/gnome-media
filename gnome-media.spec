# TODO:
# fix alsa issue
Summary:	GNOME media programs
Summary(fr):	Programmes multimédia de GNOME
Summary(pl):	Programy multimedialne dla GNOME
Name:		gnome-media
Version:	2.9.92
Release:	1
License:	GPL/LGPL
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-media/2.9/%{name}-%{version}.tar.bz2
# Source0-md5:	7578a6b234f7b9e8ef6c811a6832a7b8
Patch0:		%{name}-capplet.patch
Patch1:		%{name}-desktop.patch
Icon:		gnome-media.gif
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.9.2
BuildRequires:	ORBit2-devel >= 1:2.12.1
%ifnarch sparc sparc64
BuildRequires:	alsa-lib-devel
%endif
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	control-center-devel >= 1:2.9.4
BuildRequires:	esound-devel >= 1:0.2.31
BuildRequires:	gail-devel >= 1.8.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gnome-vfs2-devel >= 2.9.92
BuildRequires:	gstreamer-GConf-devel >= 0.8.7
BuildRequires:	gstreamer-devel >= 0.8.8
BuildRequires:	gstreamer-plugins-devel >= 0.8.7
BuildRequires:	intltool >= 0.25
BuildRequires:	libglade2-devel >= 1:2.5.0
BuildRequires:	libgnomeui-devel >= 2.9.1
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	nautilus-cd-burner-devel >= 2.9.6
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.1-10
BuildRequires:	scrollkeeper >= 0.3.11
BuildRequires:	xft-devel >= 2.1.2
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	scrollkeeper
Requires(post):	GConf2
Requires:	gail >= 1.8.0
Requires:	libgnomeui >= 2.9.1
Requires:	gstreamer-plugins >= 0.8.7
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

%package cd
Summary:	CD player
Summary(pl):	Odtwarzacz CD
Group:		X11/Applications/Multimedia
Requires(post):	GConf2
Requires(post):	scrollkeeper
Requires:	%{name}-cddb = %{epoch}:%{version}-%{release}
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
Requires(post):	/sbin/ldconfig
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
Requires:	%{name} = %{epoch}:%{version}-%{release}

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
Conflicts:	gnome-media <= 0:2.8.0-5

%description vumeter
Volume monitor.

%description vumeter -l pl
Monitor g³o¶no¶ci.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
sed -i -e 's/888/8880/' cddb-slave2/CDDB-Slave2.schemas.in

%build
intltoolize --copy --force
%{__libtoolize}
glib-gettextize --copy --force
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
rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%post cd
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun cd -p /usr/bin/scrollkeeper-update

%post cddb
/sbin/ldconfig
%gconf_schema_install

%postun cddb -p /sbin/ldconfig

%post sound-recorder
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun sound-recorder -p /usr/bin/scrollkeeper-update

%post volume-control -p /usr/bin/scrollkeeper-update

%postun volume-control -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gnome-audio-profiles-properties
%attr(755,root,root) %{_bindir}/gstreamer-properties
%attr(755,root,root) %{_libdir}/libgnome-media-profiles.so.*.*
%attr(755,root,root) %{_libdir}/libglade/2.0/*.so
%dir %{_datadir}/gnome-media
%dir %{_datadir}/gnome-media/pixmaps
%{_datadir}/gnome-media/glade
%{_datadir}/gstreamer-properties
%{_desktopdir}/gstreamer-properties.desktop
%{_omf_dest_dir}/%{name}/gstreamer-properties-C.omf
%{_pixmapsdir}/gstreamer-properties.png
%{_sysconfdir}/gconf/schemas/gnome-audio-profiles.schemas
%dir %{_gnomehelpdir}/gstreamer-properties
%{_gnomehelpdir}/gstreamer-properties/C

%files cd
%attr(755,root,root) %{_bindir}/gnome-cd
%{_desktopdir}/gnome-cd.desktop
%{_omf_dest_dir}/%{name}/gnome-cd-C.omf
%lang(de) %{_omf_dest_dir}/%{name}/gnome-cd-de.omf
%lang(es) %{_omf_dest_dir}/%{name}/gnome-cd-es.omf
%lang(fr) %{_omf_dest_dir}/%{name}/gnome-cd-fr.omf
%lang(it) %{_omf_dest_dir}/%{name}/gnome-cd-it.omf
%lang(ja) %{_omf_dest_dir}/%{name}/gnome-cd-ja.omf
%lang(ko) %{_omf_dest_dir}/%{name}/gnome-cd-ko.omf
%lang(sv) %{_omf_dest_dir}/%{name}/gnome-cd-sv.omf
%lang(zh_CN) %{_omf_dest_dir}/%{name}/gnome-cd-zh_CN.omf
%lang(zh_TW) %{_omf_dest_dir}/%{name}/gnome-cd-zh_TW.omf
%{_pixmapsdir}/gnome-cd/*
%exclude %{_pixmapsdir}/gnome-cd/cd.png
%{_sysconfdir}/gconf/schemas/gnome-cd.schemas
%dir %{_gnomehelpdir}/gnome-cd
%{_gnomehelpdir}/gnome-cd/C
%lang(de) %{_gnomehelpdir}/gnome-cd/de
%lang(es) %{_gnomehelpdir}/gnome-cd/es
%lang(fr) %{_gnomehelpdir}/gnome-cd/fr
%lang(it) %{_gnomehelpdir}/gnome-cd/it
%lang(ja) %{_gnomehelpdir}/gnome-cd/ja
%lang(ko) %{_gnomehelpdir}/gnome-cd/ko
%lang(sv) %{_gnomehelpdir}/gnome-cd/sv
%lang(zh_CN) %{_gnomehelpdir}/gnome-cd/zh_CN
%lang(zh_TW) %{_gnomehelpdir}/gnome-cd/zh_TW

%files cddb
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

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-media-profiles.so
%{_libdir}/libgnome-media-profiles.la
%{_includedir}/gnome-media
%{_pkgconfigdir}/*

%files sound-recorder
%attr(755,root,root) %{_bindir}/gnome-sound-recorder
%{_datadir}/gnome-sound-recorder
%{_desktopdir}/gnome-sound-recorder.desktop
%{_omf_dest_dir}/%{name}/grecord-C.omf
%lang(de) %{_omf_dest_dir}/%{name}/grecord-de.omf
%lang(es) %{_omf_dest_dir}/%{name}/grecord-es.omf
%lang(fr) %{_omf_dest_dir}/%{name}/grecord-fr.omf
%lang(it) %{_omf_dest_dir}/%{name}/grecord-it.omf
%lang(ja) %{_omf_dest_dir}/%{name}/grecord-ja.omf
%lang(ko) %{_omf_dest_dir}/%{name}/grecord-ko.omf
%lang(sv) %{_omf_dest_dir}/%{name}/grecord-sv.omf
%lang(zh_CN) %{_omf_dest_dir}/%{name}/grecord-zh_CN.omf
%lang(zh_TW) %{_omf_dest_dir}/%{name}/grecord-zh_TW.omf
%{_pixmapsdir}/%{name}
%{_pixmapsdir}/gnome-grecord.png
%{_sysconfdir}/gconf/schemas/gnome-sound-recorder.schemas
%dir %{_gnomehelpdir}/gnome-sound-recorder
%{_gnomehelpdir}/gnome-sound-recorder/C
%dir %{_gnomehelpdir}/grecord
%lang(de) %{_gnomehelpdir}/grecord/de
%lang(es) %{_gnomehelpdir}/grecord/es
%lang(fr) %{_gnomehelpdir}/grecord/fr
%lang(it) %{_gnomehelpdir}/grecord/it
%lang(ja) %{_gnomehelpdir}/grecord/ja
%lang(ko) %{_gnomehelpdir}/grecord/ko
%lang(sv) %{_gnomehelpdir}/grecord/sv
%lang(zh_CN) %{_gnomehelpdir}/grecord/zh_CN
%lang(zh_TW) %{_gnomehelpdir}/grecord/zh_TW

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnome-media-profiles.a

%files volume-control
%attr(755,root,root) %{_bindir}/gnome-volume-control
%{_datadir}/gnome-media/pixmaps/*
%{_desktopdir}/gnome-volume-control.desktop
%{_omf_dest_dir}/%{name}/gnome-volume-control-C.omf
%{_pixmapsdir}/%{name}
%{_pixmapsdir}/gnome-mixer.png
%dir %{_gnomehelpdir}/gnome-volume-control
%{_gnomehelpdir}/gnome-volume-control/C

%files vumeter
%attr(755,root,root) %{_bindir}/vumeter
%{_desktopdir}/reclevel.desktop
%{_desktopdir}/vumeter.desktop
%{_pixmapsdir}/gnome-reclevel.png
%{_pixmapsdir}/gnome-vumeter.png
