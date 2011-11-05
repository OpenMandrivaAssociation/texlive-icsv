# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/conferences/icsv
# catalog-date 2008-05-21 23:07:53 +0200
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-icsv
Version:	0.2
Release:	1
Summary:	Class for typesetting articles for the ICSV conference
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/conferences/icsv
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/icsv.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/icsv.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/icsv.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This is an ad-hoc class for typesetting articles for the ICSV
conference, based on the earler active-conf by the same author.

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
%{_texmfdistdir}/tex/latex/icsv/icsv.cls
%doc %{_texmfdistdir}/doc/latex/icsv/README
%doc %{_texmfdistdir}/doc/latex/icsv/icsv-example.tex
%doc %{_texmfdistdir}/doc/latex/icsv/icsv.pdf
#- source
%doc %{_texmfdistdir}/source/latex/icsv/icsv.dtx
%doc %{_texmfdistdir}/source/latex/icsv/icsv.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
