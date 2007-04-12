%define module  Template-Multilingual
%define name	perl-%{module}
%define version 0.06
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Multilingual templates for Template Toolkit
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Template/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Template)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
This subclass of Template Toolkit's Template class supports multilingual
templates: templates that contain text in several languages.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%check
./Build test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Template/Multilingual.pm
%{perl_vendorlib}/Template/Multilingual
%{_mandir}/*/*

