Summary:	GNOME media programs
Summary(pl):	Programy multimedialne GNOME'a
Name:		gnome-media
Version:	1.0.1
Release:	1
Copyright:	LGPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
URL:		http://www.gnome.org/
Icon:		gnome-media.gif
BuildPrereq:	gtk-devel
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
#%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=/usr/X11R6

make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr/X11R6 install

strip $RPM_BUILD_ROOT/usr/X11R6/bin/*

gzip -9fn AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz
%attr(755,root,root) /usr/X11R6/bin/*
/usr/X11R6/share/gnome/apps/Multimedia/*
/usr/X11R6/share/pixmaps/tcd

%lang(da)    /usr/X11R6/share/locale/da/LC_MESSAGES/gnome-media.mo
%lang(de)    /usr/X11R6/share/locale/de/LC_MESSAGES/gnome-media.mo
%lang(es)    /usr/X11R6/share/locale/es/LC_MESSAGES/gnome-media.mo
%lang(fi)    /usr/X11R6/share/locale/fi/LC_MESSAGES/gnome-media.mo
%lang(fr)    /usr/X11R6/share/locale/fr/LC_MESSAGES/gnome-media.mo
%lang(ga)    /usr/X11R6/share/locale/ga/LC_MESSAGES/gnome-media.mo
%lang(hu)    /usr/X11R6/share/locale/hu/LC_MESSAGES/gnome-media.mo
%lang(it)    /usr/X11R6/share/locale/it/LC_MESSAGES/gnome-media.mo
%lang(ja)    /usr/X11R6/share/locale/ja/LC_MESSAGES/gnome-media.mo
%lang(ko)    /usr/X11R6/share/locale/ko/LC_MESSAGES/gnome-media.mo
%lang(nl)    /usr/X11R6/share/locale/nl/LC_MESSAGES/gnome-media.mo
%lang(no)    /usr/X11R6/share/locale/no/LC_MESSAGES/gnome-media.mo
%lang(pt)    /usr/X11R6/share/locale/pt/LC_MESSAGES/gnome-media.mo
%lang(ru_RU) /usr/X11R6/share/locale/ru*/LC_MESSAGES/gnome-media.mo

%changelog
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
