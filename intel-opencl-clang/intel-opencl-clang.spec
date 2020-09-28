%if 0%{?fedora} > 32
%global LLVM_VERSION 11.0.0
%else
%global LLVM_VERSION 10.0.0
%endif

%global patchver 2

Name:           intel-opencl-clang
Version:        10.0.0
Release:        %{patchver}.1%{?dist}
Summary:        Intel(R) OpenCL(TM) Clang

License:        MIT
URL:            https://github.com/intel/opencl-clang
Source0:        %{url}/archive/v%{version}/%{name}-%{version}-%{patchver}.tar.gz
Patch0:         %{url}/commit/5fcd66e46d1a3e6bc47b6c8134bcbb0ac3376677.patch
Patch1:         %{url}/commit/9f0c2c0f5ddea1accc921aed4c94bc52c1b85637.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++

BuildRequires:  clang-devel
BuildRequires:  llvm-devel
BuildRequires:  spirv-llvm-translator-devel

%description
OpenCL clang is a thin wrapper library around clang.
OpenCL clang has OpenCL-oriented API and is capable
to compile OpenCL C kernels to SPIR-V modules.

%package        devel
Summary:        Development files Intel(R) OpenCL(TM) Clang
Requires:       %{name} = %{version}-%{release}

%description    devel
Development package for opencl-clang


%prep
%autosetup -n opencl-clang-%{version}


%build
%cmake -DPREFERRED_LLVM_VERSION=%{LLVM_VERSION}
%cmake_build


%install
%cmake_install


%files
%license LICENSE
%doc README.md
%{_libdir}/libopencl-clang.so
%{_libdir}/libopencl-clang.so.*

%files devel
%{_includedir}/cclang/*



%changelog
* Mon Sep 28 19:45:56 +03 2020 ElXreno <elxreno@gmail.com> - 10.0.0-2.1
- Initial packaging
