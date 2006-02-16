%include	/usr/lib/rpm/macros.php
%define		_class		Structures
%define		_subclass	DataGrid
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - create grid like structure based on a record set of data
Summary(pl):	%{_pearname} - tworzenie struktur tabel opartych na zbiorze rekordów danych
Name:		php-pear-%{_pearname}
Version:	0.6.2
Release:	5
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	469f7663bf635cd28745f33d3ba54797
Patch0:		%{name}-path.patch
URL:		http://pear.php.net/package/Structures_DataGrid/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear >= 4:1.0-9.5
Requires:	php-pear-PEAR-core >= 1:1.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(HTML/Table.*)' 'pear(Pager.*)' 'pear(Spreadsheet/Excel/Writer.*)' 'pear(XML/Util.*)' 'pear(XML/RSS.*)' 'pear(XML/Serializer.*)' 'pear(Console/Table.*)' 'pear(Smarty/Smarty.class.php)'

%description
This package offers a toolkit to render out a datagrid in HTML format
as well as many other formats such as an XML Document, an Excel
Spreadsheet, a Smarty Template and more. It also offers paging and
sorting functionality to limit the data that is presented. This
concept is based on the .NET Framework DataGrid.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet oferuje zestaw narzêdzi do renderowania tabel z danymi w
formacie HTML, a tak¿e innych formatach, takich jak np. dokumenty XML,
arkusze Excela czy szablony Smarty. Oferuje tak¿e funkcjonalno¶æ
stronicowania i sortowania, aby ograniczyæ ilo¶æ prezentowanych
danych. Ta idea jest oparta na DataGrid ze ¶rodowiska .NET.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
%patch0 -p1

install -d docs/%{_pearname}
mv ./%{php_pear_dir}/%{_class}/%{_subclass}/Docs/* docs/%{_pearname}
rmdir ./%{php_pear_dir}/%{_class}/%{_subclass}/Docs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
