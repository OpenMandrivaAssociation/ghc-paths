%define module ghc-paths
%define _no_haddock 1

Name: %{module}
Version: 0.1.0.6
Release: %mkrel 1
Summary: Knowledge of GHC's installation directories
Group: Development/Other
License: BSD3
Url: http://hackage.haskell.org/cgi-bin/hackage-scripts/package/%{modules}
Source: http://hackage.haskell.org/packages/archive/%{module}/%{module}-%{version}.tar.gz
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: haskell-macros >= 6.4
BuildRequires: ghc

%description
Knowledge of GHC's installation directories

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%check
%_cabal_check

%install
%_cabal_install

rm -fr %buildroot/usr/share/doc/*

%_cabal_rpm_gen_deps

%_cabal_scriptlets

%files
%defattr(-,root,root)
%_cabal_rpm_deps_dir
%{_libdir}/%{module}-%{version}
%_cabal_haddoc_files

%clean
rm -fr %buildroot

