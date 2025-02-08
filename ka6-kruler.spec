#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.12.2
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kruler
Summary:	kruler
Name:		ka6-%{kaname}
Version:	24.12.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	0f6de264d9c08d64796418f0b230cb93
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= 5.11.1
BuildRequires:	Qt6Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-knotifications-devel >= %{kframever}
BuildRequires:	kf6-kwindowsystem-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KRuler displays on screen a ruler measuring pixels. Position the 0 to
your starting point (simple drag it), and read off the precise pixel
count to your cursor. To change the length of the ruler just drag the
sides.

%description -l pl.UTF-8
KRuler wyświetla na ekranie linijkę mierzącą liczbę pikseli. Ustaw 0
w punkcie startowym (po prostu przeciągnij ją) i odczytaj precyzyjną
liczbę pikseli do kursora. Aby zmienic długość linijki, przeciągnij
jej boki.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kruler
%{_desktopdir}/org.kde.kruler.desktop
%{_iconsdir}/hicolor/*x*/apps/*.png
%{_iconsdir}/hicolor/*x*/actions/*.png
%{_datadir}/knotifications6/kruler.notifyrc
%{_datadir}/kruler
%{_datadir}/metainfo/org.kde.kruler.appdata.xml
