# TODO:
# separate -lib ?
# fix alsa issue
Summary:	GNOME media programs
Summary(fr):	Programmes multimédia de GNOME
Summary(pl):	Programy multimedialne GNOME'a
Name:		gnome-media
Version:	2.1.3
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.1/%{name}-%{version}.tar.bz2
Icon:		gnome-media.gif
Patch0:		%{name}-am.patch
Patch1:		%{name}-schema.patch
URL:		http://www.gnome.org/
%ifnarch sparc sparc64
BuildRequires:	alsa-lib-devel
%endif
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.1.3-3
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	gail-devel >= 1.1.4
BuildRequires:	gstreamer-devel >= 0.5.0
BuildRequires:	libgnomeui-devel >= 2.1.2
BuildRequires:	glib2-devel >= 2.0.6
BuildRequires:	esound-devel >= 0.2.29
BuildRequires:	ORBit2-devel >= 2.5.0
BuildRequires:	scrollkeeper >= 0.3.11
BuildRequires:	rpm-build >= 4.1-8.2
BuildRequires:	Xft-devel >= 2.0-6
Prereq:		scrollkeeper
Requires:	gail >= 1.1.4
Requires:	libgnomeui >= 2.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome
Obsoletes:	grecord

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
%patch0 -p1 -b .wiget
%patch1 -p1

%build
intltoolize --copy --force
%{__libtoolize}
glib-gettextize --copy --force
sed 's,-ourdir,ourdir,' xmldocs.make > xmldocs.make.new
mv xmldocs.make.new xmldocs.make
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
%{__autoconf}
##rm -f missing
%{__automake} -i
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	omf_dest_dir=%{_omf_dest_dir}/%{name}

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
%{_datadir}/applications/*
%{_datadir}/control-center-2.0/capplets/*
%{_datadir}/idl/*
%{_datadir}/gnome-sound-recorder/*
%{_datadir}/%{name}-2.0/*
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
