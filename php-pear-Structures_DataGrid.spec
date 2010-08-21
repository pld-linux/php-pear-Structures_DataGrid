%include	/usr/lib/rpm/macros.php
%define		_class		Structures
%define		_subclass	DataGrid
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - create grid like structure based on a record set of data
Summary(pl.UTF-8):	%{_pearname} - tworzenie struktur tabel opartych na zbiorze rekordów danych
Name:		php-pear-%{_pearname}
Version:	0.9.0
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	9aa37e190d2c0856bfc4bb556409285c
URL:		http://pear.php.net/package/Structures_DataGrid/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear >= 4:1.0-9.5
Requires:	php-pear-PEAR-core >= 1:1.4.9
Suggests:	php-pear-File
Suggests:	php-pear-Net_URL_Mapper
Suggests:	php-pear-PHPUnit
Suggests:	php-sqlite
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(File.*) pear(Net/URL/Mapper.*) pear(PHPUnit.*)

%description
This package offers a toolkit to render out a datagrid in HTML format
as well as many other formats such as an XML Document, an Excel
Spreadsheet, a Smarty Template and more. It also offers paging and
sorting functionality to limit the data that is presented. This
concept is based on the .NET Framework DataGrid.

Note: With the release of Structures_DataGrid-0.7.0, all renderers and
datasource classes are now available as a separate packages only.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet oferuje zestaw narzędzi do renderowania tabel z danymi w
formacie HTML, a także innych formatach, takich jak np. dokumenty XML,
arkusze Excela czy szablony Smarty. Oferuje także funkcjonalność
stronicowania i sortowania, aby ograniczyć ilość prezentowanych
danych. Ta idea jest oparta na DataGrid ze środowiska .NET.

Uwaga: Z wydaniem wersji Structures_DataGrid-0.7.0, wszystkie klasy
służące do renderowania czy też do obsługi źródeł danych dostępne są
tylko jako oddzielne pakiety.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/{Renderer,DataSource}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Renderer
%dir %{php_pear_dir}/%{_class}/%{_subclass}/DataSource

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Structures_DataGrid
