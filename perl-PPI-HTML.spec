%define upstream_name    PPI-HTML
%define upstream_version 1.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Generate syntax-hightlighted HTML for Perl using PPI
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/PPI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(CSS::Tiny)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(PPI)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
PPI::HTML converts Perl documents into syntax highlighted HTML pages.


%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/ppi2html


%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.80.0-2mdv2011.0
+ Revision: 654275
- rebuild for updated spec-helper

* Mon Nov 16 2009 Jérôme Quelin <jquelin@mandriva.org> 1.80.0-1mdv2011.0
+ Revision: 466429
- update to 1.08

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.70.0-1mdv2010.0
+ Revision: 401613
- rebuild using %%perl_convert_version
- fixed license field

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 1.07-2mdv2010.0
+ Revision: 375906
- rebuild

* Tue Mar 31 2009 Jérôme Quelin <jquelin@mandriva.org> 1.07-1mdv2009.1
+ Revision: 362909
- import perl-PPI-HTML


* Tue Mar 31 2009 cpan2dist 1.07-1mdv
- initial mdv release, generated with cpan2dist

