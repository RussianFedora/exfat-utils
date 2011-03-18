Name:			exfat-utils
Summary:		Utilities for exFAT file system
Version:		0.9.4
Release:		1%{?dist}
License:		GPLv3+
Group:			System Environment/Base
Source0:		http://exfat.googlecode.com/files/exfat-utils-%{version}.tar.gz
URL:			http://code.google.com/p/exfat/
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	scons
BuildRequires:	gzip

%description
A set of utilities for creating, checking, dumping and labelling exFAT file
system.

%prep
%setup -q

%build
scons

%install
rm -rf $RPM_BUILD_ROOT
scons install DESTDIR=$RPM_BUILD_ROOT/sbin
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man8/
gzip -9 -c dump/dumpexfat.8 > $RPM_BUILD_ROOT/usr/share/man/man8/dumpexfat.8.gz
gzip -9 -c fsck/exfatfsck.8 > $RPM_BUILD_ROOT/usr/share/man/man8/exfatfsck.8.gz
gzip -9 -c mkfs/mkexfatfs.8 > $RPM_BUILD_ROOT/usr/share/man/man8/mkexfatfs.8.gz
gzip -9 -c label/exfatlabel.8 > $RPM_BUILD_ROOT/usr/share/man/man8/exfatlabel.8.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/sbin/dumpexfat
/sbin/exfatfsck
%attr(755,root,root) /sbin/fsck.exfat
/sbin/mkexfatfs
%attr(755,root,root) /sbin/mkfs.exfat
/sbin/exfatlabel
%attr(644,root,root) /usr/share/man/man8/dumpexfat.8.gz
%attr(644,root,root) /usr/share/man/man8/exfatfsck.8.gz
%attr(644,root,root) /usr/share/man/man8/mkexfatfs.8.gz
%attr(644,root,root) /usr/share/man/man8/exfatlabel.8.gz

%changelog
* Sat Mar  5 2011 Andrew Nayenko <resver@gmail.com> - 0.9.4-1
- Initial package for Fedora.
