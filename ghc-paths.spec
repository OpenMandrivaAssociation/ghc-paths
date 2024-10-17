%global debug_package %{nil}
%define _no_haddock 1

Summary:	Knowledge of GHC's installation directories
Name:		ghc-paths
Version:	0.1.0.8
Release:	9
License:	BSD
Group:		Development/Other
Url:		https://hackage.haskell.org/package/%{name}
Source0:	http://hackage.haskell.org/packages/archive/%{name}/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	haskell-macros
BuildRequires:	ghc-devel
Requires:	ghc
Requires(post,preun):	ghc
Requires(post,preun):	haddock

%description
Knowledge of GHC's installation directories

%files
%{_docdir}/%{name}-%{version}
%{_libdir}/%{name}-%{version}
%{_cabal_haddoc_files}
%{_cabal_rpm_deps_dir}

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%_cabal_build

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

%check
%_cabal_check

