Summary:	GNOME media programs
Summary(pl):	Programy multimedialne GNOME'a
Name:		gnome-media
Version:	1.0.9
Release:	1
Copyright:	LGPL
Group:		X11/GNOME
Group(pl):	X11/GNOME
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
URL:		http://www.gnome.org/
Icon:		gnome-media.gif
BuildPrereq:	gtk+-devel
BuildPrereq:	glib-devel
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	gnome

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
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=/usr/X11R6

make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr/X11R6 install

strip $RPM_BUILD_ROOT/usr/X11R6/bin/*

gzip -9fn AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz
%attr(755,root,root) /usr/X11R6/bin/*
/usr/X11R6/share/gnome/apps/Multimedia/*
/usr/X11R6/share/pixmaps/tcd


%changelog
* Mon Jun 07 1999 Jan R瘯orajski <baggins@pld.org.pl>
  [1.0.1-2]
- fixed buildprereq
- added find_lang macro

* Thu Apr  1 1999 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [1.0.1-1]
- more locales (da, fi, hu, ja, nl, pt, ru_RU).

* Fri Sep 25 1998 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [0.30-1]
- added in Requires "gtk+ >= 1.1.2, glib >= 1.1.3"
- added ru_RU locale.

* Fri Sep 18 1998 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [0.27-3]
- added package Icon,
- removed COPYING from %doc (copyright statment is in Copyright field),
- removed gsl from Requires,
- changed prefix to /usr/X11R6.

* Sun Sep  6 1998 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [0.27-2]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added stripping binaries,
- removed COPYING from %doc (copyright statment ins in Copyright field),
- added pl translation (Wojtek 奸usarczyk <wojtek@shadow.eu.org>),
- added full %attr description in %files,
- added %lang macros for %{_datadir}/locale/*/LC_MESSAGES/gnome-media.mo
  files.

* Mon Mar 16 1998 Marc Ewing <marc@redhat.com>
- Integrate into gnome-media CVS source tree
