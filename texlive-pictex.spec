%global tl_name pictex
%global tl_revision 59551

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1b
Release:	%{tl_revision}.1
Summary:	Picture drawing macros for TeX and LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pictex
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pictex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pictex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
PicTeX is an early and very comprehensive drawing package that mostly
draws by placing myriads of small dots to make up pictures. It has a
tendency to run out of space; packages m-pictex and pictexwd deal with
the problems in different ways.

