Name:		texlive-pax
Version:	63509
Release:	1
Summary:	Extract and reinsert PDF annotations with pdfTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pax/pax-tds.zip
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pax.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pax.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pax.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-pax.bin = %{EVRD}

%description
If PDF files are included using pdfTeX, PDF annotations are
stripped. The pax project offers a solution without altering
pdfTeX. A Java program (pax.jar) parses the PDF file that will
later be included. The program then writes the data of the
annotations into a file that can be read by TeX. The LaTeX
package pax extends the graphics package to support the scheme:
if a PDF file is included, the package looks for the file with
the annotation data, reads them and puts the annotations in the
right place. Project status: experimental.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/pdfannotextractor
%{_datadir}/java/pax.jar
%{_texmfdistdir}/scripts/pax
%{_texmfdistdir}/tex/latex/pax
%doc %{_texmfdistdir}/doc/latex/pax
#- source
%doc %{_texmfdistdir}/source/latex/pax

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/pax/pdfannotextractor.pl pdfannotextractor
popd
mkdir -p %{buildroot}%{_datadir}/java
pushd %{buildroot}%{_datadir}/java
ln -sf %{_texmfdistdir}/scripts/pax/pax.jar pax.jar
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
