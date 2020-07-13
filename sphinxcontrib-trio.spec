#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sphinxcontrib-trio
Version  : 1.1.2
Release  : 12
URL      : https://files.pythonhosted.org/packages/ca/33/ee48d86e30bb3c5d72a47f49b1ebf5c23dd253b04d8d5fc3e6c68407a03e/sphinxcontrib-trio-1.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/ca/33/ee48d86e30bb3c5d72a47f49b1ebf5c23dd253b04d8d5fc3e6c68407a03e/sphinxcontrib-trio-1.1.2.tar.gz
Summary  : Make Sphinx better at documenting Python functions and methods
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: sphinxcontrib-trio-license = %{version}-%{release}
Requires: sphinxcontrib-trio-python = %{version}-%{release}
Requires: sphinxcontrib-trio-python3 = %{version}-%{release}
Requires: Sphinx
BuildRequires : Sphinx
BuildRequires : buildreq-distutils3

%description
sphinxcontrib-trio
        ==================
        
        This sphinx extension helps you document Python code that uses
        async/await, or abstract methods, or context managers, or generators,
        or ... you get the idea. It works by making sphinx's regular
        directives for documenting Python functions and methods smarter and
        more powerful. The name is because it was originally written for the

%package license
Summary: license components for the sphinxcontrib-trio package.
Group: Default

%description license
license components for the sphinxcontrib-trio package.


%package python
Summary: python components for the sphinxcontrib-trio package.
Group: Default
Requires: sphinxcontrib-trio-python3 = %{version}-%{release}

%description python
python components for the sphinxcontrib-trio package.


%package python3
Summary: python3 components for the sphinxcontrib-trio package.
Group: Default
Requires: python3-core
Provides: pypi(sphinxcontrib_trio)
Requires: pypi(sphinx)

%description python3
python3 components for the sphinxcontrib-trio package.


%prep
%setup -q -n sphinxcontrib-trio-1.1.2
cd %{_builddir}/sphinxcontrib-trio-1.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588631345
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sphinxcontrib-trio
cp %{_builddir}/sphinxcontrib-trio-1.1.2/LICENSE.APACHE2 %{buildroot}/usr/share/package-licenses/sphinxcontrib-trio/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/sphinxcontrib-trio-1.1.2/LICENSE.MIT %{buildroot}/usr/share/package-licenses/sphinxcontrib-trio/f8c5fdc67d412f3435473ee8ce595f06d921ca44
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sphinxcontrib-trio/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/sphinxcontrib-trio/f8c5fdc67d412f3435473ee8ce595f06d921ca44

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
