Name:		texlive-icsv
Version:	15878
Release:	1
Summary:	Class for typesetting articles for the ICSV conference
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/conferences/icsv
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/icsv.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/icsv.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/icsv.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is an ad-hoc class for typesetting articles for the ICSV
conference, based on the earler active-conf by the same author.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/icsv/icsv.cls
%doc %{_texmfdistdir}/doc/latex/icsv/README
%doc %{_texmfdistdir}/doc/latex/icsv/icsv-example.tex
%doc %{_texmfdistdir}/doc/latex/icsv/icsv.pdf
#- source
%doc %{_texmfdistdir}/source/latex/icsv/icsv.dtx
%doc %{_texmfdistdir}/source/latex/icsv/icsv.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
