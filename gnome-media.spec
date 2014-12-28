Summary:	GNOME media programs
Summary(fr.UTF-8):	Programmes multimédia de GNOME
Summary(pl.UTF-8):	Programy multimedialne dla GNOME
Name:		gnome-media
Version:	3.4.0
Release:	2
License:	GPL v2+/LGPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-media/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	90e9350299dfa90e6e59552a47ce3284
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gstreamer-devel >= 0.10.23
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.23
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libcanberra-gtk3-devel >= 0.13
BuildRequires:	libgnome-media-profiles-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.30
BuildRequires:	libxml2-progs
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9.16
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper >= 0.3.11
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires:	gstreamer-GConf
Requires:	gstreamer-audiosink
Obsoletes:	gnome
Obsoletes:	gnome-media-cd
Obsoletes:	gnome-media-cddb
Obsoletes:	gnome-media-cddb-devel
Obsoletes:	gnome-media-cddb-static
Obsoletes:	gnome-media-devel
Obsoletes:	gnome-media-libs
Obsoletes:	gnome-media-static
Obsoletes:	gnome-media-volume-control
Obsoletes:	gnome-media-vumeter
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME media programs.

%description -l fr.UTF-8
Programmes multimédia GNOME.

%description -l pl.UTF-8
Programy multimedialne dla GNOME.

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
Obsoletes:	grecord
Conflicts:	gnome-media <= 0:2.8.0-5

%description sound-recorder
Sound recorder.

%description sound-recorder -l pl.UTF-8
Rejestrator dźwięku.

%prep
%setup -q

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

%find_lang %{name}-2.0
%find_lang gnome-sound-recorder --with-gnome --with-omf
%find_lang gstreamer-properties --with-gnome --with-omf
cat gstreamer-properties.lang >> %{name}-2.0.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%scrollkeeper_update_post

%postun
%update_icon_cache hicolor
%scrollkeeper_update_postun

%post sound-recorder
%update_icon_cache hicolor
%scrollkeeper_update_post
%gconf_schema_install gnome-sound-recorder.schemas

%preun sound-recorder
%gconf_schema_install gnome-sound-recorder.schemas

%postun sound-recorder
%update_icon_cache hicolor
%scrollkeeper_update_postun

%files -f %{name}-2.0.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/gstreamer-properties
%{_desktopdir}/gstreamer-properties.desktop
%{_datadir}/gstreamer-properties
%{_iconsdir}/hicolor/*/*/gstreamer-properties.*
%dir %{_datadir}/gnome-media
%dir %{_datadir}/gnome-media/sounds
%{_datadir}/gnome-media/sounds/gnome-sounds-default.xml
%dir %{_datadir}/sounds/gnome
%dir %{_datadir}/sounds/gnome/default
%dir %{_datadir}/sounds/gnome/default/alerts
%{_datadir}/sounds/gnome/default/alerts/*.ogg

%files sound-recorder -f gnome-sound-recorder.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-sound-recorder
%{_datadir}/gnome-sound-recorder
%{_desktopdir}/gnome-sound-recorder.desktop
%{_iconsdir}/hicolor/*/*/gnome-sound-recorder.*
%{_sysconfdir}/gconf/schemas/gnome-sound-recorder.schemas
