Summary:	GNOME media programs
Summary(fr):	Programmes multimédia de GNOME
Summary(pl):	Programy multimedialne GNOME'a
Name:		gnome-media
Version:	1.2.0
Release:	6
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/gnome-media/%{name}-%{version}.tar.gz
URL:		http://www.gnome.org/
Patch0:		%{name}-sparccd.patch
Patch1:		%{name}-keepclosed.patch
Patch2:		%{name}-nogerror.patch
Icon:		gnome-media.gif
BuildRequires:	gtk+-devel
BuildRequires:	gettext-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	gnome-libs-devel
BuildRequires:	ORBit-devel
BuildRequires:	libghttp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome
Obsoletes:	grecord

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME

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
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
automake
gettextize --copy --force
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Audiodir=%{_applnkdir}/Multimedia

mv -f $RPM_BUILD_ROOT{%{_applnkdir}/Multimedia/*,%{_applnkdir}/Multimedia}
rm -rf $RPM_BUILD_ROOT%{_applnkdir}

gzip -9nf AUTHORS ChangeLog NEWS

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS}.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Multimedia/*
%{_datadir}/gnome/*
%{_datadir}/pixmaps/*
