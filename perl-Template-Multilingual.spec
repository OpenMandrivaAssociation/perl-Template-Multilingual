%define module  Template-Multilingual
%define upstream_version 1.00

Name:		perl-%{module}
Version:	%{upstream_version}
Release:	7
Summary:	Multilingual templates for Template Toolkit
License:	GPL or Artistic
Group:		Development/Perl
Source:		https://cpan.metacpan.org/authors/id/C/CH/CHOLET/Template-Multilingual-%{upstream_version}.tar.gz
Url:		https://metacpan.org/dist/Template-Multilingual
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
