Summary:        Utilities for exFAT file system
Summary(ru):    Утилиты для файловой системы exFAT
Name:           exfat-utils
Version:        1.2.4
Release:        1%{?dist}

License:        GPLv2+
Group:          System Environment/Base
Source0:        https://github.com/relan/exfat/releases/download/v%{version}/exfat-utils-%{version}.tar.gz
URL:            https://github.com/relan/exfat


%description
A set of utilities for creating, checking, dumping and labelling exFAT file
system.

%description -l ru
Набор утилит для создания, проверки, дампа и назначения метки для
файловой системы exFAT.


%prep
%setup -q


%build
%configure
%make_build


%install
%make_install INSTALL="install -p"


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
* Thu Jun 23 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 1.2.4-1
- Clean spec
- Update to 1.2.4

* Wed Mar 30 2016 Orion Poplawski <orion@cora.nwra.com> - 1.2.3-1
- Update to 1.2.3

* Sat Nov 14 2015 Nicolas Chauvet <kwizart@gmail.com> - 1.2.2-1
- Update to 1.2.2

* Sat Dec 20 2014 TingPing <tingping@tingping.se> - 1.1.1-1
- Update to 1.1.1

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Mar 20 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.1-1.R
- update to 1.0.1

* Mon Jan 21 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.0-1.R
- update to 1.0.0

* Sun Aug 12 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.9.8-1.R
- update to 0.9.8

* Tue Mar 13 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.9.7-1.R
- update to 0.9.7

* Tue Jan 17 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.9.6-1.R
- update to 0.9.6

* Tue Jun  7 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.9.5-1.R
- update to 0.9.5

* Fri Mar 18 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.9.4-2
- add BR fuse-devel

* Sat Mar  5 2011 Andrew Nayenko <resver@gmail.com> - 0.9.4-1
- Initial package for Fedora.
