
%define realname   PPI-HTML
%define version    1.07
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Generate syntax-hightlighted HTML for Perl using PPI
Source:     http://www.cpan.org/modules/by-module/PPI/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(CSS::Tiny)
BuildRequires: perl(File::Spec)
BuildRequires: perl(PPI)
BuildRequires: perl(Params::Util)
BuildRequires: perl(Test::More)

BuildArch: noarch

%description
PPI::HTML converts Perl documents into syntax highlighted HTML pages.





%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README LICENSE
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/ppi2html

