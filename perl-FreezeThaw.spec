%include	/usr/lib/rpm/macros.perl
Summary:	FreezeThaw perl module
Summary(pl):	Modu³ perla FreezeThaw
Name:		perl-FreezeThaw
Version:	0.3
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module//FreezeThaw-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FreezeThaw - converting Perl structures to strings and back.

%description -l pl
FreezeThaw - konwertuje struktury do ³añcuchów i odwrotnie.

%prep
%setup -q -n FreezeThaw-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/FreezeThaw
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/FreezeThaw.pm
%{perl_sitearch}/auto/FreezeThaw

%{_mandir}/man3/*
