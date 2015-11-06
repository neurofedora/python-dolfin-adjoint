%define modname dolfin-adjoint
%define pyname  dolfin_adjoint
%define gitcommit 671a628be858

Name:           python-%{modname}
Version:	1.6.0
Release:	1%{?dist}
License:	LGPL-3.0
Summary:	Discrete adjoint and tangent linear computations for dolfin
Url:		http://dolfin-adjoint.org
Source:		%{modname}-%{version}.tar.bz2
BuildRequires:  python-devel
Requires:       python-dolfin-openmpi = %{version}
Requires:       python-libadjoint-openmpi = %{version}

%description
The dolfin-adjoint project automatically derives the discrete adjoint 
and tangent linear models from a forward model written in the Python 
interface to dolfin.

%prep
%setup -q -n %{modname}-%{modname}-%{gitcommit}

%build
%py2_build

%install
py2_install

%files
%doc AUTHORS LICENSE README
%{python2_sitelib}/*


%changelog
* Fri Nov  6 2015 Adrian Alves <alvesadrian@fedoraproject.org> 1.6.0-1
- Initial build
