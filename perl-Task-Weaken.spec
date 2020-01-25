#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Task
%define		pnam	Weaken
Summary:	Task::Weaken - ensure that a platform has weaken support
Summary(pl.UTF-8):	Task::Weaken - zapewnienie obsługi "weaken" na każdej platformie
Name:		perl-Task-Weaken
Version:	1.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Task/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4c66b1ac45257ac7fd670920daebf868
URL:		http://search.cpan.org/dist/Task-Weaken/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module contains a replacement for Scalar::Util's "weaken"
function which is not present in the pure-perl variant.

%description -l pl.UTF-8
Moduł ten zastępuje funkcję "weaken" ze Scalar::Util, której nie ma w
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
%dir %{perl_vendorlib}/Task
%{perl_vendorlib}/Task/Weaken.pm
%{_mandir}/man3/Task::Weaken.3pm*
