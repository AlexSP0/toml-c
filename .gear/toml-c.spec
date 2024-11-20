%define unpackaged_files_terminate_build 1

Name: toml-c
Version: 1.0
Release: alt1.gitc072e53

Summary: C-library for toml-files parsing
License: %mit
Group: Other
Url: https://github.com/arp242/toml-c
Source0: %name-%version.tar
Patch: %name-%version-alt1.gitc072e53-makefile-pcfile-fixes.patch

BuildRequires(pre): rpm-build-licenses

%description
C library for parsing toml files.

%prep
%setup -q
%patch -p1

%build
%make_build

%install
%makeinstall_std PREFIX=%_libdir

%files
%_libdir/libtoml.a
%_libdir/libtoml.so.%{version}
%_libdir/include/toml.h
%_pkgconfigdir/libtoml.pc

%changelog
* Tue Nov 19 2024 Aleksey Saprunov <sav@altlinux.org> 1.0-alt1.gitc072e53
- Initial build.

