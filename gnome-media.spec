# TODO:
# add -devel and -static 
# separate -lib ?
# fix alsa issue
Summary:	GNOME media programs
Summary(fr):	Programmes multimédia de GNOME
Summary(pl):	Programy multimedialne GNOME'a
Name:		gnome-media
Version:	2.0.0
Release:	0.5
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/gnome-media/%{name}-%{version}.tar.bz2
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
BuildRequires:	gtk+2-devel >= 2.0.3
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	gail-devel >= 0.16
BuildRequires:	libgnomeui-devel >= 2.0.1
BuildRequires:	glib2-devel >= 2.0.3
BuildRequires:	esound-devel >= 0.2.23
BuildRequires:	ORBit2-devel >= 2.4.0
BuildRequires:	scrollkeeper >= 0.3.6
Prereq:		scrollkeeper
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
Programmes multimédia GNOME.

GNOME (GNU Network Object Model Environment) est un environnement
graphique de type bureau. Il rends l'utilisation de votre ordinateur
plus facile, agréable et eficace, et est facile à configurer.

%description -l pl
Programy multimedialne GNOME'a.

%prep
%setup -q
%patch0 -p1 -b .wiget

%build
libtoolize --copy --force
glib-gettextize --copy --force
sed 's,-ourdir,ourdir,' xmldocs.make > xmldocs.make.new
mv xmldocs.make.new xmldocs.make
aclocal 
%{__autoconf}
rm -f missing
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
GCONF_CONFIG_SOURCE="" \
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
%{_datadir}/applications/*
%{_datadir}/control-center-2.0/capplets/*
%{_datadir}/idl/*
%{_pixmapsdir}/*
%{_libdir}/lib*.so.*.*
%{_omf_dest_dir}/*

%{_includedir}/cddb-slave2
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_libdir}/lib*.a
