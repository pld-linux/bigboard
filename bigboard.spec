Summary:	Sidebar application launcher using mugshot.org
Summary(pl.UTF-8):	Pasek boczny aplikacji wywołującej używającej mugshot.org
Name:		bigboard
Version:	0.5.38
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/bigboard/0.5/%{name}-%{version}.tar.bz2
# Source0-md5:	a12ed37d5f83b99decfafcd981d6e146
Patch0:		%{name}-pyc.patch
URL:		http://mugshot.org/
BuildRequires:	GConf2-devel >= 2.22.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	desktop-data-model-devel >= 1.2.4
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnome-desktop-devel >= 2.22.0
BuildRequires:	gnome-keyring-devel >= 2.22.0
BuildRequires:	gnome-panel-devel >= 2.22.0
BuildRequires:	gnome-vfs2-devel >= 2.22.0
BuildRequires:	gtk+2-devel >= 2:2.12.9
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libsoup-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-pygtk-devel >= 2:2.12.0
Requires(preun,post):	GConf2
Requires:	mugshot
Requires:	online-desktop
Requires:	python-BeautifulSoup
Requires:	python-dbus
Requires:	python-gdata
Requires:	python-gnome-desktop
Requires:	python-gnome-desktop-applet
Requires:	python-gnome-desktop-keyring
Requires:	python-gnome-desktop-libwnck
Requires:	python-gnome-gconf
Requires:	python-gnome-ui
Requires:	python-gnome-vfs
Requires:	python-hippo-canvas
Requires:	python-pygobject
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bigboard is a sidebar and application launcher that works with
mugshot.org to provide an online experience.

%description -l pl.UTF-8
Bigboard jest aplikacją wywołującą działającą w formie bocznego paska
współpracującą z mugshot.org.

%prep
%setup -q
%patch0 -p1

%build
%{__mkdir} m4
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-pymod-checks \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/bigboard/bignative.la
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/bigboard/keybinder/_keybinder.la

# Remove another copy of GPLv2 license
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/bigboard/libgmail/COPYING

%py_postclean %{_libdir}/bigboard
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install bigboard.schemas

%preun
%gconf_schema_uninstall bigboard.schemas

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/bigboard
%attr(755,root,root) %{_libdir}/bigboard-applets
%dir %{_libdir}/bigboard
%{_libdir}/bigboard/*.py[co]
%dir %{py_sitedir}/bigboard
%attr(755,root,root) %{py_sitedir}/bigboard/bignative.so
%{py_sitedir}/bigboard/*.py[co]
%dir %{py_sitedir}/bigboard/httplib2
%{py_sitedir}/bigboard/httplib2/*.py[co]
%dir %{py_sitedir}/bigboard/keybinder
%{py_sitedir}/bigboard/keybinder/*.py[co]
%attr(755,root,root) %{py_sitedir}/bigboard/keybinder/_keybinder.so
%dir %{py_sitedir}/bigboard/libbig
%{py_sitedir}/bigboard/libbig/*.py[co]
%dir %{py_sitedir}/bigboard/libgmail
%dir %{py_sitedir}/bigboard/libgmail/ClientCookie
%{py_sitedir}/bigboard/libgmail/*.py[co]
%{py_sitedir}/bigboard/libgmail/README
%{py_sitedir}/bigboard/libgmail/ClientCookie/*.py[co]
%dir %{py_sitedir}/bigboard/stocks
%{py_sitedir}/bigboard/stocks/*.xml
%dir %{py_sitedir}/bigboard/stocks/apps
%{py_sitedir}/bigboard/stocks/apps/*.py[co]
%{py_sitedir}/bigboard/stocks/apps/*.png
%dir %{py_sitedir}/bigboard/stocks/files
%{py_sitedir}/bigboard/stocks/files/*.py[co]
%{py_sitedir}/bigboard/stocks/files/*.png
%dir %{py_sitedir}/bigboard/stocks/google_calendar
%{py_sitedir}/bigboard/stocks/google_calendar/*.py[co]
%{py_sitedir}/bigboard/stocks/google_calendar/*.png
%dir %{py_sitedir}/bigboard/stocks/mail
%{py_sitedir}/bigboard/stocks/mail/*.py[co]
%{py_sitedir}/bigboard/stocks/mail/*.png
%dir %{py_sitedir}/bigboard/stocks/mugshot_photos
%{py_sitedir}/bigboard/stocks/mugshot_photos/*.py[co]
%{py_sitedir}/bigboard/stocks/mugshot_photos/*.png
%dir %{py_sitedir}/bigboard/stocks/people
%{py_sitedir}/bigboard/stocks/people/*.py[co]
%{py_sitedir}/bigboard/stocks/people/*.png
%dir %{py_sitedir}/bigboard/stocks/search
%{py_sitedir}/bigboard/stocks/search/*.py[co]
%dir %{py_sitedir}/bigboard/stocks/self
%{py_sitedir}/bigboard/stocks/self/*.py[co]
%dir %{py_sitedir}/bigboard/stocks/workspaces
%{py_sitedir}/bigboard/stocks/workspaces/*.py[co]
%{py_sitedir}/bigboard/stocks/workspaces/*.png
%dir %{py_sitedir}/bigboard/themes
%{py_sitedir}/bigboard/themes/*.py[co]
%{py_sitedir}/bigboard/themes/*.css
%{_sysconfdir}/gconf/schemas/bigboard.schemas
%{_libdir}/bonobo/servers/GNOME_OnlineDesktop_BigBoardFactory.server
%{_datadir}/bigboard
%{_datadir}/gnome-2.0/ui/GNOME_OnlineDesktop_BigBoardButtonApplet.xml
%{_datadir}/online-prefs-sync/bigboard.synclist
