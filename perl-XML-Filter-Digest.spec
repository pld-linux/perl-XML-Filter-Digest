#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Filter-Digest
Summary:	XML::Filter::Digest - parse formatted output and produce XML
Summary(pl.UTF-8):   XML::Filter::Digest - analiza sformatowanego wyjścia i tworzenia XML-a
Name:		perl-XML-Filter-Digest
Version:	0.06
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1a8ed951ec85851ad483f794f68ca54e
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Digest-MD5 >= 2.09
BuildRequires:	perl-XML-Handler-YAWriter >= 0.1
BuildRequires:	perl(XML::Parser::PerlSAX) >= 0.06
BuildRequires:	perl-XML-XPath >= 0.51
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Most XML tools aim to parse some simple XML and to produce some
formatted output. XML::Filter::Digest aims to do the opposite.

Many formats can now be parsed by a SAX Driver. XPath offers a smart
way to write queries to XML. XML::Filter::Digest is a PerlSAX Filter
to query XML and to provide a simpler digest as a result.

XML::Filter::Digest uses its own script language that can be parsed by
XML::Script::Digest to formulate these digest queries.

%description -l pl.UTF-8
Celem większości narzędzi do XML-a jest analiza jakiegoś prostego
XML-a i stworzenie jakiegoś sformatowanego wyjścia. Cel
XML::Filter::Digest jest coś przeciwnego.

Teraz sterownik SAX może przetwarzać wiele formatów. XPath oferuje
elegancki sposób pisania zapytań dla XML-a. XML::Filter::Digest to
filtr PerlSAX do odpytywania XML-a i dostarczania w wyniku prostego
podsumowania.

XML::Filter::Digest używa własnego języka skryptowego, który może być
przetwarzany przez XML::Script::Digest aby sformułować te zapytania
podsumowujące.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/XML/*/*.pm
%{_mandir}/man3/*
%{_mandir}/man1/*
