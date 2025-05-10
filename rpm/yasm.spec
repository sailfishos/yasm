Name:           yasm
Summary:        A complete rewrite of the NASM assembler
License:        BSD and (GPLv2+ or Artistic or LGPLv2+) and LGPLv2
Version:        1.3.0
Release:        1
Url:            https://github.com/sailfishos/yasm
Source:         %{name}-%{version}.tar.bz2
Patch1:         0001-Use-GNUInstallDirs-for-file-paths-when-installing-fi.patch
Patch2:         yasm-gcc15.patch
# From https://github.com/yasm/yasm/pull/286
Patch3:         0002-Bump-CMAKE_MINIMUM_REQUIRED-to-3.5-285.patch
BuildRequires:  cmake
BuildRequires:  python3-base
ExclusiveArch:  %{ix86} x86_64

%description
Yasm is a complete rewrite of the NASM assembler. It is designed from
the ground up to allow for multiple syntaxes to be supported (e.g.,
NASM, TASM, GAS, etc.) in addition to multiple output object formats
and even multiple instruction sets.
Another primary module of the overall design is an optimizer module.
Actually it supports ix86 and AMD64, next will be PowerPC.

%package devel
Summary:        YASM development package
Requires:       %{name} = %{version}

%description devel
This package includes headers needed to develop programs that use libyasm.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%cmake -DBUILD_SHARED_LIBS=ON -DENABLE_NLS=OFF
%cmake_build

%install
%cmake_install

%files
%license Artistic.txt BSD.txt COPYING GNU_GPL-2.0 GNU_LGPL-2.0
%{_bindir}/vsyasm
%{_bindir}/yasm
%{_bindir}/ytasm
%{_libdir}/*.so

%files devel
%doc AUTHORS
%{_includedir}/*
