#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-Find-Rule
Version  : 0.34
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/File-Find-Rule-0.34.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/File-Find-Rule-0.34.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : GPL-1.0
Requires: perl-File-Find-Rule-bin
Requires: perl-File-Find-Rule-man
Requires: perl(Text::Glob)
BuildRequires : perl(Text::Glob)

%description
No detailed description available

%package bin
Summary: bin components for the perl-File-Find-Rule package.
Group: Binaries
Requires: perl-File-Find-Rule-man

%description bin
bin components for the perl-File-Find-Rule package.


%package man
Summary: man components for the perl-File-Find-Rule package.
Group: Default

%description man
man components for the perl-File-Find-Rule package.


%prep
%setup -q -n File-Find-Rule-0.34

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/File/Find/Rule.pm
/usr/lib/perl5/site_perl/5.26.1/File/Find/Rule/Extending.pod
/usr/lib/perl5/site_perl/5.26.1/File/Find/Rule/Procedural.pod

%files bin
%defattr(-,root,root,-)
/usr/bin/findrule

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/findrule.1
/usr/share/man/man3/File::Find::Rule.3
/usr/share/man/man3/File::Find::Rule::Extending.3
/usr/share/man/man3/File::Find::Rule::Procedural.3
