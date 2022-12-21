Name:		limine
Version:	4.20221216.0
Release:	4
Summary:	An advanced, portable, multiprotocol bootloader
License:	BSD
URL:		https://limine-bootloader.org/
BuildRequires:	nasm
BuildRequires:	mtools
BuildRequires:	llvm
BuildRequires:	lld
BuildRequires:	clang
BuildArch:	x86_64 i386 aarch64 i586
Requires:	glibc
Source0:	https://github.com/limine-bootloader/limine/releases/download/v%{version}/limine-%{version}.tar.xz

%description
Limine is an advanced, portable, multiprotocol bootloader that supports Linux,
multiboot1 and 2, the native Limine boot protocol, and more.

%prep
%autosetup

%build
%ifarch x86_64
%configure --enable-bios-cd --enable-bios-pxe --enable-bios --enable-uefi-x86-64 --enable-uefi-cd CROSS_TOOLCHAIN=llvm
%endif
%ifarch i386 i586
%configure --enable-bios-cd --enable-bios-pxe --enable-bios --enable-uefi-ia32 --enable-uefi-cd CROSS_TOOLCHAIN=llvm
%endif
%ifarch aarch64
%configure --enable-uefi-aarch64 --enable-uefi-cd CROSS_TOOLCHAIN=llvm
%endif
%make_build

%install
%make_install

%files
%license LICENSE.md
# Limine utilities
%{_bindir}/limine-version
%ifarch x86_64 i386 i586
%{_bindir}/limine-deploy
%endif
# Limine
%ifarch x86_64 i386 i586
%{_datadir}/%{name}/limine-pxe.bin
%{_datadir}/%{name}/limine-cd.bin
%{_datadir}/%{name}/limine-cd-efi.bin
%{_datadir}/%{name}/limine.sys
%endif
%ifarch aarch64
%{_datadir}/%{name}/BOOTAA64.EFI
%{_datadir}/%{name}/limine-cd-efi.bin
%endif
%ifarch x86_64
%{_datadir}/%{name}/BOOTX64.EFI
%endif
%ifarch i386 i586
%{_datadir}/%{name}/BOOTIA32.EFI
%endif

%package devel
Version:	4.20221216.0
Release:	2
Summary:	An advanced, portable, multiprotocol bootloader (development library)
BuildArch:	noarch

%description devel
Limine is an advanced, portable, multiprotocol bootloader that supports Linux,
multiboot1 and 2, the native Limine boot protocol, and more. (development library)

%files devel
%{_includedir}/limine.h

%changelog
* Wed Dec 21 2022 Eric Zhang <ericzhang456@disroot.org> - 4.20221216.0
    - fix build for older versions of rpm
* Wed Dec 21 2022 Eric Zhang <ericzhang456@disroot.org> - 4.20221216.0
    - add support for opensuse i586
* Wed Dec 21 2022 Eric Zhang <ericzhang456@disroot.org> - 4.20221216.0
    - architecture specific tweaks
* Mon Dec 19 2022 Eric Zhang <ericzhang456@disroot.org> - 4.20221216.0
    - initial
