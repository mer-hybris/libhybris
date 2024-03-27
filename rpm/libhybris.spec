#%%if 0%%{?qa_stage_devel:1}
#%%bcond_without arm_tracing
#%%bcond_without trace
#%%bcond_without debug
#%%else
%bcond_with arm_tracing
%bcond_with trace
%bcond_with debug
#%%end

Name:      libhybris
Version:   0.0.0
Release:   1%{?dist}
Summary:   Utilize Bionic-based HW adaptations on glibc systems
License:   ASL 2.0 and BSD and ISC and LGPLv2 and MIT
URL:       https://github.com/mer-hybris/libhybris
Source:    %{name}-%{version}.tar.bz2
BuildRequires: libtool
BuildRequires: pkgconfig(wayland-client)
BuildRequires: vulkan-headers
# When droid-hal-ha builds for a specific HA it should provide
# droid-hal-devel via droid-hal-%%{device}-devel package
BuildRequires: droid-hal-devel
Conflicts: mesa-llvmpipe
Obsoletes: libhybris-libOpenVG <= 0.0.5.44

%description
%{summary}.

%package devel
Summary: Common development headers for %{name}
Requires: %{name} = %{version}-%{release}
Obsoletes: libhybris-libOpenVG-devel <= 0.0.5.44

%description devel
%{summary}.

%package libEGL
Summary: EGL for hybris
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libhardware = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides: libEGL
Conflicts: mesa-llvmpipe-libEGL

%description libEGL
%{summary}.

%package libEGL-devel
Summary: EGL development headers for %{name}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libEGL = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}
Requires: pkgconfig(android-headers)
Provides: libEGL-devel
Conflicts: mesa-llvmpipe-libEGL-devel

%description libEGL-devel
%{summary}.

%package libGLESv1
Summary: OpenGL ES 1.x for %{name}
Requires: %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides: libGLESv1
Conflicts: mesa-llvmpipe-libGLESv1

%description libGLESv1
%{summary}.

%package libGLESv1-devel
Summary: OpenGL ES 1.x development library for %{name}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libGLESv1 = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}
Provides: libGLESv1-devel
Conflicts: mesa-llvmpipe-libGLESv1-devel

%description libGLESv1-devel
%{summary}.

%package libGLESv2
Summary: OpenGL ES 2.0 for %{name}
Requires: %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides: libGLESv2
Conflicts: mesa-llvmpipe-libGLESv2

%description libGLESv2
%{summary}.

%package libGLESv2-devel
Summary: OpenGL ES 2.0 development library for %{name}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libGLESv2 = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}
Provides: libGLESv2-devel
Conflicts: mesa-llvmpipe-libGLESv2-devel

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

%package libwayland-egl
Summary: Wayland EGL for %{name}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libhardware = %{version}-%{release}
Requires: %{name}-libEGL = %{version}-%{release}
Requires: %{name}-libsync = %{version}-%{release}
BuildRequires: pkgconfig(wayland-egl)
Requires: wayland-egl

%description libwayland-egl
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

%package libsf
Summary: SurfaceFlinger support helpers for %{name}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires: %{name} = %{version}-%{release}

%description libsf
%{summary}.

%package libsf-devel
Summary: SurfaceFlinger support development library for %{name}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libsf = %{version}-%{release}
Provides: libsf-devel

%description libsf-devel
%{summary}.

%package libvulkan
Summary: Vulkan support helpers for %{name}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires: %{name} = %{version}-%{release}
Provides: vulkan
Obsoletes: vulkan-loader

%description libvulkan
%{summary}.

%package tests
Summary: Tests for %{name}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libEGL = %{version}-%{release}
Requires: %{name}-libGLESv2 = %{version}-%{release}
Requires: %{name}-libhardware = %{version}-%{release}
Requires: %{name}-libsync = %{version}-%{release}
Requires: %{name}-libvibrator = %{version}-%{release}
Requires: %{name}-libvulkan = %{version}-%{release}

%description tests
%{summary}.

%package tests-upstream
Summary: Tests from upstream %{name} but not working on our side
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libEGL = %{version}-%{release}
Requires: %{name}-libGLESv2 = %{version}-%{release}
Requires: %{name}-libhardware = %{version}-%{release}
Requires: %{name}-libsync = %{version}-%{release}

