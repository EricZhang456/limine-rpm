Name:		limine
Version:	4.20221216.0
Release:	1	
Summary:	An advanced, portable, multiprotocol bootloader
License:	BSD
URL:		https://limine-bootloader.org/
BuildRequires:	nasm
BuildRequires:	mtools
BuildRequires:	llvm
BuildRequires:	lld
BuildRequires:	clang
BuildArch:	x86_64
Requires:	glibc
Source0:	https://github.com/limine-bootloader/limine/releases/download/v4.20221216.0/limine-4.20221216.0.tar.xz

%description
Limine is an advanced, portable, multiprotocol bootloader that supports Linux,
multiboot1 and 2, the native Limine boot protocol, and more.

%prep
%autosetup

%conf
%configure --enable-all

%build
%make_build

%install
%make_install

%files
#%license LICENSE
# Limine utilities
%{_bindir}/limine-version
%{_bindir}/limine-deploy
# Limine
%{_datadir}/%{name}/limine-pxe.bin
%{_datadir}/%{name}/limine-cd.bin
%{_datadir}/%{name}/BOOTAA64.EFI
%{_datadir}/%{name}/limine.sys
%{_datadir}/%{name}/BOOTX64.EFI
%{_datadir}/%{name}/BOOTIA32.EFI
%{_datadir}/%{name}/limine-cd-efi.bin

%package devel
Version:	4.20221216.0
Release:	1	
Summary:	An advanced, portable, multiprotocol bootloader (development library)

%description devel
Limine is an advanced, portable, multiprotocol bootloader that supports Linux,
multiboot1 and 2, the native Limine boot protocol, and more. (development library)

%files devel
%{_includedir}/limine.h

%changelog
* Mon Dec 19 2022 Eric Zhang <ericzhang456@disroot.org> - 4.20221216.0
    - initial
