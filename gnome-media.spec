# TODO:
# separate -lib ?
# fix alsa issue
Summary:	GNOME media programs
Summary(fr):	Programmes multim�dia de GNOME
Summary(pl):	Programy multimedialne GNOME'a
Name:		gnome-media
Version:	2.3.4
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.3/%{name}-%{version}.tar.bz2
# Source0-md5:	0b4693a9b1bf691cd84680f442b7a53c
Icon:		gnome-media.gif
URL:		http://www.gnome.org/
BuildRequires:	ORBit2-devel >= 2.7.0
%ifnarch sparc sparc64
BuildRequires:	alsa-lib-devel
%endif
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	control-center-devel >= 2.2.0
BuildRequires:	gail-devel >= 1.2.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel >= 2.3.3
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
Requires:	libgnomeui >= 2.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome
Obsoletes:	grecord

%description
GNOME media programs. GNOME is the GNU Network Object Model
Environment. That's a fancy name but really GNOME is a nice GUI
desktop environment. It makes using your computer easy, powerful, and
easy to configure.

%description -l fr
Programmes multim�dia GNOME.

GNOME (GNU Network Object Model Environment) est un environnement
graphique de type bureau. Il rends l'utilisation de votre ordinateur
plus facile, agr�able et eficace, et est facile � configurer.

%description -l pl
Programy multimedialne GNOME'a.

%package devel
Summary:	gnome-media devel files
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description devel
gnome-media devel files.

%package static
Summary:	gnome-media static libraries
Group:		X11/Applications/Multimedia
Requires:	%{name}-devel = %{version}

%description static
gnome-media static libraries.

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
%{_datadir}/gnome-sound-recorder/*
%{_datadir}/%{name}-2.0/*
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
