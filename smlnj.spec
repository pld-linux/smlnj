Summary:	Standard ML of New Jersey
Name:		smlnj
Version:	110.0.7
Release:	1
Epoch:		1
License:	distributable
Group:		Development/Languages
Source0:	%{name}-%{version}.tar.bz2
#URL:		
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SML/NJ.

%prep
%setup  -q
tar -xzf config.tar.Z

%build
CFLAGS="%{rpmcflags}" config/install.sh

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/smlnj
cp -a bin lib src $RPM_BUILD_ROOT%{_libdir}/smlnj
chmod u+w -R $RPM_BUILD_ROOT%{_libdir}/smlnj
sed \
	-e "s|@BINDIR@|%{_libdir}/smlnj/bin|" \
	-e "s|@VERSION@|`cat config/version`|" \
	config/_run-sml > $RPM_BUILD_ROOT%{_libdir}/smlnj/bin/.run-sml
mkdir -p $RPM_BUILD_ROOT%{_prefix}/bin
for f in $RPM_BUILD_ROOT%{_libdir}/smlnj/lib/*cm; do
	sed -e "s|$PWD|%{_libdir}/smlnj|" $f > $f.new
	mv $f.new $f
done
ln -sf %{_libdir}/smlnj/bin/{ml-{burg,lex,yacc},sml,sml-cm} \
       $RPM_BUILD_ROOT%{_prefix}/bin

gzip -9nf 110*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_prefix}/bin/*
%dir %{_libdir}/smlnj
%dir %{_libdir}/smlnj/bin
%{_libdir}/smlnj/bin/.arch-n-opsys
%{_libdir}/smlnj/bin/.heap
%attr(755,root,root) %{_libdir}/smlnj/bin/.run-sml
%dir %{_libdir}/smlnj/bin/.run
%attr(755,root,root) %{_libdir}/smlnj/bin/.run/*
%{_libdir}/smlnj/bin/*
%{_libdir}/smlnj/lib
%{_libdir}/smlnj/src
