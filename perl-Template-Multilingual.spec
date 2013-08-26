%define module  Template-Multilingual
%define upstream_version 1.00

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Summary:	Multilingual templates for Template Toolkit
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Template/Template-Multilingual-%{upstream_version}.tar.gz
Url:		http://search.cpan.org/dist/%{module}/
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Template)
BuildArch:	noarch

%description
This subclass of Template Toolkit's Template class supports multilingual
templates: templates that contain text in several languages.

%prep
%setup -q -n %{module}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot}

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/Template/Multilingual.pm
%{perl_vendorlib}/Template/Multilingual
%{_mandir}/*/*



%changelog
* Mon Sep 14 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.00-2mdv2010.0
+ Revision: 440693
- rebuild

* Tue Jan 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.00-1mdv2009.1
+ Revision: 331589
- update to new version 1.00
- update to new version 1.00

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.09-3mdv2009.0
+ Revision: 241912
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Aug 08 2007 Funda Wang <fundawang@mandriva.org> 0.09-1mdv2008.0
+ Revision: 60464
- New version 0.09

* Thu May 03 2007 Olivier Thauvin <nanardon@mandriva.org> 0.08-1mdv2008.0
+ Revision: 22086
- 0.08


* Wed May 17 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.06-1mdk
- First Mandriva release


