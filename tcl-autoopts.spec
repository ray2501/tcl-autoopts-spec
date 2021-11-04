%{!?directory:%define directory /usr}

%define pkgname autopots

Name:          tcl-autoopts
Summary:       Tcl module that automatically gives your program a command line interface
Version:       0.6.1
Release:       0
License:       MIT
Group:         Development/Libraries/Tcl
Source:        %{name}-%{version}.tar.gz
URL:           https://wiki.tcl-lang.org/page/autoopts
BuildRequires: tcl >= 8.6
Requires:      tcl >= 8.6
BuildRoot:     %{_tmppath}/%{name}-%{version}-build

%description
Autoopts is a Tcl module that automatically gives your program a command line
interface. In short, autoopts generates a command line interface based on the
arguments that your main proc takes.

%prep
%setup -q -n %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{tcl_noarchdir}/%{pkgname}%{version}
cp -f autoopts.tcl %{buildroot}%{tcl_noarchdir}/%{pkgname}%{version}
cp -f pkgIndex.tcl %{buildroot}%{tcl_noarchdir}/%{pkgname}%{version}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc AUTHORS LICENSE
%{tcl_noarchdir}/%{pkgname}%{version}

