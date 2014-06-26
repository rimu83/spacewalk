%{!?perlgen:%define perlgen 5.8}
Name: perl-Mail-RFC822-Address
Version: 0.3
Release: 10%{?dist}
Summary: Mail-RFC822-Address Perl module
License: distributable
Group: Development/Libraries
URL: http://search.cpan.org/search?mode=module&query=Mail%3a%3aRFC822%3a%3aAddress
BuildRoot: %{_tmppath}/%{name}-root
Buildarch: noarch
BuildRequires:	perl(ExtUtils::MakeMaker)


Requires: %(perl -MConfig -le 'if (defined $Config{useithreads}) { print "perl(:WITH_ITHREADS)" } else { print "perl(:WITHOUT_ITHREADS)" }')
Requires: %(perl -MConfig -le 'if (defined $Config{usethreads}) { print "perl(:WITH_THREADS)" } else { print "perl(:WITHOUT_THREADS)" }')
Requires: %(perl -MConfig -le 'if (defined $Config{uselargefiles}) { print "perl(:WITH_LARGEFILES)" } else { print "perl(:WITHOUT_LARGEFILES)" }')
Source0: Mail-RFC822-Address-0.3.tar.gz

%description
Mail-RFC822-Address Perl module
%prep
%setup -q -n Mail-RFC822-Address-%{version}

%build
%if "%{perlgen}" == "5.8"
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL PREFIX=$RPM_BUILD_ROOT%{_prefix} < /dev/null
%else
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL < /dev/null
%endif

make
make test

%clean
rm -rf $RPM_BUILD_ROOT
%install

rm -rf $RPM_BUILD_ROOT
eval `perl '-V:installarchlib'`
mkdir -p $RPM_BUILD_ROOT/$installarchlib
%if "%{perlgen}" == "5.8"
make install
%else
make install PREFIX=$RPM_BUILD_ROOT%{_prefix}
%endif


[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress

rm -f `find $RPM_BUILD_ROOT -type f -name perllocal.pod -o -name .packlist`
find $RPM_BUILD_ROOT/usr -type f -print | \
	sed "s@^$RPM_BUILD_ROOT@@g" | \
	grep -v perllocal.pod | \
	grep -v "\.packlist" > Mail-RFC822-Address-%{version}-filelist
if [ "$(cat Mail-RFC822-Address-%{version}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit 1
fi

%files -f Mail-RFC822-Address-%{version}-filelist

%changelog
* Thu Dec 12 2002 cturner@redhat.com
- Specfile autogenerated
