Summary: Couchbase client library
Name: libcouchbase
Version: 2.8.1
Release: 1%{?dist}
License: ASL 2.0
BuildRequires: cmake >= 2.8.9
BuildRequires: pkgconfig(libevent) >= 2
BuildRequires: libev-devel >= 3
BuildRequires: openssl-devel
URL: https://developer.couchbase.com/server/other-products/release-notes-archives/c-sdk
Source: https://packages.couchbase.com/clients/c/%{name}-%{version}.tar.gz

%description
This package provides the core for libcouchbase. It contains an IO
implementation based on select(2). If preferred, you can install one
of the available backends (libcouchbase-libevent or libcouchbase-libev).
libcouchbase will automatically use the installed backend. It is also
 possible to integrate another IO backend or write your own.

%package libevent
Summary: Couchbase client library - libevent backend
Requires: %{name}%{?_isa} = %{version}-%{release}
%description libevent
This package provides libevent backend for libcouchbase

%package libev
Summary: Couchbase client library - libev backend
Requires: %{name}%{?_isa} = %{version}-%{release}
%description libev
This package provides libev backend for libcouchbase

%package tools
Summary: Couchbase client tools
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libevent%{?_isa}
%description tools
This is the CLI tools Couchbase project.

%package devel
Summary: Couchbase client library - Header files
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for the Couchbase Client & Protocol Library

%prep
%setup -q -n %{name}-%{version}
%cmake -DLCB_NO_TESTS=1 -DLCB_BUILD_LIBUV=OFF

%build
make %{_smp_mflags} V=1

%install
make install DESTDIR="%{buildroot}" AM_INSTALL_PROGRAM_FLAGS=""

%post -n %{name} -p /sbin/ldconfig

%postun -n %{name} -p /sbin/ldconfig

%files
%{_libdir}/%{name}.so.*
%doc README.markdown RELEASE_NOTES.markdown
%license LICENSE 

%files libevent
%{_libdir}/%{name}_libevent.so

%files libev
%{_libdir}/%{name}_libev.so

%files tools
%{_bindir}/cbc*
%{_mandir}/man1/cbc*.1*
%{_mandir}/man4/cbcrc*.4*

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Tue Sep 26 2017 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.8.1-1
- Initial package
