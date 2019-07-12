# Todo: make main program dinamically linked
%global commit0 5db3a78499c1a82882b1dd71b23bcf8dfa69f925
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:           kvazaar
Version:        1.3.0
Release:        1%{?gver}%{dist}
Summary:        An open-source HEVC encoder
License:        LGPLv2+
URL:            http://ultravideo.cs.tut.fi/#encoder

Source0:        https://github.com/ultravideo/kvazaar/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
Kvazaar is the leading academic open-source HEVC encoder developed from scratch
in C. This package contains the application for encoding videos.

%package        libs
Summary:        HEVC encoder %{name} libraries

%description    libs
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}. This package contains the shared libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{commit0} 
autoreconf -vif
%configure --disable-static

%build
make %{?_smp_mflags}

%install
%make_install

find %{buildroot} -name '*.la' -delete

# Pick up docs in the files section
rm -fr %{buildroot}%{_docdir}

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%{_bindir}/*
%{_mandir}/man1/*

%files libs
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README.md CREDITS
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog

* Thu Jul 11 2017 David Vasquez <davidva at tutanota dot com> 1.3.0-1.git5db3a78
- Updated to 1.3.0-1.git5db3a78

* Sun Nov 19 2017 David Vasquez <davidva at tutanota dot com> 1.2.0-1.gitcf85d52
- Updated to 1.2.0-1.gitcf85d52

* Wed Oct 25 2017 David Vasquez <davidva at tutanota dot com> 1.1.0-1.git9974380
- Upstream
- Updated to current commit

* Mon Jul 17 2017 Simone Caronni <negativo17@gmail.com> - 1.1.0-1
- Update to 1.1.0.

* Wed Nov 09 2016 Simone Caronni <negativo17@gmail.com> - 1.0.0-1
- Update to 1.0.0.

* Thu Jul 14 2016 Simone Caronni <negativo17@gmail.com> - 0.8.3-1
- Update to 0.8.3.

* Fri Mar 04 2016 Simone Caronni <negativo17@gmail.com> - 0.8.2-1
- Update to 0.8.2, remove old build/install procedure.

* Fri Nov 20 2015 Simone Caronni <negativo17@gmail.com> - 0.7.2-1
- First build.
