Summary:	Standard ML of New Jersey
Summary(pl):	Standard ML z New Jersey
Name:		smlnj
Version:	110.0.7
Release:	4
Epoch:		1
License:	BSD-like
Group:		Development/Languages
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	f3415cfa3ee7069c3bd02dce82f0431d
URL:		http://www.smlnj.org/
#URL:		http://cm.bell-labs.com/cm/cs/what/smlnj/
BuildRequires:	tetex-latex
BuildRequires:	tetex-dvips
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86}

%description
Standard ML of New Jersey is most popular implementation of Standard
Meta Language (SML). It is compilant with SML'97 specification. SML is
functional language from ML family (like CAML).

%description -l pl
Standard ML z New Jersey jest najbardziej popularn± implementacj±
jêzyka SML (Standard Meta Language). Jest ona kompatybilna ze
specyfikacj± SML'97. SML jest jêzykiem funkcjonalnym z rodziny ML (jak
CAML).

%prep
%setup  -q
tar -xzf config.tar.Z

%build
CFLAGS="%{rpmcflags}" config/install.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/smlnj
cp -a bin lib src $RPM_BUILD_ROOT%{_libdir}/smlnj
chmod u+w -R $RPM_BUILD_ROOT%{_libdir}/smlnj
sed \
	-e "s|@BINDIR@|%{_libdir}/smlnj/bin|" \
	-e "s|@VERSION@|`cat config/version`|" \
	config/_run-sml > $RPM_BUILD_ROOT%{_libdir}/smlnj/bin/.run-sml
install -d $RPM_BUILD_ROOT%{_bindir}
for f in $RPM_BUILD_ROOT%{_libdir}/smlnj/lib/*cm; do
	sed -e "s|$PWD|%{_libdir}/smlnj|" $f > $f.new
	mv $f.new $f
done
# damn hacks..
rep=$(echo "$PWD" | sed -e 's|.|/|g' | \
      sed -e "s|$(echo "%{_libdir}/smlnj" | \
	      sed -e 's|.|.|g')\$|%{_libdir}/smlnj|")
sed -e "s|$PWD|$rep|g" bin/.heap/sml-cm*-linux > \
	$RPM_BUILD_ROOT%{_libdir}/smlnj/bin/.heap/sml-cm*-linux

ln -sf %{_libdir}/smlnj/bin/{ml-{burg,lex,yacc},sml,sml-cm} \
       $RPM_BUILD_ROOT%{_bindir}

# documetation... gotta extract from src/ tree
rm -rf docs
mkdir docs
# CM
cp -f src/cm/Doc/manual.ps docs/cm.ps
mkdir docs/cm
cp -f src/cm/Doc/HTML/*.{html,css,gif} docs/cm
# CML
cp -a src/cml/doc/HTML docs/cml
cp -f src/cml/doc/Hardcopy/manual.ps docs/cml.ps
# ml-burg
cp -f src/ml-burg/doc/doc.ps docs/ml-burg.ps
# ml-lex
cd src/ml-lex
latex lexgen.tex
dvips lexgen.dvi -o ml-lex.ps
cd ../..
cp -f src/ml-lex/ml-lex.ps docs/
cp -f src/ml-lex/mlex_int.doc docs/ml-lex-int.txt
# ml-yacc
cd src/ml-yacc/doc
latex mlyacc.tex
dvips mlyacc.dvi -o ml-yacc.ps
cd ../../..
cp -f src/ml-yacc/doc/ml-yacc.ps docs/
cp -f src/ml-yacc/doc/tech.doc docs/ml-yacc-tech.txt
cp -a src/ml-yacc/examples docs/ml-yacc-examples
# smlnj-lib
cp -a src/smlnj-lib/Doc/HTML docs/smlnj-lib

# get rid of docs from src/ tree...
rm -rf $RPM_BUILD_ROOT%{_libdir}/smlnj/src/*/{Doc,doc}

cp -f 110* docs/
rm docs/110-README.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/smlnj
%dir %{_libdir}/smlnj/bin
%{_libdir}/smlnj/bin/.heap
%attr(755,root,root) %{_libdir}/smlnj/bin/.arch-n-opsys
%attr(755,root,root) %{_libdir}/smlnj/bin/.run-sml
%dir %{_libdir}/smlnj/bin/.run
%attr(755,root,root) %{_libdir}/smlnj/bin/.run/*
%{_libdir}/smlnj/bin/*
%{_libdir}/smlnj/lib
# some equivalent of make clean could be probably done here...
# however this source is needed to comiple some programs
%{_libdir}/smlnj/src
