# TODO:
# separate -lib ?
# fix alsa issue
Summary:	GNOME media programs
Summary(fr):	Programmes multimédia de GNOME
Summary(pl):	Programy multimedialne dla GNOME
Name:		gnome-media
Version:	2.7.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.7/%{name}-%{version}.tar.bz2
# Source0-md5:	2bc7afd97189ee010621a2fe4360fdf8
Patch0:		%{name}-locale-names.patch
Icon:		gnome-media.gif
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.7.1
BuildRequires:	ORBit2-devel >= 1:2.10.2
%ifnarch sparc sparc64
BuildRequires:	alsa-lib-devel
%endif
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	control-center-devel >= 1:2.6.1
BuildRequires:	esound-devel >= 1:0.2.31
BuildRequires:	gail-devel >= 1.6.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-vfs2-devel >= 2.7.1
BuildRequires:	gstreamer-GConf-devel >= 0.8.2
BuildRequires:	gstreamer-devel >= 0.8.3
BuildRequires:	gstreamer-plugins-devel >= 0.8.2
BuildRequires:	intltool >= 0.25
BuildRequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	libgnomeui-devel >= 2.7.1
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	rpm-build >= 4.1-10
BuildRequires:	scrollkeeper >= 0.3.11
BuildRequires:	xft-devel >= 2.1.2
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	scrollkeeper
Requires(post):	GConf2
Requires:	gail >= 1.6.0
Requires:	libgnomeui >= 2.7.1
Requires:	gstreamer-plugins >= 0.8.2
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
Requires:	%{name} = %{version}-%{release}

%description devel
gnome-media devel files.

%description devel -l pl
Pliki nag³ówkowe gnome-media.

%package static
Summary:	gnome-media static libraries
Summary(pl):	Biblioteki statyczne gnome-media
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
gnome-media static libraries.

%description static -l pl
Biblioteki statyczne gnome-media.

%prep
%setup -q
%patch0 -p1

mv po/{no,nb}.po

%build
intltoolize --copy --force
%{__libtoolize}
glib-gettextize --copy --force
%{__aclocal} -I m4 -I %{_aclocaldir}/gnome2-macros
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

install -d $RPM_BUILD_ROOT%{_datadir}/gnome/capplets
mv $RPM_BUILD_ROOT%{_datadir}/control-center-2.0/capplets/*.desktop $RPM_BUILD_ROOT%{_datadir}/gnome/capplets
rm -f $RPM_BUILD_ROOT%{_libdir}/libglade/2.0/*.la

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
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/CDDBSlave2
%attr(755,root,root) %{_libdir}/cddb-track-editor
%{_libdir}/bonobo/servers/*
%attr(755,root,root) %{_libdir}/libglade/2.0/*.so
%{_datadir}/gnome/capplets/*
%{_datadir}/idl/*
%{_datadir}/gnome-media
%{_datadir}/gnome-sound-recorder
%{_datadir}/gstreamer-properties
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_omf_dest_dir}/*
%{_sysconfdir}/gconf/schemas/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/cddb-slave2
%{_includedir}/gnome-media
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
