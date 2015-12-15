Name:      libhybris
Version:   0.0.0
Release:   1%{?dist}
Summary:   Utilize Bionic-based HW adaptations on glibc systems

Group:     System/Libraries
License:   ASL 2.0
URL:       https://github.com/libhybris/libhybris
Source:    %{name}-%{version}.tar.bz2
BuildRequires: libtool
BuildRequires: pkgconfig(wayland-client)
# When droid-hal-ha builds for a specific HA it should provide
# droid-hal-devel via droid-hal-%{device}-devel package
BuildRequires: droid-hal-devel
Conflicts: mesa-llvmpipe

%description
%{summary}.

%package devel
Summary: Common development headers for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
%{summary}.

%package libEGL
Summary: EGL for hybris
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libhardware = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides: libEGL
Provides: libEGL.so.1

%description libEGL
%{summary}.

%package libEGL-devel
Summary: EGL development headers for %{name}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libEGL = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}
Requires: pkgconfig(android-headers)
Provides: libEGL-devel

%description libEGL-devel
%{summary}.

%package libGLESv1
Summary: OpenGL ES 1.x for %{name}
Requires: %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides: libGLESv1
Provides: libGLES_CM.so.1

%description libGLESv1
%{summary}.

%package libGLESv1-devel
Summary: OpenGL ES 1.x development library for %{name}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libGLESv1 = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}
Provides: libGLESv1-devel

%description libGLESv1-devel
%{summary}.

%package libGLESv2
Summary: OpenGL ES 2.0 for %{name}
Requires: %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides: libGLESv2
Provides: libGLESv2.so.2

%description libGLESv2
%{summary}.

%package libGLESv2-devel
Summary: OpenGL ES 2.0 development library for %{name}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libGLESv2 = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}
Provides: libGLESv2-devel

%description libGLESv2-devel
%{summary}.

%package libOpenCL
Summary: OpenCL for %{name}
Requires: %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides: libOpenCL

%description libOpenCL
%{summary}.

%package libOpenCL-devel
Summary: OpenCL development library for %{name}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libOpenCL = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}
Provides: libOpenCL-devel

%description libOpenCL-devel
%{summary}.

%package libOpenVG
Summary: OpenVG for %{name}
Requires: %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides: libOpenVG

%description libOpenVG
%{summary}.

%package libOpenVG-devel
Summary: OpenVG development library for %{name}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libOpenVG = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}
Provides: libOpenVG-devel

%description libOpenVG-devel
%{summary}.

%package libwayland-egl
Summary: Wayland EGL for %{name}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libhardware = %{version}-%{release}
Requires: %{name}-libEGL = %{version}-%{release}
Requires: %{name}-libsync = %{version}-%{release}
Provides: libwayland-egl

%description libwayland-egl
%{summary}.

%package libwayland-egl-devel
Summary: Wayland EGL development library for %{name}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libwayland-egl = %{version}-%{release}
Provides: libwayland-egl-devel

%description libwayland-egl-devel
%{summary}.

%package libhardware
Summary: libhardware for %{name}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires: %{name} = %{version}-%{release}

%description libhardware
%{summary}.

%package libhardware-devel
Summary: libhardware development library for %{name}
Requires: %{name}-devel = %{version}-%{release}
Requires: %{name}-libhardware = %{version}-%{release}

%description libhardware-devel
%{summary}.

%package libsync
Summary: libsync for %{name}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires: %{name} = %{version}-%{release}

%description libsync
%{summary}.

%package libsync-devel
Summary: libsync development library for %{name}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libsync = %{version}-%{release}

%description libsync-devel
%{summary}.

%package libnfc
Summary: Near Field Communication for %{name}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires: %{name} = %{version}-%{release}

%description libnfc
%{summary}.

%package libnfc-devel
Summary: Near Field Communication development library for %{name}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libnfc = %{version}-%{release}

%description libnfc-devel
%{summary}.

%package libvibrator
Summary: Vibrator for %{name}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires: %{name} = %{version}-%{release}

%description libvibrator
%{summary}.

%package libvibrator-devel
Summary: Vibrator development library for %{name}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libvibrator = %{version}-%{release}

%description libvibrator-devel
%{summary}.

%package tests
Summary: Tests for %{name}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libEGL = %{version}-%{release}
Requires: %{name}-libGLESv2 = %{version}-%{release}
Requires: %{name}-libhardware = %{version}-%{release}
Requires: %{name}-libsync = %{version}-%{release}
Requires: %{name}-libvibrator = %{version}-%{release}


%description tests
%{summary}.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
cd hybris
autoreconf -v -f -i
%configure \
  --enable-wayland \
  %{!?qa_stage_devel:--enable-debug} \
  %{!?qa_stage_devel:--enable-trace} \
  --with-android-headers=/usr/lib/droid-devel/droid-headers \
%ifarch %{arm}
  --enable-arch=arm \
%endif
%ifarch %{ix86}
  --enable-arch=x86 \
%endif
  --enable-property-cache \
  --with-default-hybris-ld-library-path=/usr/libexec/droid-hybris/system/lib:/vendor/lib:/system/lib

make

%install
rm -rf $RPM_BUILD_ROOT
cd hybris
make install DESTDIR=$RPM_BUILD_ROOT

