%global major_version 20
%global minor_version 3
%global patch_version 2
%global api_patch_version 865

Name:           intel-gmmlib
Version:        %{major_version}.%{minor_version}.%{patch_version}
Release:        1%{?dist}
Summary:        Intel(R) Graphics Memory Management Library Package

Group:          System Environment/Libraries
License:        MIT
URL:            https://github.com/intel/gmmlib
Source0:        %{url}/archive/%{name}-%{version}.tar.gz
ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
Intel(R) Graphics Memory Management Library

%package        devel
Summary:        Intel(R) Graphics Memory Management Library development package
Group:          Development
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains library and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n gmmlib-intel-gmmlib-%{version}
find Source -name "*.cpp" -exec chmod -x {} ';'
find Source -name "*.h" -exec chmod -x {} ';'

%build
%cmake \
    -DMAJOR_VERSION=%{major_version} -DMINOR_VERSION=%{minor_version} -DPATCH_VERSION=%{patch_version} \
    -DGMMLIB_API_PATCH_VERSION=%{api_patch_version} \
    -DRUN_TEST_SUITE:BOOL='ON'
%cmake_build

%install
%cmake_install

%files
%defattr(-,root,root)
/usr/lib64/libigdgmm.so.*

%files devel
%defattr(-,root,root)
/usr/include/igdgmm/*
/usr/lib64/libigdgmm.so
/usr/lib64/pkgconfig/igdgmm.pc

%changelog
* Wed Oct  7 15:56:08 +03 2020 ElXreno <elxreno@gmail.com> - 20.3.2-1
- Update to version 20.3.2

* Thu Sep 03 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.2.4-1
- Update to 20.2.4

* Thu Jul 30 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.2.3-1
- Update to 20.2.3

* Wed Mar 25 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.1.1-1
- Update to 20.1.1

* Fri Jan 03 2020 Jacek Danecki <jacek.danecki@intel.com> - 19.4.1-1
- Update to 19.4.1

* Tue Nov 19 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.3.4-1
- Update to 19.3.4
