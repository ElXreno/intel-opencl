%define _lto_cflags %{nil}

%if 0%{?fedora} > 32
%global LLVM_VERSION 11.0.0
%else
%global LLVM_VERSION 10.0.0
%endif

%global patch_version 5176

%global vc_intrinsics_commit c8c52b5fb14b33e32de9df573b7de186a0c97c94
%global llvm_commit llvmorg-10.0.1
# Hack
%global LLVM_VERSION 10.0.1
%global spirv_llvm_translator_commit  v10.0.0
%global llvm_patches_commit cfc800519a71522194efcaa9a5dd67ecbff43ffa
%global opencl_clang_commit v10.0.0-2

Name:           intel-igc
Version:        1.0.5176
Release:        1%{?dist}
Summary:        Intel(R) Graphics Compiler for OpenCL(TM)

License:        MIT
URL:            https://github.com/intel/intel-graphics-compiler
Source0:        %{url}/archive/igc-%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/intel/vc-intrinsics/archive/%{vc_intrinsics_commit}/vc-intrinsics-%{vc_intrinsics_commit}.tar.gz
Source2:        https://github.com/llvm/llvm-project/archive/%{llvm_commit}/llvm-project-%{llvm_commit}.tar.gz
Source3:        https://github.com/KhronosGroup/SPIRV-LLVM-Translator/archive/%{spirv_llvm_translator_commit}/spirv-llvm-translator-%{spirv_llvm_translator_commit}.tar.gz
Source4:        https://github.com/intel/llvm-patches/archive/%{llvm_patches_commit}/llvm-patches-%{llvm_patches_commit}.tar.gz
Source5:        https://github.com/intel/opencl-clang/archive/%{opencl_clang_commit}/intel-opencl-clang-%{opencl_clang_commit}.tar.gz
Source11:       fix_for_opt_buildbreak.patch
Patch0:         %{url}/commit/f4efb15429bdaca0122640ae63042a8950b491df.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  git

BuildRequires:  z3-devel

%description
Intel(R) Graphics Compiler for OpenCL(TM).

%package        core
Summary:        Intel(R) Graphics Compiler Core

%description    core

%package        opencl
Summary:        Intel(R) Graphics Compiler Frontend
Requires:       %{name}-core = %{version}-%{release}
Requires:       intel-opencl-clang >= 10.0.14

%description    opencl

%package        opencl-devel
Summary:        Intel(R) Graphics Compiler development package
Requires:       %{name}-opencl = %{version}-%{release}

%description    opencl-devel

%prep
mkdir igc vc-intrinsics llvm-project llvm_patches

tar xzf %{SOURCE0} -C igc --strip-components=1

tar xvf %{SOURCE1} -C vc-intrinsics --strip-components=1

tar xvf %{SOURCE2} -C llvm-project --strip-components=1
mv llvm-project/clang llvm-project/llvm/tools/

pushd llvm-project/llvm/projects
mkdir llvm-spirv opencl-clang
tar xvf %{SOURCE3} -C llvm-spirv --strip-components=1
tar xvf %{SOURCE5} -C opencl-clang --strip-components=1
popd

tar xvf %{SOURCE4} -C llvm_patches --strip-components=1

# Update patch
cp -f %{SOURCE11} llvm_patches/releases/10.0.0/patches_external/


%build
%cmake -Wno-dev -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr  \
    -DIGC_PREFERRED_LLVM_VERSION=%{LLVM_VERSION} -DIGC_PACKAGE_RELEASE=%{patch_version} \
    -DINSTALL_GENX_IR=OFF \
    ./igc/IGC
%make_build -C %{_target_platform}

%install
%make_install -C %{_target_platform}
rm -fv %{buildroot}/usr/bin/GenX_IR

%files core
%{_libdir}/libiga64.so.1
%{_libdir}/libiga64.so.%{version}
%{_libdir}/libigc.so.1
%{_libdir}/libigc.so.%{version}
%{_bindir}/iga64
%{_libdir}/igc/NOTICES.txt

%files opencl
%{_libdir}/libigdfcl.so.1
%{_libdir}/libigdfcl.so.%{version}

%files opencl-devel
%{_includedir}/igc/*
%{_includedir}/iga/*
%{_includedir}/visa/*
%{_libdir}/libiga64.so
%{_libdir}/libigc.so
%{_libdir}/libigdfcl.so
%{_libdir}/pkgconfig/*

%changelog
* Wed Oct  7 16:43:16 +03 2020 ElXreno <elxreno@gmail.com> - 1.0.5176-1
- Update to version 1.0.5176

* Fri Jul 10 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.4312-1
- Update to 1.0.4312

* Mon Jun 29 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.4241-1
- Update to 1.0.4241

* Tue Jun 09 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.4154-1
- Update to 1.0.4154

* Fri Jun 05 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.4116-1
- Update to 1.0.4116

* Tue May 26 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.4062-1
- Update to 1.0.4062

* Thu May 21 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.4036-2
- Add workaround from https://github.com/intel/intel-graphics-compiler/pull/135

* Wed May 20 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.4036-1
- Update to 1.0.4036

* Tue May 12 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3977-1
- Update to 1.0.3977

* Thu May 07 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3951-1
- Update to 1.0.3951

* Wed Apr 29 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3899-1
- Update to 1.0.3899

* Tue Apr 21 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3826-1
- Update to 1.0.3826

* Wed Apr 15 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3800-1
- Update to 1.0.3800

* Wed Apr 08 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3752-1
- Update to 1.0.3752

* Wed Mar 25 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3627-1
- Update to 1.0.3627

* Tue Mar 17 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3572-1
- Update to 1.0.3572

* Tue Mar 10 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3529-2
- Rebuild with opencl-clang 10.0.4

* Mon Mar 09 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3529-1
- Update to 1.0.3529

* Mon Feb 24 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3445-1
- Update to 1.0.3445

* Wed Feb 12 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3342-1
- Update to 1.0.3342
- Build with llvm/clang 10

* Tue Feb 04 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3289-1
- Update to 1.0.3289

* Wed Jan 15 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3151-1
- Update to 1.0.3151

* Thu Dec 19 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3041-2
- Fix IGC commit

* Tue Dec 10 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3041-1
- Update to 1.0.3041

* Mon Dec 02 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2990-1
- Update to 1.0.2990

* Tue Nov 26 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2972-1
- Update to 1.0.2972

* Tue Nov 26 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2934-1
- Update to 1.0.2934

* Thu Nov 21 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2916-1
- Update to 1.0.2916

* Wed Nov 20 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2878-1
- Update to 1.0.2878

* Thu Nov 14 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2805-1
- Update to 1.0.2805

* Wed Oct 30 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2714.1-1
- Update to 1.0.2714.1

