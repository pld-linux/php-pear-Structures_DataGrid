%include	/usr/lib/rpm/macros.php
%define		_class		Structures
%define		_subclass	DataGrid
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - create grid like structure based on a record set of data
Summary(pl):	%{_pearname} - tworzenie struktur tabel opartych na zbiorze rekordów danych
Name:		php-pear-%{_pearname}
Version:	0.8.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	96e424a8e554388c340289c2b77efcaf
URL:		http://pear.php.net/package/Structures_DataGrid/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear >= 4:1.0-9.5
Requires:	php-pear-PEAR-core >= 1:1.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package offers a toolkit to render out a datagrid in HTML format
as well as many other formats such as an XML Document, an Excel
Spreadsheet, a Smarty Template and more. It also offers paging and
sorting functionality to limit the data that is presented. This
concept is based on the .NET Framework DataGrid.

Note: With the release of Structures_DataGrid-0.7.0, all renderers and
datasource classes are now available as a separate packages only.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet oferuje zestaw narzêdzi do renderowania tabel z danymi w
formacie HTML, a tak¿e innych formatach, takich jak np. dokumenty XML,
arkusze Excela czy szablony Smarty. Oferuje tak¿e funkcjonalno¶æ
stronicowania i sortowania, aby ograniczyæ ilo¶æ prezentowanych
danych. Ta idea jest oparta na DataGrid ze ¶rodowiska .NET.

Uwaga: Z wydaniem wersji Structures_DataGrid-0.7.0, wszystkie klasy
s³u¿±ce do renderowania czy te¿ do obs³ugi ¼róde³ danych dostêpne s±
tylko jako oddzielne pakiety.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Renderer
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/%{_subclass}/Renderer
