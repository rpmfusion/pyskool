%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           pyskool
Version:        1.1.1
Release:        1%{?dist}
Summary:        Remakes of Skool Daze and Back to Skool

# Proprietary graphics from the original game are used
License:        GPLv3+ and proprietary
URL:            http://pyskool.ca
Source0:        http://pyskool.ca/downloads/%{name}/%{name}-%{version}.tar.xz
Source1:        skool_daze.desktop
Source2:        back_to_skool.desktop

BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme
Requires:       pygame


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
%setup -q


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# Install game data
install -d %{buildroot}%{_datadir}/%{name}
cp -ar icon.png images images.ini ini pyskool.ini sounds \
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

# Install man pages
mkdir -p %{buildroot}%{_mandir}/man6/
install -p -m0644 man/man6/* %{buildroot}%{_mandir}/man6/


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

 
%files
%doc COPYING docs/*
%{_bindir}/ezad_looks.py
%{_bindir}/back_to_skool.py
%{_bindir}/skool_daze.py 
%{_bindir}/skool_daze_take_too.py
%{_bindir}/back_to_skool_daze.py
%{python_sitelib}/*
%{_datadir}/%{name}
%{_datadir}/applications/skool_daze.desktop
%{_datadir}/applications/back_to_skool.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man6/*


%changelog
* Sun Feb 2 2014 Andrea Musuruane <musuruan@gmail.com> 1.1.1-1
- Updated to upstream 1.1.1

* Fri Dec 6 2013 Andrea Musuruane <musuruan@gmail.com> 1.1-1
- Updated to upstream 1.1

* Thu Dec 6 2012 Andrea Musuruane <musuruan@gmail.com> 1.0.1-1
- Updated to upstream 1.0.1

* Wed Jun 1 2011 Andrea Musuruane <musuruan@gmail.com> 0.6-1
- First release
