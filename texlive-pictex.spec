# revision 21943
# category Package
# catalog-ctan /graphics/pictex
# catalog-date 2011-04-03 16:40:50 +0200
# catalog-license lppl1
# catalog-version 1.1
Name:		texlive-pictex
Version:	1.1
Release:	9
Summary:	Picture drawing macros for TeX and LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pictex
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pictex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pictex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
PicTeX is an early, and very comprehensive drawing package,
that mostly draws by placing myriads of small dots to make up
pictures. It has a tendency to run out of space, most
especially of allowable dimensions registers; packages m-pictex
and pictexwd deal with the register problem, in different ways.
Note that full documentation may be bought via the PC-TeX site,
though a command summary is available as free software.
Alternatively, a front-end package such as mathsPiC, which
covers all of PicTeX and has a complete and free manual, could
be used.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pictex/errorbars.tex
%{_texmfdistdir}/tex/generic/pictex/latexpicobjs.tex
%{_texmfdistdir}/tex/generic/pictex/piccorr.sty
%{_texmfdistdir}/tex/generic/pictex/picmore.tex
%{_texmfdistdir}/tex/generic/pictex/pictex.sty
%{_texmfdistdir}/tex/generic/pictex/pictex.tex
%{_texmfdistdir}/tex/generic/pictex/pictexwd.sty
%{_texmfdistdir}/tex/generic/pictex/pictexwd.tex
%{_texmfdistdir}/tex/generic/pictex/pointers.tex
%{_texmfdistdir}/tex/generic/pictex/postpictex.tex
%{_texmfdistdir}/tex/generic/pictex/prepictex.tex
%{_texmfdistdir}/tex/generic/pictex/texpictex.tex
%{_texmfdistdir}/tex/generic/pictex/tree.sty
%doc %{_texmfdistdir}/doc/generic/pictex/00index
%doc %{_texmfdistdir}/doc/generic/pictex/README
%doc %{_texmfdistdir}/doc/generic/pictex/pictexzusatz.txt
%doc %{_texmfdistdir}/doc/generic/pictex/readme.errorbars

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 754901
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 719257
- texlive-pictex
- texlive-pictex
- texlive-pictex
- texlive-pictex

