# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/conferences/icsv
# catalog-date 2008-05-21 23:07:53 +0200
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-icsv
Version:	0.2
Release:	11
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 752684
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 718692
- texlive-icsv
- texlive-icsv
- texlive-icsv
- texlive-icsv

