# revision 22929
# category Package
# catalog-ctan /macros/latex/contrib/babel-contrib/serbianc
# catalog-date 2011-06-09 20:30:15 +0200
# catalog-license lppl1.3
# catalog-version 2.2
Name:		texlive-serbianc
Version:	2.2
Release:	4
Summary:	Babel module to support Serbian Cyrillic
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/serbianc
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/serbianc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/serbianc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/serbianc.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides support for Serbian documents written in
Cyrillic, in babel.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/serbianc/serbianc.ldf
%{_texmfdistdir}/tex/generic/serbianc/serbianc.sty
%doc %{_texmfdistdir}/doc/generic/serbianc/COPYING
%doc %{_texmfdistdir}/doc/generic/serbianc/ChangeLog
%doc %{_texmfdistdir}/doc/generic/serbianc/Copyright
%doc %{_texmfdistdir}/doc/generic/serbianc/INSTALL
%doc %{_texmfdistdir}/doc/generic/serbianc/README
%doc %{_texmfdistdir}/doc/generic/serbianc/README.Files
%doc %{_texmfdistdir}/doc/generic/serbianc/sample.pdf
%doc %{_texmfdistdir}/doc/generic/serbianc/sample.tex
%doc %{_texmfdistdir}/doc/latex/serbianc/README
#- source
%doc %{_texmfdistdir}/source/generic/serbianc/serbianc.dtx
%doc %{_texmfdistdir}/source/generic/serbianc/serbianc.ins
%doc %{_texmfdistdir}/source/generic/serbianc/serbianc.patch

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.2-2
+ Revision: 755911
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.2-1
+ Revision: 719509
- texlive-serbianc
- texlive-serbianc
- texlive-serbianc
- texlive-serbianc

