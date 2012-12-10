Name:           harmonySEQ
Version:        0.16
Release:        1
Summary:        A MIDI sequencing application helpful for music composers and live artists

Group:          Sound
Source0:         http://launchpad.net/harmonyseq/stable/%{version}/+download/%{name}-%{version}.tar.gz
URL:            http://harmonyseq.wordpress.com/
License:        GPLv3

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtkmm-2.4) glibmm2.4-devel
buildrequires:	pkgconfig(alsa)
buildrequires:	pkgconfig(liblo)
BuildRequires:  shared-mime-info

%description
harmonySEQ is a MIDI sequencer for Linux. Basically, it does what any
sequencer does – it playbacks a sequence of notes. However, it is
slightly different from most of the popular software sequencers.

%prep
%setup -q

%build

%configure
make

%check

%install

make install DESTDIR=%{buildroot}
perl -pi -e 's/x-harmonyseq/x-harmonyseq;/g' \
     %{buildroot}/%{_datadir}/applications/harmonyseq.desktop
%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%attr(755,root,root) %{_bindir}/*
%docdir %{_datadir}/doc/harmonyseq
%{_datadir}/doc/harmonyseq
%{_datadir}/applications/*
%{_datadir}/harmonyseq
%{_datadir}/icons/gnome/192x192/mimetypes/*
%{_datadir}/icons/gnome/32x32/mimetypes/*
%{_datadir}/icons/gnome/48x48/mimetypes/*
%{_datadir}/icons/gnome/scalable/mimetypes/*
%{_datadir}/icons/hicolor/192x192/apps/*
%{_datadir}/icons/hicolor/32x32/apps/*
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/mime/packages/*


%changelog
* Sat Feb 18 2012 Frank Kober <emuse@mandriva.org> 0.16-1
+ Revision: 776764
- imported package harmonySEQ