%description tests-upstream
%{summary}.

%package tests-upstream-devel
Summary: Tests from upstream %{name} but not working on our side, development files
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires: %{name} = %{version}-%{release}
Requires: %{name}-tests-upstream = %{version}-%{release}

%description tests-upstream-devel
%{summary}.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}

%description doc
%{summary}.

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
cd hybris
%reconfigure \
  --enable-wayland \
  %{?with_debug:--enable-debug} \
  %{?with_trace:--enable-trace} \
%ifnarch %{ix86}
  %{?with_arm_tracing:--enable-arm-tracing} \
%endif
  --enable-property-cache \
%ifarch %{arm}
  --enable-arch=arm \
%endif
%ifarch %{ix86}
  --enable-arch=x86 \
%endif
%ifarch aarch64
  --enable-arch=arm64 \
  --with-default-hybris-ld-library-path=/usr/libexec/droid-hybris/system/lib64:/vendor/lib64:/system/lib64:/odm/lib64 \
%else
  --with-default-hybris-ld-library-path=/usr/libexec/droid-hybris/system/lib:/vendor/lib:/system/lib:/odm/lib \
%endif
  --enable-silent-rules

%make_build

%install
cd hybris
%make_install

# Remove the static libraries.
rm -f %{buildroot}/%{_libdir}/*.la %{buildroot}/%{_libdir}/libhybris/*.la
# Remove unneeded library symlink
rm -f %{buildroot}/%{_libdir}/libhybris-vulkanplatformcommon.so %{buildroot}/%{_libdir}/libvulkan.so

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m0644 AUTHORS %{buildroot}%{_docdir}/%{name}-%{version}

# For releases before Sailfish Os 4.6.0
find -H "$RPM_BUILD_ROOT" -name "*.la" -a \( -type f -o -type l \) -delete

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post libEGL -p /sbin/ldconfig
%postun libEGL -p /sbin/ldconfig

%post libGLESv1 -p /sbin/ldconfig
%postun libGLESv1 -p /sbin/ldconfig

%post libGLESv2 -p /sbin/ldconfig
%postun libGLESv2 -p /sbin/ldconfig

%post libOpenCL -p /sbin/ldconfig
%postun libOpenCL -p /sbin/ldconfig

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

%post libsf -p /sbin/ldconfig
%postun libsf -p /sbin/ldconfig

%post libvulkan -p /sbin/ldconfig
%postun libvulkan -p /sbin/ldconfig

%post tests-upstream -p /sbin/ldconfig
%postun tests-upstream -p /sbin/ldconfig

%post tests-upstream-devel -p /sbin/ldconfig
%postun tests-upstream-devel -p /sbin/ldconfig

%files
%license LICENSE.Apache2 LICENSE.BSD-2 LICENSE.BSD-3 LICENSE.BSD-4 LICENSE.ISC LICENSE.LGPLv21 LICENSE.MIT
%dir %{_libdir}/libhybris
%{_libdir}/libhybris-common.so.*
%{_libdir}/libhybris-platformcommon.so.*
%{_libdir}/libandroid-properties.so.*
%{_libdir}/libgralloc.so.*
%{_libdir}/libhwc2.so.*
%{_bindir}/getprop
%{_bindir}/setprop
%{_libdir}/libhybris/linker/*.so
%{_libdir}/libui.so.*
%{_libdir}/libwifi.so.*

%files devel
%dir %{_includedir}/hybris
%{_includedir}/hybris/input
%{_includedir}/hybris/properties
%{_includedir}/hybris/dlfcn
%{_includedir}/hybris/common
%{_includedir}/hybris/platformcommon
%{_libdir}/libhybris-common.so
%{_libdir}/libhybris-platformcommon.so
%{_libdir}/pkgconfig/libgralloc.pc
%{_libdir}/libandroid-properties.so
%{_libdir}/pkgconfig/libandroid-properties.pc
%{_includedir}/hybris/camera
%{_includedir}/hybris/surface_flinger
%{_includedir}/hybris/ui
%{_includedir}/hybris/media
%{_libdir}/libgralloc.so
%{_libdir}/libhwc2.so
%{_libdir}/libui.so
%{_libdir}/libwifi.so
%{_libdir}/pkgconfig/libwifi.pc
%{_includedir}/hybris/hwc2/hwc2_compatibility_layer.h
%{_libdir}/pkgconfig/libhwc2.pc

%files libEGL
%defattr(-,root,root,-)
%{_libdir}/libEGL.so.*
%{_libdir}/libhybris-eglplatformcommon.so.*
%{_libdir}/libhybris/eglplatform_fbdev.so
%{_libdir}/libhybris/eglplatform_null.so
%{_libdir}/libhybris/eglplatform_hwcomposer.so
%{_libdir}/libhybris-hwcomposerwindow.so.*

%files libEGL-devel
%{_includedir}/KHR
%{_includedir}/EGL
%{_includedir}/hybris/eglplatformcommon
%{_libdir}/libEGL.so
%{_libdir}/libhybris-eglplatformcommon.so
%{_libdir}/pkgconfig/egl.pc
%{_libdir}/pkgconfig/hybris-egl-platform.pc
%{_includedir}/hybris/hwcomposerwindow
%{_libdir}/libhybris-hwcomposerwindow.so
%{_libdir}/pkgconfig/hwcomposer-egl.pc

%files libGLESv1
%{_libdir}/libGLESv1_CM.so.*

%files libGLESv1-devel
%{_libdir}/libGLESv1_CM.so
%{_includedir}/GLES
%{_libdir}/pkgconfig/glesv1_cm.pc

%files libGLESv2
%{_libdir}/libGLESv2.so.2*

%files libGLESv2-devel
%{_includedir}/GLES2
%{_includedir}/GLES3
%{_libdir}/libGLESv2.so
%{_libdir}/pkgconfig/glesv2.pc

%files libOpenCL
%{_libdir}/libOpenCL.so.*

%files libOpenCL-devel
%{_includedir}/CL
%{_libdir}/libOpenCL.so
%{_libdir}/pkgconfig/OpenCL.pc

%files libwayland-egl
%{_libdir}/libhybris/eglplatform_wayland.so

%files libhardware
%{_libdir}/libhardware.so.*

%files libhardware-devel
%{_libdir}/libhardware.so
%{_libdir}/pkgconfig/libhardware.pc

%files libsync
%{_libdir}/libsync.so.*

%files libsync-devel
%{_libdir}/libsync.so
%{_libdir}/pkgconfig/libsync.pc

%files libnfc
%{_libdir}/libnfc_*.so.*

%files libnfc-devel
%{_libdir}/libnfc_*.so
%{_libdir}/pkgconfig/libnfc_*.pc

%files libvibrator
%{_libdir}/libvibrator.so.*

%files libvibrator-devel
%{_libdir}/libvibrator.so
%{_libdir}/pkgconfig/libvibrator.pc

%files libsf
%{_libdir}/libsf.so.*

%files libsf-devel
%{_libdir}/libsf.so
%{_libdir}/pkgconfig/libsf.pc

%files libvulkan
%{_libdir}/libvulkan.so.*
%{_libdir}/libhybris-vulkanplatformcommon.so.*
%{_libdir}/libhybris/vulkanplatform_null.so
%{_libdir}/libhybris/vulkanplatform_wayland.so

%files tests
%{_bindir}/test_audio
%{_bindir}/test_dlopen
%{_bindir}/test_egl
%{_bindir}/test_egl_configs
%{_bindir}/test_glesv2
%{_bindir}/test_glesv3
%{_bindir}/test_gps
%{_bindir}/test_hwcomposer
%{_bindir}/test_lights
%{_bindir}/test_nfc
%{_bindir}/test_opencl
%{_bindir}/test_sensors
%{_bindir}/test_vibrator
%{_bindir}/test_vulkan
%{_bindir}/test_wifi

%files tests-upstream
%{_libdir}/libcamera.so.*
%{_libdir}/libis.so.*
%{_libdir}/libmedia.so.*
%{_bindir}/test_camera
%{_bindir}/test_input
%{_bindir}/test_media
%{_bindir}/test_recorder
%{_bindir}/test_sf

%files tests-upstream-devel
%{_libdir}/libcamera.so
%{_libdir}/libis.so
%{_libdir}/libmedia.so
%{_libdir}/pkgconfig/libcamera.pc
%{_libdir}/pkgconfig/libis.pc
%{_libdir}/pkgconfig/libmedia.pc

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}
