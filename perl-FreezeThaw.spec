%include	/usr/lib/rpm/macros.perl
Summary:	FreezeThaw perl module
Summary(pl):	Modu� perla FreezeThaw
Name:		perl-FreezeThaw
Version:	0.41
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/FreezeThaw/FreezeThaw-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FreezeThaw - converting Perl structures to strings and back.

%description -l pl
FreezeThaw - konwertuje struktury do �a�cuch�w i odwrotnie.

%prep
%setup -q -n FreezeThaw-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/FreezeThaw.pm
%{_mandir}/man3/*
