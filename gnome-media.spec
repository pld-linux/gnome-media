Summary:	GNOME media programs
Summary(pl):	Programy multimedialne GNOME'a
Name:		gnome-media
Version:	1.2.0
Release:	1
License:	GPL
Group:		X11/GNOME
Group(pl):	X11/GNOME
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/%{name}-%{version}.tar.gz
Source1:	gtcd.idl
Source2:	gtcd.goad
URL:		http://www.gnome.org/
Patch0:		gnome-media-applnk.patch
Patch1:		gnome-media-sparccd.patch
Patch2:		gnome-media-keepclosed.patch
Patch3:		gnome-media-gtcdcorba.patch
Patch4:		gnome-media-mocorba.patch
Patch5:		gnome-media-fixedcorba.patch
Patch6:		gnome-media-nogerror.patch
Icon:		gnome-media.gif
BuildRequires:	gtk+-devel
BuildRequires:	gettext-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	gnome-libs-devel
BuildRequires:	ORBit-devel
BuildRequires:	libghttp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME

%description
GNOME media programs. GNOME is the GNU Network Object Model
Environment. That's a fancy name but really GNOME is a nice GUI
desktop environment. It makes using your computer easy, powerful, and
easy to configure.

%description -l pl
Programy multimedialne GNOME'a

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
# %patch3 -p1
# %patch4 -p1
# %patch5 -p1
%patch6 -p1

# aclocal -I macros
# automake --include-deps tcd/Makefile
# autoconf

install %{SOURCE1} %{SOURCE2} tcd

%build
gettextize --copy --force
automake
LDFLAGS="-s"; export LDFLAGS
%configure

make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

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
