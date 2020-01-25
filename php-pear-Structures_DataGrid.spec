%define		status		beta
%define		pearname	Structures_DataGrid
Summary:	%{pearname} - create grid like structure based on a record set of data
Summary(pl.UTF-8):	%{pearname} - tworzenie struktur tabel opartych na zbiorze rekordów danych
Name:		php-pear-%{pearname}
Version:	0.9.3
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	108ed5caedb4b3634e214af9cb7dd968
URL:		http://pear.php.net/package/Structures_DataGrid/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear >= 4:1.0-9.5
Requires:	php-pear-PEAR-core >= 1:1.4.9
Suggests:	php-pear-File
Suggests:	php-pear-Net_URL_Mapper
Suggests:	php-pear-PHPUnit
Suggests:	php-sqlite
Obsoletes:	php-pear-Structures_DataGrid-tests
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

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Ten pakiet oferuje zestaw narzędzi do renderowania tabel z danymi w
formacie HTML, a także innych formatach, takich jak np. dokumenty XML,
arkusze Excela czy szablony Smarty. Oferuje także funkcjonalność
stronicowania i sortowania, aby ograniczyć ilość prezentowanych
danych. Ta idea jest oparta na DataGrid ze środowiska .NET.

Uwaga: Z wydaniem wersji Structures_DataGrid-0.7.0, wszystkie klasy
służące do renderowania czy też do obsługi źródeł danych dostępne są
tylko jako oddzielne pakiety.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Structures/DataGrid/{Renderer,DataSource}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Structures/DataGrid.php
%dir %{php_pear_dir}/Structures/DataGrid
%{php_pear_dir}/Structures/DataGrid/Column.php
%{php_pear_dir}/Structures/DataGrid/DataSource.php
%{php_pear_dir}/Structures/DataGrid/Exception.php
%{php_pear_dir}/Structures/DataGrid/Renderer.php
%dir %{php_pear_dir}/Structures/DataGrid/Renderer
%dir %{php_pear_dir}/Structures/DataGrid/DataSource
