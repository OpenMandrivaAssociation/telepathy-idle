Name:		telepathy-idle
Version:	0.1.5
Release:	%mkrel 1
Summary:	A Telepathy connection manager implementation for the IRC protocol

Group:		Networking/Instant messaging
License:	LGPLv2
URL:		http://telepathy.freedesktop.org/wiki/
Source0:	http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	pkgconfig
BuildRequires:	glib2-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	openssl-devel
BuildRequires:	libtelepathy-glib-devel
BuildRequires:	libxslt-devel libxslt-proc
BuildRequires:	python-pyxml
Requires:	telepathy-filesystem
Requires:	telepathy-glib

%description
A Telepathy connection manager implementation for the IRC protocol.

%prep
%setup -q

%build
autoreconf -f
libtoolize
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.idle.service
%{_datadir}/telepathy/managers/idle.manager
%{_libdir}/telepathy-idle
%{_mandir}/man8/telepathy-idle.8*

