Summary:	Standard ML of New Jersey
Summary(pl.UTF-8):	Standard ML z New Jersey
Name:		smlnj
Version:	110.57
Release:	1
Epoch:		1
License:	BSD-like
Group:		Development/Languages
Source0:	http://smlnj.cs.uchicago.edu/dist/working/%{version}/config.tgz
# Source0-md5:	a0f556961bc93fb63fc8cc38813e8659
Source1:	http://smlnj.cs.uchicago.edu/dist/working/%{version}/boot.ppc-unix.tgz
# Source1-md5:	ae6ca067c1071c8006ccffefb8a6c4e9
Source2:	http://smlnj.cs.uchicago.edu/dist/working/%{version}/boot.sparc-unix.tgz
# Source2-md5:	56b18701a1c34ff4325c2818906b0ca3
Source3:	http://smlnj.cs.uchicago.edu/dist/working/%{version}/boot.x86-unix.tgz
# Source3-md5:	4af368d68bd472c35bc5aa83f9a59f34
Source4:	http://smlnj.cs.uchicago.edu/dist/working/%{version}/MLRISC.tgz
# Source4-md5:	3f0b6ff18038e0cbc08b317169917206
Source5:	http://smlnj.cs.uchicago.edu/dist/working/%{version}/ckit.tgz
# Source5-md5:	78530579023597067deabac1e3109afa
Source6:	http://smlnj.cs.uchicago.edu/dist/working/%{version}/cm.tgz
# Source6-md5:	7c286667e8be55a33287b02b1b4aa2d5
Source7:	http://smlnj.cs.uchicago.edu/dist/working/%{version}/cml.tgz
# Source7-md5:	6b23cc3b33465511ef9cca46cea5d9ab
Source8:	http://smlnj.cs.uchicago.edu/dist/working/%{version}/compiler.tgz
# Source8-md5:	7dba6d725648414733f11b8a1292c86e
Source9:	http://smlnj.cs.uchicago.edu/dist/working/%{version}/eXene.tgz
# Source9-md5:	656508ff3828344e7e6b59e3429f0f19
Source10:	http://smlnj.cs.uchicago.edu/dist/working/%{version}/ml-burg.tgz
# Source10-md5:	cbbf80c5cb007e83eb63a5cd94977b68
Source11:	http://smlnj.cs.uchicago.edu/dist/working/%{version}/ml-lex.tgz
# Source11-md5:	25d64f79f7de8e41d37911cdabad89b3
Source12:	http://smlnj.cs.uchicago.edu/dist/working/%{version}/ml-yacc.tgz
# Source12-md5:	b06c5be6d557751616fa430e421bf706
Source13:	http://smlnj.cs.uchicago.edu/dist/working/%{version}/ml-nlffi-lib.tgz
# Source13-md5:	3bb54918075534506b3d01a722c37aca
Source14:	http://smlnj.cs.uchicago.edu/dist/working/%{version}/ml-nlffigen.tgz
# Source14-md5:	62b30439b8d2be80c2db995dbb51dbaa
Source15:	http://smlnj.cs.uchicago.edu/dist/working/%{version}/runtime.tgz
# Source15-md5:	3e5bc506dffdbd93c004b33ae12ff49e
Source16:	http://smlnj.cs.uchicago.edu/dist/working/%{version}/smlnj-c.tgz
# Source16-md5:	c438ab652699c7d5afbd89f45be90486
Source17:	http://smlnj.cs.uchicago.edu/dist/working/%{version}/smlnj-lib.tgz
# Source17-md5:	e32800489430b8f598f849ab1524aac7
Source18:	http://smlnj.cs.uchicago.edu/dist/working/%{version}/system.tgz
# Source18-md5:	3a15e19305803ca5dbc3d4d28c278b53
Source19:	http://smlnj.cs.uchicago.edu/dist/working/%{version}/tools.tgz
# Source19-md5:	d96d685bdc258c55b15844faf057166f
Patch0:		%{name}-build.patch
URL:		http://www.smlnj.org/
#URL:		http://cm.bell-labs.com/cm/cs/what/smlnj/
BuildRequires:	tetex-latex
BuildRequires:	tetex-dvips
BuildRequires:	transfig
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86} ppc sparc

%description
Standard ML of New Jersey is most popular implementation of Standard
Meta Language (SML). It is compilant with SML'97 specification. SML is
functional language from ML family (like CAML).

%description -l pl.UTF-8
Standard ML z New Jersey jest najbardziej popularną implementacją
języka SML (Standard Meta Language). Jest ona kompatybilna ze
specyfikacją SML'97. SML jest językiem funkcjonalnym z rodziny ML (jak
CAML).

%prep
%setup -q -c
%patch0 -p1
install %SOURCE1 .
install %SOURCE2 .
install %SOURCE3 .
install %SOURCE4 .
install %SOURCE5 .
install %SOURCE6 .
install %SOURCE7 .
install %SOURCE8 .
install %SOURCE9 .
install %SOURCE10 .
install %SOURCE11 .
install %SOURCE12 .
install %SOURCE13 .
install %SOURCE14 .
install %SOURCE15 .
install %SOURCE16 .
install %SOURCE17 .
install %SOURCE18 .
install %SOURCE19 .

%build
CFLAGS="%{rpmcflags}" config/install.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/smlnj,%{_bindir}}

cp -a bin lib src $RPM_BUILD_ROOT%{_libdir}/smlnj
chmod u+w -R $RPM_BUILD_ROOT%{_libdir}/smlnj

sed -e "s|@SHELL@|/bin/sh|" \
    -e "s|@BINDIR@|%{_libdir}/smlnj/bin|" \
    -e "s|@VERSION@|`cat config/version`|" \
	config/_run-sml > $RPM_BUILD_ROOT%{_libdir}/smlnj/bin/.run-sml

find $RPM_BUILD_ROOT%{_libdir}/smlnj/lib/ -type f -name \*cm | \
	xargs sed -i -e "s|$PWD|%{_libdir}/smlnj|g"

# damn hacks..
rep=$(echo "$PWD" | sed -e 's|.|/|g' | \
	sed -e "s|$(echo "%{_libdir}/smlnj" | \
	sed -e 's|.|.|g')\$|%{_libdir}/smlnj|")

sed -i -e "s|$PWD|$rep|g" $RPM_BUILD_ROOT%{_libdir}/smlnj/bin/.heap/sml.*-linux

ln -sf %{_libdir}/smlnj/bin/{ml-{burg,lex,yacc},sml,sml-cm} \
	$RPM_BUILD_ROOT%{_bindir}

# documetation... gotta extract from src/ tree
rm -rf docs
mkdir -p docs/{cm,MLRISC}

# CM
cd src/cm/Doc
latex manual.tex
dvips -o manual.ps manual.dvi
mkdir HTML
./mkhtml -dir HTML manual.tex
cd -
cp -f src/cm/Doc/manual.ps docs/cm.ps
cp -f src/cm/Doc/HTML/*.{html,css,png} docs/cm

# CML
#cd src/cml/doc
#cd -
#cp -a src/cml/doc/HTML docs/cml
#cp -f src/cml/doc/Hardcopy/manual.ps docs/cml.ps

# ml-burg
cd src/ml-burg/doc
transfig -L ps tree.fig
make
latex doc.tex
dvips -o doc.ps doc.dvi
cd -
cp -f src/ml-burg/doc/doc.ps docs/ml-burg.ps

# ml-lex
cd src/ml-lex
latex lexgen.tex
dvips -o ml-lex.ps lexgen.dvi
cd -
cp -f src/ml-lex/ml-lex.ps docs/
cp -f src/ml-lex/mlex_int.doc docs/ml-lex-int.txt

# ml-nlffi-lib
cd src/ml-nlffi-lib/Doc/manual
latex nlffi.tex
dvips -o nlffi.ps nlffi.dvi
cd -
cp -f src/ml-nlffi-lib/Doc/mini-tutorial.txt docs/nlffi-mini-tutorial.txt
cp -f src/ml-nlffi-lib/Doc/manual/nlffi.ps docs/nlffi.ps

# ml-yacc
cd src/ml-yacc/doc
latex mlyacc.tex
dvips -o mlyacc.ps mlyacc.dvi
cd -
cp -f src/ml-yacc/doc/mlyacc.ps docs/
cp -f src/ml-yacc/doc/tech.doc docs/ml-yacc-tech.txt
cp -a src/ml-yacc/examples docs/ml-yacc-examples

# smlnj-lib
#cd src/smlnj-lib/Doc
#cp -a HTML docs/smlnj-lib
#cd -

# MLRISC
cd src/MLRISC/Doc
make -C pictures
make -C html
cd -
cp -a src/MLRISC/Doc/{graphics,pictures,html} docs/MLRISC/

# get rid of docs from src/ tree...
rm -rf $RPM_BUILD_ROOT%{_libdir}/smlnj/src/*/{Doc,doc}

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
%attr(755,root,root) %{_libdir}/smlnj/bin/.link-sml
%attr(755,root,root) %{_libdir}/smlnj/bin/.run-sml
%dir %{_libdir}/smlnj/bin/.run
%attr(755,root,root) %{_libdir}/smlnj/bin/.run/*
%{_libdir}/smlnj/bin/*
%{_libdir}/smlnj/lib
# some equivalent of make clean could be probably done here...
# however this source is needed to comiple some programs
%{_libdir}/smlnj/src
