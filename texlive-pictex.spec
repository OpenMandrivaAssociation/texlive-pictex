Name:		texlive-pictex
Version:	1.1
Release:	1
Summary:	Picture drawing macros for TeX and LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pictex
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pictex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pictex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
