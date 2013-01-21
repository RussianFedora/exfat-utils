Summary:    Utilities for exFAT file system
Summary(ru):Утилиты для файловой системы exFAT
Name:       exfat-utils
Version:    1.0.0
Release:    1%{?dist}

License:    GPLv3+
Group:      System Environment/Base
Source0:    http://exfat.googlecode.com/files/exfat-utils-%{version}.tar.gz
URL:        http://code.google.com/p/exfat/

BuildRequires:  scons
BuildRequires:  fuse-devel


%description
A set of utilities for creating, checking, dumping and labelling exFAT file
system.

%description -l ru
Набор утилит для создания, проверки, дампа и назначения метки для
файловой системы exFAT.


%prep
%setup -q


%build
scons


%install
rm -rf $RPM_BUILD_ROOT
scons install DESTDIR=$RPM_BUILD_ROOT%{_sbindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8/
gzip -9 -c dump/dumpexfat.8 > $RPM_BUILD_ROOT%{_mandir}/man8/dumpexfat.8.gz
gzip -9 -c fsck/exfatfsck.8 > $RPM_BUILD_ROOT%{_mandir}/man8/exfatfsck.8.gz
gzip -9 -c mkfs/mkexfatfs.8 > $RPM_BUILD_ROOT%{_mandir}/man8/mkexfatfs.8.gz
gzip -9 -c label/exfatlabel.8 > $RPM_BUILD_ROOT%{_mandir}/man8/exfatlabel.8.gz


%files
%{_sbindir}/dumpexfat
%{_sbindir}/exfatfsck
%attr(755,root,root) %{_sbindir}/fsck.exfat
%{_sbindir}/mkexfatfs
%attr(755,root,root) %{_sbindir}/mkfs.exfat
%{_sbindir}/exfatlabel
%attr(644,root,root) %{_mandir}/man8/dumpexfat.8.gz
%attr(644,root,root) %{_mandir}/man8/exfatfsck.8.gz
%attr(644,root,root) %{_mandir}/man8/mkexfatfs.8.gz
%attr(644,root,root) %{_mandir}/man8/exfatlabel.8.gz


%changelog
* Mon Jan 21 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.0-1.R
- update to 1.0.0

* Sun Aug 12 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.9.8-1.R
- update to 0.9.8

* Tue Mar 13 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.9.7-1.R
- update to 0.9.7

* Tue Jan 17 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.9.6-1.R
- update to 0.9.6

* Thu Jun  7 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.9.5-1.R
- update to 0.9.5

* Fri Mar 18 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.9.4-2
- add BR fuse-devel

* Sat Mar  5 2011 Andrew Nayenko <resver@gmail.com> - 0.9.4-1
- Initial package for Fedora.
