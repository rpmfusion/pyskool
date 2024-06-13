Name:           pyskool
Version:        1.2.1
Release:        18%{?dist}
Summary:        Remakes of Skool Daze and Back to Skool

# Proprietary graphics from the original game are used
License:        GPLv3+ and proprietary
URL:            http://pyskool.ca
Source0:        %url/downloads/%{name}/%{name}-%{version}.tar.xz
Source1:        skool_daze.desktop
Source2:        back_to_skool.desktop
Patch0:         temporary_python312_fix.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       hicolor-icon-theme
Requires:       python3-pygame

%description
The games are based in a boys’ school and revolved around the antics of Eric,
the hero. 

In Skool Daze, Eric must steal his report card from the school safe - the 
combination of which must be extracted from the teachers’ brains using flashing
shields or, in the case of the history teacher, post-hypnotic suggestion. 

In Back to Skool, Eric must get his report card back into the school safe, 
this time with the extra help provided by a water pistol, stink-bombs, a bike, 
mice, a frog and a girlfriend.


%prep
%autosetup -p1


%build
%{py3_build}


%install
%{py3_install}

# Install game data
install -d %{buildroot}%{_datadir}/%{name}
cp -ar icon.png images ini sounds \
  %{buildroot}%{_datadir}/%{name}

# Install icon
install -d %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 0644 icon.png \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

# Install desktop files
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE2}

# Install appdata
install -d %{buildroot}%{_datadir}/metainfo
install -p -m 0644 xdg/pyskool.appdata.xml \
  %{buildroot}%{_datadir}/metainfo
appstream-util validate-relax --nonet \
  %{buildroot}%{_datadir}/metainfo/*.appdata.xml

# Install man pages
mkdir -p %{buildroot}%{_mandir}/man6/
install -p -m0644 man/man6/* %{buildroot}%{_mandir}/man6/


%files
%doc docs/*
%license COPYING
%{_bindir}/ezad_looks.py
%{_bindir}/back_to_skool.py
%{_bindir}/skool_daze.py 
%{_bindir}/skool_daze_take_too.py
%{_bindir}/back_to_skool_daze.py
%{python3_sitelib}/*
%{_datadir}/%{name}/
%{_datadir}/applications/skool_daze.desktop
%{_datadir}/applications/back_to_skool.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man6/*


%changelog
* Thu Jun 13 2024 Leigh Scott <leigh123linux@gmail.com> - 1.2.1-18
- Rebuilt for Python 3.13

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 03 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Leigh Scott <leigh123linux@gmail.com> - 1.2.1-15
- Rebuilt for Python 3.12

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Leigh Scott <leigh123linux@gmail.com> - 1.2.1-11
- Rebuild for python-3.10

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Leigh Scott <leigh123linux@gmail.com> - 1.2.1-8
- Rebuild for python-3.9

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 24 2019 Leigh Scott <leigh123linux@gmail.com> - 1.2.1-6
- Rebuild for python-3.8

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Andrea Musuruane <musuruan@gmail.com> - 1.2.1-4
- Rebuilt for python3
- Used new AppData directory

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.1-2
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Wed Jul 25 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.1-1
- Updated to upstream 1.2.1
- Remove obsolete scriptlets
- Update for python changes in F29

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 01 2016 Sérgio Basto <sergio@serjux.com> - 1.2-2
-
  https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Jan 17 2015 Andrea Musuruane <musuruan@gmail.com> 1.2-1
- Updated to upstream 1.2
- Added appdata

* Sun Jun 15 2014 Andrea Musuruane <musuruan@gmail.com> 1.1.2-1
- Updated to upstream 1.1.2

* Sun Feb 2 2014 Andrea Musuruane <musuruan@gmail.com> 1.1.1-1
- Updated to upstream 1.1.1

* Fri Dec 6 2013 Andrea Musuruane <musuruan@gmail.com> 1.1-1
- Updated to upstream 1.1

* Thu Dec 6 2012 Andrea Musuruane <musuruan@gmail.com> 1.0.1-1
- Updated to upstream 1.0.1

* Wed Jun 1 2011 Andrea Musuruane <musuruan@gmail.com> 0.6-1
- First release
