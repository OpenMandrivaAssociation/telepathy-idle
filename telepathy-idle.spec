Name:           telepathy-idle
Version:        0.1.2
Release:        %mkrel 1
Summary:        A Telepathy connection manager implementation for the IRC protocol

Group:          Networking/Instant messaging
License:        LGPL
URL:            http://telepathy.freedesktop.org/wiki/
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig
BuildRequires: glib2-devel
BuildRequires: dbus-glib-devel
BuildRequires: openssl-devel
BuildRequires: telepathy-glib
BuildRequires: libxslt-devel libxslt-proc
Requires:	telepathy-filesystem
Requires:	telepathy-glib

%description

A Telepathy connection manager implementation for the IRC protocol.

%files
%defattr(-,root,root,-)
%{_bindir}/telepathy-idle
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.idle.service
%{_datadir}/telepathy/managers/idle.manager

#--------------------------------------------------------------------

%prep
%setup -q


%build
%configure
%make


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT
