Summary:	GNOME media programs
Summary(fr):	Programmes multimédia de GNOME
Summary(pl):	Programy multimedialne GNOME'a
Name:		gnome-media
Version:	1.2.3
Release:	4
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-media/1.2/%{name}-%{version}.tar.bz2
# Source0-md5:	2728b3cc7d8028d2f7beab3ad4fee027
Patch0:		%{name}-am_fixes.patch
Patch1:		%{name}-am_conditional.patch
Patch2:		%{name}-omf.patch
Patch3:		%{name}-desktop.patch
Patch4:		%{name}-zh.patch
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
mv -f po/zh_CN.GB2312.po po/zh_CN.po
mv -f po/zh_TW.Big5.po po/zh_TW.po
%patch4 -p1

%build
rm -f missing
xml-i18n-toolize --copy --force
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I macros
%{__autoconf}
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

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%{_sysconfdir}/CORBA/servers/gtcd.goad
%attr(755,root,root) %{_bindir}/*
%{_omf_dest_dir}/%{name}
%{_applnkdir}/Multimedia/*
%{_datadir}/gnome/cddb-submit-methods
%{_datadir}/mime-info/*
%{_datadir}/idl/gtcd.idl
%{_pixmapsdir}/*
