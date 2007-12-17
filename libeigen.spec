%define name libeigen
%define version	1.0.5
%define release %mkrel 1
%define lib_name %mklibname eigen 1

Name: 		%{name}
Summary: 	Eigen is a lightweight C++ template library for vector and matrix math
Version: 	%{version}
Release: 	%{release}
Group: 		System/Libraries
License: 	LGPL
URL: 		http://download.tuxfamily.org/eigen/
Source:		eigen-%version.tar.bz2
BuildRequires:  cmake

%description
Eigen is a lightweight C++ template library for vector and matrix math, a.k.a. linear algebra.

%package -n %{lib_name}-devel
Summary: 	Headers for developing programs that will use %{name}
Group: 		Development/C
Provides: 	eigen-devel = %{version}-%{release}

%description -n %{lib_name}-devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q -n eigen

%build
cd $RPM_BUILD_DIR/eigen/
mkdir build
cd build
export QTDIR=/usr/lib/qt4/
export PATH=$QTDIR/bin:$PATH

cmake -DCMAKE_INSTALL_PREFIX=%_prefix \
      -DCMAKE_BUILD_TYPE=Debug \
%if "%{_lib}" != "lib"
      -DLIB_SUFFIX=64 \
%endif
        ../

%make


%install
rm -rf $RPM_BUILD_ROOT
cd $RPM_BUILD_DIR/eigen/build/
make DESTDIR=%buildroot install




%clean 
rm -rf $RPM_BUILD_ROOT

%files -n %{lib_name}-devel
%defattr(-,root,root)
%dir %_includedir/eigen/
%_includedir/eigen/*.h

