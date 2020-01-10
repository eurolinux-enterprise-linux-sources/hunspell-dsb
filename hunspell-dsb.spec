Name: hunspell-dsb
Summary: Lower Sorbian hunspell dictionaries
Version: 1.4.6
Release: 4%{?dist}
Group: Applications/Text
Source: http://extensions.services.openoffice.org/e-files/3045/12/lower_sorbian_spelling_dictionary-1.4.6.oxt
URL: http://dsb-spell.sourceforge.net
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch

Requires: hunspell

%description
Lower Sorbian hunspell dictionaries.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dsb_DE.* $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc description/desc_de.txt description/desc_en.txt description/desc_pl.txt registration/license_en.txt  

%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.4.6-4
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 14 2012 Caolán McNamara <caolanm@redhat.com> - 1.4.6-1
- latest version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 08 2011 Caolán McNamara <caolanm@redhat.com> - 1.4.5-1
- latest version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 04 2011 Caolán McNamara <caolanm@redhat.com> - 1.4.4-1
- latest version

* Thu Dec 02 2010 Caolán McNamara <caolanm@redhat.com> - 1.4.3-1
- latest version

* Mon May 24 2010 Caolán McNamara <caolanm@redhat.com> - 1.4.2-1
- latest version

* Sun Apr 11 2010 Caolán McNamara <caolanm@redhat.com> - 1.4.1-1
- latest version

* Wed Mar 31 2010 Caolán McNamara <caolanm@redhat.com> - 1.4.0-1
- latest version

* Thu Mar 04 2010 Caolán McNamara <caolanm@redhat.com> - 1.3.0-1
- latest version

* Wed Jan 06 2010 Caolán McNamara <caolanm@redhat.com> - 1.2.0-1
- latest version

* Fri Dec 11 2009 Caolán McNamara <caolanm@redhat.com> - 1.1.3-1
- latest version

* Tue Nov 03 2009 Caolán McNamara <caolanm@redhat.com> - 1.1.2-1
- latest version

* Wed Oct 14 2009 Caolán McNamara <caolanm@redhat.com> - 1.1.1-1
- initial version
