# TODO:
# separate -lib ?
# fix alsa issue
Summary:	GNOME media programs
Summary(fr):	Programmes multimédia de GNOME
Summary(pl):	Programy multimedialne dla GNOME
Name:		gnome-media
Version:	2.3.8
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.3/%{name}-%{version}.tar.bz2
# Source0-md5:	f5d937ce82f0a16cdf0a093bb6663baf
Icon:		gnome-media.gif
URL:		http://www.gnome.org/
BuildRequires:	ORBit2-devel >= 2.7.5-1
%ifnarch sparc sparc64
BuildRequires:	alsa-lib-devel
%endif
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	control-center-devel >= 2.3.4-2
BuildRequires:	gail-devel >= 1.2.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel >= 2.3.4-2
BuildRequires:	gstreamer-devel >= 0.6.0
BuildRequires:	gstreamer-GConf-devel >= 0.6.0
BuildRequires:	gstreamer-plugins-devel >= 0.6.0
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	rpm-build >= 4.1-10
BuildRequires:	scrollkeeper >= 0.3.11
BuildRequires:	xft-devel >= 2.1.2
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	scrollkeeper
Requires(post):	GConf2
Requires:	gail >= 1.2.0
Requires:	libgnomeui >= 2.3.3.1-2
Obsoletes:	gnome
Obsoletes:	grecord
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%package devel
Summary:	gnome-media devel files
Summary(pl):	Pliki nag³ówkowe gnome-media
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
gnome-media devel files.

%description devel -l pl
Pliki nag³ówkowe gnome-media.

%package static
Summary:	gnome-media static libraries
Summary(pl):	Biblioteki statyczne gnome-media
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
gnome-media static libraries.

%description static -l pl
Biblioteki statyczne gnome-media.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
    DESTDIR=$RPM_BUILD_ROOT \
    GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
scrollkeeper-update
%gconf_schema_install

%postun
/sbin/ldconfig
scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_sysconfdir}/gconf/schemas/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/CDDBSlave2
%attr(755,root,root) %{_libdir}/cddb-track-editor
%{_libdir}/bonobo/servers/*
%{_datadir}/control-center-2.0/capplets/*
%{_datadir}/idl/*
%{_datadir}/gnome-sound-recorder
%{_datadir}/%{name}-2.0
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_libdir}/lib*.so.*.*
%{_omf_dest_dir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/cddb-slave2
%{_libdir}/lib*.la
%{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
