Summary:	Sidebar application launcher using mugshot.org
Name:		bigboard
Version:	0.5.33
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/bigboard/0.5/%{name}-%{version}.tar.bz2
# Source0-md5:	0b45627aac3cc220609050c091464092
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

%prep
%setup -q
%patch0 -p1

%build
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

rm -f $RPM_BUILD_ROOT%{py_sitedir}/bigboard/bignative.la
rm -f $RPM_BUILD_ROOT%{py_sitedir}/bigboard/keybinder/_keybinder.la

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
%attr(755,root,root) %{_bindir}/bigboard
%attr(755,root,root) %{_libdir}/bigboard-applets
%dir %{_libdir}/bigboard
%{_libdir}/bigboard/*.py[co]
%dir %{py_sitedir}/bigboard
%attr(755,root,root) %{py_sitedir}/bigboard/bignative.so
%{py_sitedir}/bigboard/*.py[co]
%dir %{py_sitedir}/bigboard/bigbar
%{py_sitedir}/bigboard/bigbar/*.py[co]
%dir %{py_sitedir}/bigboard/httplib2
%{py_sitedir}/bigboard/httplib2/*.py[co]
%dir %{py_sitedir}/bigboard/keybinder
%{py_sitedir}/bigboard/keybinder/*.py[co]
%attr(755,root,root) %{py_sitedir}/bigboard/keybinder/_keybinder.so
%dir %{py_sitedir}/bigboard/libbig
%{py_sitedir}/bigboard/libbig/*.py[co]
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