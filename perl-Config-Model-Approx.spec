%define upstream_name    Config-Model-Approx
%define upstream_version 1.003

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Approx configuration file editor
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Config::Model)
BuildRequires: perl(Config::Model::CursesUI)
BuildRequires: perl(Config::Model::TkUI)
BuildRequires: perl(Module::Build)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This module provides a configuration model for Approx. Then Config::Model provides a graphical editor program for /etc/approx/approx.conf. See config-edit-approx more help.

This module and Config::Model can also be used from Perl programs to modify safely the content of /etc/approx/approx.conf.

Once this module is installed, you can run:

 # config-edit-approx

The Perl API is documented in Config::Model and mostly in Config::Model::Node.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README ChangeLog
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/Config/Model/models/Approx.pl
%{perl_vendorlib}/Config/Model/Approx.pm
