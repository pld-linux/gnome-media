Summary:	GNOME media programs
Summary(fr):	Programmes multimédia de GNOME
Summary(pl):	Programy multimedialne GNOME'a
Name:		gnome-media
Version:	1.2.2
Release:	5
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/gnome-media/%{name}-%{version}.tar.gz
Patch0:		%{name}-keepclosed.patch
Patch1:		%{name}-nogerror.patch
Patch2:		%{name}-corba.patch
Patch3:		%{name}-alsa.patch
Patch4:		%{name}-use_AM_GNU_GETTEXT.patch
Patch5:		%{name}-am_fixes.patch
Patch6:		%{name}-am_conditional.patch
Icon:		gnome-media.gif
URL:		http://www.gnome.org/
%ifnarch sparc sparc64
BuildRequires:	alsa-lib-devel
%endif
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	gnome-http-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	ORBit-devel
BuildRequires:	libghttp-devel
BuildRequires:	scrollkeeper
Prereq:		scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome
Obsoletes:	grecord

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
libtoolize --copy --force
gettextize --copy --force
aclocal -I macros
%{__autoconf}
rm -f missing
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Audiodir=%{_applnkdir}/Multimedia \
	Applicationsdir=%{_applnkdir}/Multimedia \
	omf_dest_dir=%{_omf_dest_dir}/%{name}

gzip -9nf AUTHORS ChangeLog NEWS

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_omf_dest_dir}/%{name}
%{_applnkdir}/Multimedia/*
%{_datadir}/gnome/cddb-submit-methods
%{_datadir}/mime-info/*
%{_pixmapsdir}/*
