# revision 26112
# category Package
# catalog-ctan /macros/latex/contrib/pax/pax-tds.zip
# catalog-date 2012-04-18 16:26:37 +0200
# catalog-license other-free
# catalog-version v0.1k
Name:		texlive-pax
Version:	v0.1k
Release:	3
Summary:	Extract and reinsert PDF annotations with pdfTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pax/pax-tds.zip
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pax.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pax.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pax.source.tar.xz
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
%{_javadir}/pax.jar
%{_texmfdistdir}/scripts/pax/pax.jar
%{_texmfdistdir}/scripts/pax/pdfannotextractor.pl
%{_texmfdistdir}/tex/latex/pax/pax.sty
%doc %{_texmfdistdir}/doc/latex/pax/README
#- source
%doc %{_texmfdistdir}/source/latex/pax/build.xml
%doc %{_texmfdistdir}/source/latex/pax/license/LaTeX/lppl.txt
%doc %{_texmfdistdir}/source/latex/pax/license/PDFAnnotExtractor/gpl.txt
%doc %{_texmfdistdir}/source/latex/pax/src/Constants.java
%doc %{_texmfdistdir}/source/latex/pax/src/Entry.java
%doc %{_texmfdistdir}/source/latex/pax/src/EntryWriteException.java
%doc %{_texmfdistdir}/source/latex/pax/src/MANIFEST.MF
%doc %{_texmfdistdir}/source/latex/pax/src/PDFAnnotExtractor.java
%doc %{_texmfdistdir}/source/latex/pax/src/StringVisitor.java

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/pax/pdfannotextractor.pl pdfannotextractor
popd
mkdir -p %{buildroot}%{_javadir}
pushd %{buildroot}%{_javadir}
    ln -sf %{_texmfdistdir}/scripts/pax/pax.jar pax.jar
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> v0.1k-3
+ Revision: 805015
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> v0.1k-2
+ Revision: 754724
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v0.1k-1
+ Revision: 719209
- texlive-pax
- texlive-pax
- texlive-pax
- texlive-pax

