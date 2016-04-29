#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cliff-tablib
Version  : 1.1
Release  : 10
URL      : https://github.com/dreamhost/cliff-tablib/archive/1.1.tar.gz
Source0  : https://github.com/dreamhost/cliff-tablib/archive/1.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: cliff-tablib-python
BuildRequires : cliff-python
BuildRequires : coverage
BuildRequires : nose
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : tablib-python

%description
=======================================================
cliff-tablib -- Formatting Extensions for Cliff
=======================================================

%package python
Summary: python components for the cliff-tablib package.
Group: Default

%description python
python components for the cliff-tablib package.


%prep
%setup -q -n cliff-tablib-1.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
python -m nose -d --with-coverage --cover-inclusive --cover-package clifftablib
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
