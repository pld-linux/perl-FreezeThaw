%include	/usr/lib/rpm/macros.perl
Summary:	FreezeThaw perl module
Summary(pl):	Modu³ perla FreezeThaw
Name:		perl-FreezeThaw
Version:	0.43
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/FreezeThaw/FreezeThaw-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FreezeThaw - converting Perl structures to strings and back.

%description -l pl
FreezeThaw - konwertuje struktury do ³añcuchów i odwrotnie.

%prep
%setup -q -n FreezeThaw-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/FreezeThaw.pm
%{_mandir}/man3/*
