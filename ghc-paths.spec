%global debug_package %{nil}
%define _no_haddock 1

Name:      ghc-paths
Version:   0.1.0.8
Release:   7
Summary:   Knowledge of GHC's installation directories
Group:     Development/Other
License:   BSD
Url: http://hackage.haskell.org/package/%{name}
Source0: http://hackage.haskell.org/packages/archive/%{name}/%{version}/%{name}-%{version}.tar.gz
BuildRequires: haskell-macros >= 6.4
BuildRequires: ghc
Requires: ghc
Requires(post): ghc, haddock
Requires(preun): ghc, haddock

%description
Knowledge of GHC's installation directories

%prep
%setup -q -n %{name}-%{version}

%build
%_cabal_build

%check
%_cabal_check

%install
%_cabal_install

%_cabal_rpm_gen_deps

%_cabal_scriptlets

%files
%defattr(-,root,root)
%{_docdir}/%{name}-%{version}
%_cabal_rpm_deps_dir
%{_libdir}/%{name}-%{version}
%_cabal_haddoc_files



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.0.6-3mdv2011.0
+ Revision: 610851
- rebuild

* Wed Feb 10 2010 Funda Wang <fwang@mandriva.org> 0.1.0.6-2mdv2010.1
+ Revision: 503560
- fix requirs

* Sat Dec 05 2009 Funda Wang <fwang@mandriva.org> 0.1.0.6-1mdv2010.1
+ Revision: 473961
- new version 0.1.0.6

* Sun Nov 08 2009 Olivier Thauvin <nanardon@mandriva.org> 0.1.0.5-3mdv2010.1
+ Revision: 463021
- don't build documentation (loop: haddock need ghc-path to build, ghc-path need haddock...)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Dec 05 2008 Olivier Thauvin <nanardon@mandriva.org> 0.1.0.5-1mdv2009.1
+ Revision: 310110
- import ghc-paths


