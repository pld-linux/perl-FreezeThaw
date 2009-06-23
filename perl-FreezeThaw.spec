#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	FreezeThaw - converting Perl structures to strings and back
Summary(pl.UTF-8):	FreezeThaw - konwersja struktur Perla na łańcuchy i odwrotnie
Name:		perl-FreezeThaw
Version:	0.45
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/FreezeThaw/FreezeThaw-%{version}.tar.gz
# Source0-md5:	2060d11775f5546f97cc03d8f1ed98e5
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FreezeThaw module converts Perl data to/from stringified form,
appropriate for saving-to/reading-from permanent storage.

%description -l pl.UTF-8
Moduł FreezeThaw konwertuje dane Perla do/z postaci łańcuchów
tekstowych. Przydatne do zapisu na trwałym nośniku i odczycie z niego.

%prep
%setup -q -n FreezeThaw-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/FreezeThaw.pm
%{_mandir}/man3/*
