Summary:	GNOME media programs
Summary(pl):	Programy multimedialne GNOME'a
Name:		gnome-media
Version:	1.0.51
Release:	1
Copyright:	LGPL
Group:		X11/GNOME
Group(pl):	X11/GNOME
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
URL:		http://www.gnome.org/
Patch0:		gnome-media-applnk.patch
Icon:		gnome-media.gif
BuildRequires:	gtk+-devel
BuildRequires:	glib-devel
BuildRequires:	gettext-devel
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	gnome

%define		_prefix		/usr/X11R6
%define		_applnkdir	%{_datadir}/applnk

%description
GNOME media programs.

GNOME is the GNU Network Object Model Environment.  That's a fancy
name but really GNOME is a nice GUI desktop environment.  It makes
using your computer easy, powerful, and easy to configure.

%description -l pl
Programy multimedialne GNOME'a

%prep
%setup -q
%patch -p1

%build
gettextize --copy --force
automake
LDFLAGS="-s"; export LDFLAGS
%configure

make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

gzip -9fn AUTHORS ChangeLog NEWS

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
