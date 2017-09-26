Summary: Couchbase Client & Protocol Library
Name: libcouchbase
Version: 2.8.1
Release: 1%{?dist}
Vendor: Couchbase, Inc.
License: ASL 2.0
Group: System Environment/Libraries
BuildRequires: cmake >= 2.8.9
BuildRequires: libevent-devel >= 1.4, libev-devel >= 3, openssl-devel
URL: https://developer.couchbase.com/server/other-products/release-notes-archives/c-sdk
Source: https://packages.couchbase.com/clients/c/libcouchbase-2.8.1.tar.gz

%description
This is the client and protocol library for Couchbase project.

%package -n %{name}2-libevent
Group: System Environment/Libraries
Summary: Couchbase Client & Protocol Library (libevent backend)
Requires: %{name}2-core%{?_isa} = %{version}-%{release}, libevent >= 1.4
%description -n %{name}2-libevent
This package provides libevent backend for libcouchbase

%package -n %{name}2-libev
Group: System Environment/Libraries
Summary: Couchbase Client & Protocol Library (libev backend)
Requires: %{name}2-core%{?_isa} = %{version}-%{release}, libev >= 3
%description -n %{name}2-libev
This package provides libev backend for libcouchbase

%package -n %{name}2-core
Group: System Environment/Libraries
Summary: Couchbase Client & Protocol Library (core)
Provides: %{name}2%{?_isa} = %{version}-%{release}
%description -n %{name}2-core
This package provides the core for libcouchbase. It contains an IO
implementation based on select(2). If preferred, you can install one
of the available backends (libcouchbase2-libevent or
libcouchbase2-libev).  libcouchbase will automatically use the
installed backend. It is also possible to integrate another IO backend
or write your own.

%package -n %{name}2-bin
Group: Development/Tools
Summary: Couchbase Client Tools
Requires: %{name}2-core = %{version}-%{release}
%if %{?fedora}0 >= 180 || %{?rhel}0 >= 70
Requires: %{name}2-libevent%{?_isa} = %{version}-%{release}
%endif
%description -n %{name}2-bin
This is the CLI tools Couchbase project.

%package devel
Group: Development/Libraries
Summary: Couchbase Client & Protocol Library - Header files
Requires: %{name}2-core%{?_isa} = %{version}-%{release}
%description devel
Development files for the Couchbase Client & Protocol Library

%prep
%setup -q -n libcouchbase-2.8.1
%cmake -DLCB_NO_TESTS=1 -DLCB_BUILD_LIBUV=OFF

%build
%{__make} %{_smp_mflags} V=1

%install
%{__make} install DESTDIR="%{buildroot}" AM_INSTALL_PROGRAM_FLAGS=""

%clean
%{__rm} -rf %{buildroot}

%post -n %{name}2-core -p /sbin/ldconfig

%postun -n %{name}2-core -p /sbin/ldconfig

%files -n %{name}2-core
%defattr(-, root, root)
%{_libdir}/%{name}.so.*
%doc README.markdown LICENSE RELEASE_NOTES.markdown

%files -n %{name}2-libevent
%defattr(-, root, root)
%{_libdir}/%{name}_libevent.so

%files -n %{name}2-libev
%defattr(-, root, root)
%{_libdir}/%{name}_libev.so

%files -n %{name}2-bin
%defattr(-, root, root)
%{_bindir}/cbc*
%{_mandir}/man1/cbc*.1*
%{_mandir}/man4/cbcrc*.4*

%files devel
%defattr(-, root, root)
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Tue Sep 26 2017 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.8.1-1
- Initial package
