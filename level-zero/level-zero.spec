%define debug_package %{nil}

%global major_version 1
%global minor_version 0
%global patch_version 0

Name:           level-zero
Version:        %{major_version}.%{minor_version}.%{patch_version}
Release:        2%{?dist}
Summary:        oneAPI Level Zero Specification Headers and Loader 

License:        MIT
URL:            https://github.com/oneapi-src/level-zero
Source0:        %{url}/archive/v%{major_version}.%{minor_version}/%{name}-%{version}.tar.gz
ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
oneAPI Level Zero Specification Headers and Loader 

%package       devel
Summary:       oneAPI Level Zero Specification Headers and Loader development package
Requires:      %{name} = %{version}-%{release}

%description   devel
The %{name}-devel package contains library and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n level-zero-%{major_version}.%{minor_version}
echo %{patch_version} > VERSION_PATCH

%build
%cmake ..
%cmake_build

%install
%cmake_install

%files
%{_libdir}/libze_loader.so.%{major_version}
%{_libdir}/libze_loader.so.%{major_version}.%{minor_version}.%{patch_version}
%{_libdir}/libze_validation_layer.so.%{major_version}
%{_libdir}/libze_validation_layer.so.%{major_version}.%{minor_version}.%{patch_version}

%files devel
%{_includedir}/level_zero/*
%{_libdir}/libze_loader.so
%{_libdir}/libze_validation_layer.so

%changelog
* Wed Oct  7 15:49:13 +03 2020 ElXreno <elxreno@gmail.com> - 1.0.0-2
- Fix indent and build

* Fri Oct 02 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.0-1
- Update to 1.0.0

* Thu Apr 09 2020 Jacek Danecki <jacek.danecki@intel.com> - 0.91.10-1
- Update to 0.91.10

* Fri Mar 27 2020 Jacek Danecki <jacek.danecki@intel.com> - 0.91.2-1
- Initial packaging 0.91.2

