Summary:     GNOME media programs
Summary(pl): Programy multimedialne GNOME'a
Name:        gnome-media
Version:     0.27
Release:     2
Copyright:   LGPL
Group:       X11/Libraries
Source:      ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
URL:         http://www.gnome.org/
Requires:    gsl, esound
BuildRoot:   /tmp/%{name}-%{version}-root
Obsoletes:   gnome

%description
GNOME media programs.

GNOME is the GNU Network Object Model Environment.  That's a fancy
name but really GNOME is a nice GUI desktop environment.  It makes
using your computer easy, powerful, and easy to configure.

%description -l pl
Programy multimedialne GNOME'a

%prep
%setup -q

%build
# Needed for snapshot releases.
if [ ! -f configure ]; then
  CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh --prefix=/usr
else
  CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
fi

make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr install

strip $RPM_BUILD_ROOT/usr/bin/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755, root, root) /usr/bin/*
/usr/share/apps/Audio/*
/usr/share/pixmaps/tcd
%lang(de) /usr/share/locale/de/LC_MESSAGES/gnome-media.mo
%lang(es) /usr/share/locale/es/LC_MESSAGES/gnome-media.mo
%lang(fr) /usr/share/locale/fr/LC_MESSAGES/gnome-media.mo
%lang(ga) /usr/share/locale/ga/LC_MESSAGES/gnome-media.mo
%lang(it) /usr/share/locale/it/LC_MESSAGES/gnome-media.mo
%lang(ko) /usr/share/locale/ko/LC_MESSAGES/gnome-media.mo
%lang(no) /usr/share/locale/no/LC_MESSAGES/gnome-media.mo
%lang(pt) /usr/share/locale/pt/LC_MESSAGES/gnome-media.mo

%changelog
* Sun Sep  6 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.27-2]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added striping binaries,
- removed COPYING from %doc (copyright statment ins in Copyright field),
- added pl translation (Wojtek ¦lusarczyk <wojtek@shadow.eu.org>),
- added full %attr description in %files,
- added %lang macros for /usr/share/locale/*/LC_MESSAGES/gnome-media.mo
  files.

* Mon Mar 16 1998 Marc Ewing <marc@redhat.com>
- Integrate into gnome-media CVS source tree
