# TODO:
# separate -lib ?
# fix alsa issue
Summary:	GNOME media programs
Summary(fr):	Programmes multim�dia de GNOME
Summary(pl):	Programy multimedialne GNOME'a
Name:		gnome-media
Version:	2.1.0
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.1/%{name}-%{version}.tar.bz2
Icon:		gnome-media.gif
Patch0:		%{name}-am.patch
URL:		http://www.gnome.org/
%ifnarch sparc sparc64
BuildRequires:	alsa-lib-devel
%endif
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.0.6
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	gail-devel >= 0.17
BuildRequires:	libgnomeui-devel >= 2.0.5
BuildRequires:	glib2-devel >= 2.0.6
BuildRequires:	esound-devel >= 0.2.29
BuildRequires:	ORBit2-devel >= 2.4.3
BuildRequires:	scrollkeeper >= 0.3.11
Prereq:		scrollkeeper
Requires:	gail >= 0.17
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome
Obsoletes:	grecord

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME2
%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)

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
%patch0 -p1 -b .wiget

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
GCONF_CONFIG_SOURCE="`%{_bindir}/gconftool-2 --get-default-source`" \
%{_bindir}/gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/*.schemas > /dev/null 

%postun
/sbin/ldconfig
scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_sysconfdir}/gconf/schemas/*
%attr(755,root,root) %{_bindir}/*
%{_libdir}/bonobo/servers/*
%attr(755,root,root) %{_libdir}/CDDBSlave2
%attr(755,root,root) %{_libdir}/cddb-track-editor
%{_datadir}/applications/*
%{_datadir}/control-center-2.0/capplets/*
%{_datadir}/idl/*
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
