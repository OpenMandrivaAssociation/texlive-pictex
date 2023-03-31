Name:		texlive-pictex
Version:	59551
Release:	2
Summary:	Picture drawing macros for TeX and LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pictex
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pictex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pictex.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/generic/pictex
%doc %{_texmfdistdir}/doc/generic/pictex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
