%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define devname %mklibname eigen -d

Summary:	Lightweight C++ template library for vector and matrix math
Name:		libeigen
Version:	1.0.5
Release:	11
Group:		System/Libraries
License:	LGPLv2+
Url:		http://download.tuxfamily.org/eigen/
Source0:	http://download.tuxfamily.org/eigen/eigen-%{version}.tar.bz2
BuildRequires:	cmake

%description
Eigen is a lightweight C++ template library for vector and matrix math, a.k.a.
linear algebra.

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Provides:	eigen-devel = %{EVRD}
Conflicts:	%{_lib}eigen1-devel < 1.0.5-6
Obsoletes:	%{_lib}eigen1-devel < 1.0.5-6

%description -n %{devname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%files -n %{devname}
%dir %{_includedir}/eigen/
%{_includedir}/eigen/*.h

#----------------------------------------------------------------------------

%prep
%setup -qn eigen

%build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_BUILD_TYPE=Debug \
	-DBUILD_EXAMPLES:BOOL=OFF \
%if "%{_lib}" != "lib"
	-DLIB_SUFFIX=64 \
%endif

%install
%makeinstall_std -C build

