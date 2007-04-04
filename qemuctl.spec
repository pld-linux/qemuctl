%include	/usr/lib/rpm/macros.perl
Summary:	A controller GUI for the run-time options of QEMU computer emulator
Summary(pl.UTF-8):	GUI sterujące dla opcji uruchomieniowych emulatora komputera QEMU
Name:		qemuctl
Version:	0.2
Release:	1
License:	GPL v2
Group:		Applications/Emulators
Source0:	http://dl.sourceforge.net/qemuctl/%{name}%{version}.tar.gz
# Source0-md5:	26cad0b969fd83794940fd8ba68a1eb6
Patch0:		%{name}-Makefile.patch
URL:		http://qemuctl.sourceforge.net/
BuildRequires:  rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A controller GUI for the run-time options of QEMU computer emulator.
It can be used as a stand-alone application or as a plug-in for Qemu
Launcher. (Only x86 PC emulator is supported.)

%description -l pl.UTF-8
GUI sterujące dla opcji uruchomieniowych emulatora komputera QEMU.
Może być używane jako samodzielna aplikacja lub wtyczka dla Qemu
Launchera. Obsługiwany jest tylko emulator PC x86.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX="%{_prefix}" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
