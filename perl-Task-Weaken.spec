# NOTE
# - you should consider using pldcpan for new perl packages
#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Task
%define		pnam	Weaken
Summary:	Task::Weaken - ensure that a platform has weaken support
Summary(pl):	Task::Weaken - zapewnienie wsparcia dla "weaken" na platformie
Name:		perl-Task-Weaken
Version:	0.99
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Task/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	92de456b6d1be928428babb7ebcdc6c1
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module contains a replacement for Scalar::Util's "weaken"
function which is not present in the pure-perl variant.

%description -l pl
Modu� ten zast�puje funkcj� "weaken" ze Scalar::Util, kt�rej nie ma w
czystym Perlu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Task
%{_mandir}/man3/*
