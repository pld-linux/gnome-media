Summary:	GNOME media programs
Summary(fr):	Programmes multim�dia de GNOME
Summary(pl):	Programy multimedialne GNOME'a
Name:		gnome-media
Version:	1.2.0
Release:	9
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
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
Programmes multim�dia GNOME.

GNOME (GNU Network Object Model Environment) est un environnement
graphique de type bureau. Il rends l'utilisation de votre ordinateur
plus facile, agr�able et eficace, et est facile � configurer.

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
	Audiodir=%{_applnkdir}/Multimedia \
	Applicationsdir=%{_applnkdir}/Multimedia

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
