#
# spec file for package yasm
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           yasm
Summary:        A complete rewrite of the NASM assembler
License:        (Artistic-1.0 or GPLv2+ or LGPLv2+) and BSD and GPLv2+ and LGPLv2+
Group:          Development/Languages/Other
Version:        1.3.0
Release:        0
Url:            http://www.tortall.net/projects/yasm/releases
Source:         %{name}-%{version}.tar.gz
Patch0:         0001-%{name}-No-build-date.patch
Patch1:         0002-%{name}-No-RPM-opt-flags.patch
BuildRequires:  python
ExclusiveArch:  i586 i486 i386 x86_64

%description
YASM is a complete rewrite of the NASM assembler. It is designed from
the ground up to allow for multiple syntaxes to be supported (e.g.,
NASM, TASM, GAS, etc.) in addition to multiple output object formats.
Another primary module of the overall design is an optimizer module.
Actually it supports ix86 and AMD64, next will be PowerPC

%package devel
Summary:        YASM development package
Group:          Development/Languages
Requires:       %{name} = %{version}

%description devel
This package includes everything needed to develop programs that use
libyasm.

%prep
%setup -q -n %{name}-%{version}/%{name}
%patch0 -p1
%patch1 -p1

%build
export CFLAGS="%{optflags}"
%autogen \
 --with-gnu-ld \
 --enable-python
make %{?jobs:-j%jobs}

%install
%makeinstall

%files
%defattr(-,root,root)
%doc Artistic.txt BSD.txt COPYING GNU_GPL-2.0 GNU_LGPL-2.0
%doc ABOUT-NLS AUTHORS ChangeLog NEWS README
/usr/bin/*
%_mandir/man7/*
%_mandir/man1/*

%files devel
%defattr(-,root,root)
/usr/include/*
%_libdir/lib*.a
