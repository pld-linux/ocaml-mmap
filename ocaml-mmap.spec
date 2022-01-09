#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	File mapping functionality for OCaml
Summary(pl.UTF-8):	Funkcjonalność odwzorowywania plików dla OCamla
Name:		ocaml-mmap
Version:	1.1.0
Release:	1
License:	LGPL v2.1 with linking exception
Group:		Libraries
#Source0Download: https://github.com/mirage/mmap/releases
Source0:	https://github.com/mirage/mmap/releases/download/v%{version}/mmap-v%{version}.tbz
# Source0-md5:	8c5d5fbc537296dc525867535fb878ba
URL:		https://github.com/mirage/mmap
BuildRequires:	ocaml >= 1:4.02.3
BuildRequires:	ocaml-dune >= 1.6
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
This project provides a Mmap.map_file functions for mapping files in
memory. It is the same as the Unix.map_file function added in OCaml >=
4.06.

This package contains files needed to run bytecode executables using
mmap library.

%description -l pl.UTF-8
Ten projekt udostępnia funkcje Mmap.map_file do odwzorowywania plików
w pamięci. Jest to odpowiednik funkcji Unix.map_file z OCamla >= 4.06.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki mmap.

%package devel
Summary:	File mapping functionality for OCaml - development part
Summary(pl.UTF-8):	Funkcjonalność odwzorowywania plików dla OCamla - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
This package contains files needed to develop OCaml programs using
mmap library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów używających
biblioteki mmap.

%prep
%setup -q -n mmap-v%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/mmap/mmap.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/mmap

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE README.md
%dir %{_libdir}/ocaml/mmap
%{_libdir}/ocaml/mmap/META
%{_libdir}/ocaml/mmap/mmap.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/mmap/mmap.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/mmap/mmap.cmi
%{_libdir}/ocaml/mmap/mmap.cmt
%{_libdir}/ocaml/mmap/mmap.cmti
%{_libdir}/ocaml/mmap/mmap.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/mmap/mmap.a
%{_libdir}/ocaml/mmap/mmap.cmx
%{_libdir}/ocaml/mmap/mmap.cmxa
%endif
%{_libdir}/ocaml/mmap/dune-package
%{_libdir}/ocaml/mmap/opam
