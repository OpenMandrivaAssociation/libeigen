%define	debug_package	%nil
%define major	1
%define libname %mklibname eigen %{major}

Summary: 	Lightweight C++ template library for vector and matrix math
Name: 		libeigen
Version: 	1.0.5
Release: 	5
Group: 		System/Libraries
License: 	LGPLv2
Url: 		http://download.tuxfamily.org/eigen/
Source0:	http://download.tuxfamily.org/eigen/eigen-%{version}.tar.gz
BuildRequires:  cmake

%description
Eigen is a lightweight C++ template library for vector and matrix math, a.k.a.
linear algebra.

%package -n %{libname}-devel
Summary: 	Headers for developing programs that will use %{name}
Group: 		Development/C
Provides: 	eigen-devel = %{version}-%{release}

%description -n %{libname}-devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -qn eigen

%build
export QTDIR=/usr/lib/qt4/
export PATH=$QTDIR/bin:$PATH

%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_BUILD_TYPE=Debug \
%if "%{_lib}" != "lib"
	-DLIB_SUFFIX=64 \
%endif

%make

%install
%makeinstall_std -C build

%files -n %{libname}-devel
%dir %{_includedir}/eigen/
%{_includedir}/eigen/*.h