# Remove the static libraries.
rm %{buildroot}/%{_libdir}/*.la %{buildroot}/%{_libdir}/libhybris/*.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post libEGL -p /sbin/ldconfig
%postun libEGL -p /sbin/ldconfig

%post libGLESv1 -p /sbin/ldconfig
%postun libGLESv1 -p /sbin/ldconfig

%post libGLESv2 -p /sbin/ldconfig
%postun libGLESv2 -p /sbin/ldconfig

%post libwayland-egl -p /sbin/ldconfig
%postun libwayland-egl -p /sbin/ldconfig

%post libhardware -p /sbin/ldconfig
%postun libhardware -p /sbin/ldconfig

%post libsync -p /sbin/ldconfig
%postun libsync -p /sbin/ldconfig

%post libnfc -p /sbin/ldconfig
%postun libnfc -p /sbin/ldconfig

%post libvibrator -p /sbin/ldconfig
%postun libvibrator -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc hybris/AUTHORS hybris/COPYING
%{_libdir}/libhybris-common.so.*
%{_libdir}/libandroid-properties.so.*
%{_bindir}/getprop
%{_bindir}/setprop

%files devel
%defattr(-,root,root,-)
%{_includedir}/hybris/input/*.h
%{_includedir}/hybris/properties/properties.h
%{_includedir}/hybris/dlfcn/dlfcn.h
%{_includedir}/hybris/common/binding.h
%{_includedir}/hybris/common/dlfcn.h
%{_includedir}/hybris/common/floating_point_abi.h
%{_libdir}/libhybris-common.so
%{_libdir}/libandroid-properties.so
%{_libdir}/pkgconfig/libandroid-properties.pc
%{_includedir}/hybris/camera/*.h
%{_includedir}/hybris/surface_flinger/surface_flinger_compatibility_layer.h
%{_includedir}/hybris/ui/ui_compatibility_layer.h


%files libEGL
%defattr(-,root,root,-)
%{_libdir}/libEGL.so.*
%{_libdir}/libhybris-eglplatformcommon.so.*
%{_libdir}/libhybris/eglplatform_fbdev.so
%{_libdir}/libhybris/eglplatform_null.so
%{_libdir}/libhybris/eglplatform_hwcomposer.so
%{_libdir}/libhybris-hwcomposerwindow.so.1
%{_libdir}/libhybris-hwcomposerwindow.so.1.0.0

%files libEGL-devel
%defattr(-,root,root,-)
%{_includedir}/KHR/*.h
%{_includedir}/EGL/*.h
%{_includedir}/hybris/eglplatformcommon/*.h
%{_libdir}/libEGL.so
%{_libdir}/libhybris-eglplatformcommon.so
%{_libdir}/pkgconfig/egl.pc
%{_libdir}/pkgconfig/hybris-egl-platform.pc
%{_includedir}/hybris/hwcomposerwindow/hwcomposer.h
%{_includedir}/hybris/hwcomposerwindow/hwcomposer_window.h
%{_libdir}/libhybris-hwcomposerwindow.so
%{_libdir}/pkgconfig/hwcomposer-egl.pc

%files libGLESv1
%defattr(-,root,root,-)
%{_libdir}/libGLESv1_CM.so.*

%files libGLESv1-devel
%defattr(-,root,root,-)
%{_libdir}/libGLESv1_CM.so
%{_includedir}/GLES/*.h
%{_libdir}/pkgconfig/glesv1_cm.pc

%files libGLESv2
%defattr(-,root,root,-)
%{_libdir}/libGLESv2.so.2*

%files libGLESv2-devel
%defattr(-,root,root,-)
%{_includedir}/GLES2/*.h
%{_libdir}/libGLESv2.so
%{_libdir}/pkgconfig/glesv2.pc

%files libOpenCL
%defattr(-,root,root,-)
# We don't have implementation of OpenCL atm.

%files libOpenCL-devel
%defattr(-,root,root,-)
%{_includedir}/CL/*.h
%{_includedir}/CL/*.hpp

%files libOpenVG
%defattr(-,root,root,-)
# We don't have implementation of OpenVG atm.

%files libOpenVG-devel
%defattr(-,root,root,-)
%{_includedir}/VG/*.h

%files libwayland-egl
%defattr(-,root,root,-)
%{_libdir}/libhybris/eglplatform_wayland.so
%{_libdir}/libwayland-egl.so.*

%files libwayland-egl-devel
%defattr(-,root,root,-)
%{_libdir}/libwayland-egl.so
%{_libdir}/pkgconfig/wayland-egl.pc

%files libhardware
%defattr(-,root,root,-)
%{_libdir}/libhardware.so.*

%files libhardware-devel
%defattr(-,root,root,-)
%{_libdir}/libhardware.so
%{_libdir}/pkgconfig/libhardware.pc

%files libsync
%defattr(-,root,root,-)
%{_libdir}/libsync.so.*

%files libsync-devel
%defattr(-,root,root,-)
%{_libdir}/libsync.so
%{_libdir}/pkgconfig/libsync.pc

%files libnfc
%defattr(-,root,root,-)
%{_libdir}/libnfc_*.so.*

%files libnfc-devel
%defattr(-,root,root,-)
%{_libdir}/libnfc_*.so
%{_libdir}/pkgconfig/libnfc_*.pc

%files libvibrator
%defattr(-,root,root,-)
%{_libdir}/libvibrator.so.*

%files libvibrator-devel
%defattr(-,root,root,-)
%{_libdir}/libvibrator.so
%{_libdir}/pkgconfig/libvibrator.pc

%files tests
%defattr(-,root,root,-)
%{_bindir}/test_*
