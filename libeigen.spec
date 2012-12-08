%define name libeigen
%define version	1.0.5
%define release %mkrel 5
%define lib_name %mklibname eigen 1

Name: 		%{name}
Summary: 	Lightweight C++ template library for vector and matrix math
Version: 	%{version}
Release: 	%{release}
Group: 		System/Libraries
License: 	LGPL
URL: 		http://download.tuxfamily.org/eigen/
Source:		eigen-%version.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  cmake

%description
Eigen is a lightweight C++ template library for vector and matrix math, a.k.a.
linear algebra.

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




%changelog
* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.5-4mdv2011.0
+ Revision: 425536
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.5-3mdv2009.0
+ Revision: 222539
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.5-2mdv2008.1
+ Revision: 170948
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix description-line-too-long

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.0.5-1mdv2008.1
+ Revision: 140921
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot


* Wed Feb 28 2007 Laurent Montel <lmontel@mandriva.com> 1.0.5-1mdv2007.0
+ Revision: 127080
- 1.0.5

* Mon Feb 26 2007 Laurent Montel <lmontel@mandriva.com> 1.0.4-1mdv2007.1
+ Revision: 125784
- 1.0.4

* Tue Feb 06 2007 Laurent Montel <lmontel@mandriva.com> 1.0.3-1mdv2007.1
+ Revision: 116802
- 1.0.3

* Mon Jan 22 2007 Laurent Montel <lmontel@mandriva.com> 1.0.2-1mdv2007.1
+ Revision: 111976
- Update

* Tue Jan 02 2007 Laurent Montel <lmontel@mandriva.com> 1.0-1mdv2007.1
+ Revision: 103131
- Import libeigen

* Tue Jan 02 2007 Laurent MONTEL <lmontel@mandriva.com> 1.0
- initial spec file created

