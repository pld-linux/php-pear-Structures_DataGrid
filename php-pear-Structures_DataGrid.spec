%include	/usr/lib/rpm/macros.php
%define         _class          Structures
%define         _subclass       DataGrid
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - create grid like structure based on a recird set of data
#Summary(pl):	%{_pearname} - tworzenie s
Name:		php-pear-%{_pearname}
Version:	0.4.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b9b9a00f103fbc32571435a84060f473
URL:		http://pear.php.net/package/Structures_DataGrid/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package offers a toolkit to render out a datagrid in HTML format as
well as many other formats such as an XML Document, an Excel Spreadsheet,
a Smarty Template and more.  It also offers paging and sorting
functionallity to limit the data that is presented.  This concept is based
on the .NET Framework DataGrid

This class has in PEAR status: %{_status}.

#%description -l pl
#...
#
#Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/{Record,Renderer}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/Record/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Record
install %{_pearname}-%{version}/%{_subclass}/Renderer/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Renderer

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/%{_subclass}/Docs
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/
