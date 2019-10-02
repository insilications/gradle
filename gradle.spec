Name     : gradle
Version  : 5.6.2
Release  : 17
URL      : https://services.gradle.org/distributions/gradle-5.6.2-bin.zip
Source0  : https://services.gradle.org/distributions/gradle-5.6.2-bin.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 CPL-1.0 LGPL-2.1 LGPL-2.1-only MIT
Requires: gradle-bin = %{version}-%{release}
Requires: gradle-data = %{version}-%{release}
Requires: gradle-license = %{version}-%{release}

%description
<img src="gradle.png" width="350px" alt="Gradle Logo" />
Gradle is a build tool with a focus on build automation and support for multi-language development. If you are building, testing, publishing, and deploying software on any platform, Gradle offers a flexible model that can support the entire development lifecycle from compiling and packaging code to publishing web sites. Gradle has been designed to support build automation across multiple languages and platforms including Java, Scala, Android, C/C++, and Groovy, and is closely integrated with development tools and continuous integration servers including Eclipse, IntelliJ, and Jenkins.

%package bin
Summary: bin components for the gradle package.
Group: Binaries
Requires: gradle-data = %{version}-%{release}
Requires: gradle-license = %{version}-%{release}

%description bin
bin components for the gradle package.


%package data
Summary: data components for the gradle package.
Group: Data

%description data
data components for the gradle package.


%package license
Summary: license components for the gradle package.
Group: Default

%description license
license components for the gradle package.


%prep
%setup -q -n gradle-5.6.2

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gradle
cp LICENSE %{buildroot}/usr/share/package-licenses/gradle/LICENSE

mkdir -p %{buildroot}/usr/share/gradle
cp -R ./* %{buildroot}/usr/share/gradle
rm %{buildroot}/usr/share/gradle/bin/gradle.bat

mkdir -p %{buildroot}/usr/bin
ln -s /usr/share/gradle/bin/gradle %{buildroot}/usr/bin/gradle

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gradle

%files data
%defattr(-,root,root,-)
/usr/share/gradle/LICENSE
/usr/share/gradle/NOTICE
/usr/share/gradle/bin/gradle
/usr/share/gradle/getting-started.html
/usr/share/gradle/init.d/readme.txt
/usr/share/gradle/lib/annotations-13.0.jar
/usr/share/gradle/lib/ant-1.9.14.jar
/usr/share/gradle/lib/ant-launcher-1.9.14.jar
/usr/share/gradle/lib/asm-7.1.jar
/usr/share/gradle/lib/asm-analysis-7.1.jar
/usr/share/gradle/lib/asm-commons-7.1.jar
/usr/share/gradle/lib/asm-tree-7.1.jar
/usr/share/gradle/lib/commons-compress-1.18.jar
/usr/share/gradle/lib/commons-io-2.6.jar
/usr/share/gradle/lib/commons-lang-2.6.jar
/usr/share/gradle/lib/failureaccess-1.0.1.jar
/usr/share/gradle/lib/fastutil-8.2.1-min.jar
/usr/share/gradle/lib/gradle-api-metadata-5.6.2.jar
/usr/share/gradle/lib/gradle-base-services-5.6.2.jar
/usr/share/gradle/lib/gradle-base-services-groovy-5.6.2.jar
/usr/share/gradle/lib/gradle-bootstrap-5.6.2.jar
/usr/share/gradle/lib/gradle-build-cache-5.6.2.jar
/usr/share/gradle/lib/gradle-build-cache-packaging-5.6.2.jar
/usr/share/gradle/lib/gradle-build-option-5.6.2.jar
/usr/share/gradle/lib/gradle-cli-5.6.2.jar
/usr/share/gradle/lib/gradle-core-5.6.2.jar
/usr/share/gradle/lib/gradle-core-api-5.6.2.jar
/usr/share/gradle/lib/gradle-docs-5.6.2.jar
/usr/share/gradle/lib/gradle-execution-5.6.2.jar
/usr/share/gradle/lib/gradle-file-collections-5.6.2.jar
/usr/share/gradle/lib/gradle-files-5.6.2.jar
/usr/share/gradle/lib/gradle-hashing-5.6.2.jar
/usr/share/gradle/lib/gradle-installation-beacon-5.6.2.jar
/usr/share/gradle/lib/gradle-instant-execution-5.6.2.jar
/usr/share/gradle/lib/gradle-jvm-services-5.6.2.jar
/usr/share/gradle/lib/gradle-kotlin-dsl-5.6.2.jar
/usr/share/gradle/lib/gradle-kotlin-dsl-tooling-models-5.6.2.jar
/usr/share/gradle/lib/gradle-launcher-5.6.2.jar
/usr/share/gradle/lib/gradle-logging-5.6.2.jar
/usr/share/gradle/lib/gradle-messaging-5.6.2.jar
/usr/share/gradle/lib/gradle-model-core-5.6.2.jar
/usr/share/gradle/lib/gradle-model-groovy-5.6.2.jar
/usr/share/gradle/lib/gradle-native-5.6.2.jar
/usr/share/gradle/lib/gradle-persistent-cache-5.6.2.jar
/usr/share/gradle/lib/gradle-pineapple-5.6.2.jar
/usr/share/gradle/lib/gradle-process-services-5.6.2.jar
/usr/share/gradle/lib/gradle-resources-5.6.2.jar
/usr/share/gradle/lib/gradle-runtime-api-info-5.6.2.jar
/usr/share/gradle/lib/gradle-snapshots-5.6.2.jar
/usr/share/gradle/lib/gradle-tooling-api-5.6.2.jar
/usr/share/gradle/lib/gradle-worker-processes-5.6.2.jar
/usr/share/gradle/lib/gradle-wrapper-5.6.2.jar
/usr/share/gradle/lib/groovy-all-1.3-2.5.4.jar
/usr/share/gradle/lib/guava-27.1-android.jar
/usr/share/gradle/lib/jansi-1.17.1.jar
/usr/share/gradle/lib/javax.inject-1.jar
/usr/share/gradle/lib/jcl-over-slf4j-1.7.25.jar
/usr/share/gradle/lib/jsr305-3.0.2.jar
/usr/share/gradle/lib/jul-to-slf4j-1.7.25.jar
/usr/share/gradle/lib/kotlin-compiler-embeddable-1.3.41-patched-for-gradle-5.6.2.jar
/usr/share/gradle/lib/kotlin-reflect-1.3.41.jar
/usr/share/gradle/lib/kotlin-sam-with-receiver-compiler-plugin-1.3.41.jar
/usr/share/gradle/lib/kotlin-script-runtime-1.3.41.jar
/usr/share/gradle/lib/kotlin-scripting-compiler-embeddable-1.3.41.jar
/usr/share/gradle/lib/kotlin-scripting-compiler-impl-embeddable-1.3.41.jar
/usr/share/gradle/lib/kotlin-stdlib-1.3.41.jar
/usr/share/gradle/lib/kotlin-stdlib-common-1.3.41.jar
/usr/share/gradle/lib/kotlin-stdlib-jdk7-1.3.41.jar
/usr/share/gradle/lib/kotlin-stdlib-jdk8-1.3.41.jar
/usr/share/gradle/lib/kotlinx-metadata-jvm-0.1.0.jar
/usr/share/gradle/lib/kryo-2.24.0.jar
/usr/share/gradle/lib/log4j-over-slf4j-1.7.25.jar
/usr/share/gradle/lib/minlog-1.2.jar
/usr/share/gradle/lib/native-platform-0.18.jar
/usr/share/gradle/lib/native-platform-freebsd-amd64-libcpp-0.18.jar
/usr/share/gradle/lib/native-platform-freebsd-amd64-libstdcpp-0.18.jar
/usr/share/gradle/lib/native-platform-freebsd-i386-libcpp-0.18.jar
/usr/share/gradle/lib/native-platform-freebsd-i386-libstdcpp-0.18.jar
/usr/share/gradle/lib/native-platform-linux-aarch64-0.18.jar
/usr/share/gradle/lib/native-platform-linux-aarch64-ncurses5-0.18.jar
/usr/share/gradle/lib/native-platform-linux-amd64-0.18.jar
/usr/share/gradle/lib/native-platform-linux-amd64-ncurses5-0.18.jar
/usr/share/gradle/lib/native-platform-linux-amd64-ncurses6-0.18.jar
/usr/share/gradle/lib/native-platform-linux-i386-0.18.jar
/usr/share/gradle/lib/native-platform-linux-i386-ncurses5-0.18.jar
/usr/share/gradle/lib/native-platform-linux-i386-ncurses6-0.18.jar
/usr/share/gradle/lib/native-platform-osx-amd64-0.18.jar
/usr/share/gradle/lib/native-platform-windows-amd64-0.18.jar
/usr/share/gradle/lib/native-platform-windows-amd64-min-0.18.jar
/usr/share/gradle/lib/native-platform-windows-i386-0.18.jar
/usr/share/gradle/lib/native-platform-windows-i386-min-0.18.jar
/usr/share/gradle/lib/objenesis-2.6.jar
/usr/share/gradle/lib/plugins/aether-api-1.13.1.jar
/usr/share/gradle/lib/plugins/aether-connector-wagon-1.13.1.jar
/usr/share/gradle/lib/plugins/aether-impl-1.13.1.jar
/usr/share/gradle/lib/plugins/aether-spi-1.13.1.jar
/usr/share/gradle/lib/plugins/aether-util-1.13.1.jar
/usr/share/gradle/lib/plugins/apiguardian-api-1.0.0.jar
/usr/share/gradle/lib/plugins/asm-util-7.1.jar
/usr/share/gradle/lib/plugins/aws-java-sdk-core-1.11.407.jar
/usr/share/gradle/lib/plugins/aws-java-sdk-kms-1.11.407.jar
/usr/share/gradle/lib/plugins/aws-java-sdk-s3-1.11.407.jar
/usr/share/gradle/lib/plugins/bcpg-jdk15on-1.61.jar
/usr/share/gradle/lib/plugins/bcprov-jdk15on-1.61.jar
/usr/share/gradle/lib/plugins/biz.aQute.bndlib-4.0.0.jar
/usr/share/gradle/lib/plugins/bsh-2.0b6.jar
/usr/share/gradle/lib/plugins/commons-codec-1.11.jar
/usr/share/gradle/lib/plugins/dd-plist-1.21.jar
/usr/share/gradle/lib/plugins/google-api-client-1.25.0.jar
/usr/share/gradle/lib/plugins/google-api-services-storage-v1-rev136-1.25.0.jar
/usr/share/gradle/lib/plugins/google-http-client-1.25.0.jar
/usr/share/gradle/lib/plugins/google-http-client-jackson2-1.25.0.jar
/usr/share/gradle/lib/plugins/google-oauth-client-1.25.0.jar
/usr/share/gradle/lib/plugins/gradle-announce-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-antlr-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-build-cache-http-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-build-comparison-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-build-init-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-build-profile-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-code-quality-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-composite-builds-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-dependency-management-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-diagnostics-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-ear-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-ide-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-ide-native-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-ide-play-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-ivy-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-jacoco-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-javascript-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-kotlin-dsl-provider-plugins-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-kotlin-dsl-tooling-builders-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-language-groovy-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-language-java-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-language-jvm-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-language-native-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-language-scala-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-maven-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-osgi-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-platform-base-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-platform-jvm-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-platform-native-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-platform-play-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-plugin-development-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-plugin-use-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-plugins-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-publish-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-reporting-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-resources-gcs-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-resources-http-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-resources-s3-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-resources-sftp-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-scala-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-signing-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-test-kit-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-testing-base-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-testing-junit-platform-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-testing-jvm-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-testing-native-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-tooling-api-builders-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-tooling-native-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-version-control-5.6.2.jar
/usr/share/gradle/lib/plugins/gradle-workers-5.6.2.jar
/usr/share/gradle/lib/plugins/gson-2.8.5.jar
/usr/share/gradle/lib/plugins/hamcrest-core-1.3.jar
/usr/share/gradle/lib/plugins/httpclient-4.5.6.jar
/usr/share/gradle/lib/plugins/httpcore-4.4.10.jar
/usr/share/gradle/lib/plugins/ion-java-1.0.2.jar
/usr/share/gradle/lib/plugins/ivy-2.3.0.jar
/usr/share/gradle/lib/plugins/jackson-annotations-2.9.8.jar
/usr/share/gradle/lib/plugins/jackson-core-2.9.8.jar
/usr/share/gradle/lib/plugins/jackson-databind-2.9.8.jar
/usr/share/gradle/lib/plugins/jatl-0.2.3.jar
/usr/share/gradle/lib/plugins/jaxb-impl-2.3.1.jar
/usr/share/gradle/lib/plugins/jcifs-1.3.17.jar
/usr/share/gradle/lib/plugins/jcommander-1.72.jar
/usr/share/gradle/lib/plugins/jmespath-java-1.11.407.jar
/usr/share/gradle/lib/plugins/joda-time-2.10.jar
/usr/share/gradle/lib/plugins/jsch-0.1.54.jar
/usr/share/gradle/lib/plugins/junit-4.12.jar
/usr/share/gradle/lib/plugins/junit-platform-commons-1.3.1.jar
/usr/share/gradle/lib/plugins/junit-platform-engine-1.3.1.jar
/usr/share/gradle/lib/plugins/junit-platform-launcher-1.3.1.jar
/usr/share/gradle/lib/plugins/jzlib-1.1.3.jar
/usr/share/gradle/lib/plugins/maven-aether-provider-3.0.4.jar
/usr/share/gradle/lib/plugins/maven-artifact-3.0.4.jar
/usr/share/gradle/lib/plugins/maven-compat-3.0.4.jar
/usr/share/gradle/lib/plugins/maven-core-3.0.4.jar
/usr/share/gradle/lib/plugins/maven-model-3.0.4.jar
/usr/share/gradle/lib/plugins/maven-model-builder-3.0.4.jar
/usr/share/gradle/lib/plugins/maven-plugin-api-3.0.4.jar
/usr/share/gradle/lib/plugins/maven-repository-metadata-3.0.4.jar
/usr/share/gradle/lib/plugins/maven-settings-3.0.4.jar
/usr/share/gradle/lib/plugins/maven-settings-builder-3.0.4.jar
/usr/share/gradle/lib/plugins/nekohtml-1.9.22.jar
/usr/share/gradle/lib/plugins/opentest4j-1.1.1.jar
/usr/share/gradle/lib/plugins/org.eclipse.jgit-5.0.3.201809091024-r.jar
/usr/share/gradle/lib/plugins/plexus-cipher-1.7.jar
/usr/share/gradle/lib/plugins/plexus-classworlds-2.5.1.jar
/usr/share/gradle/lib/plugins/plexus-component-annotations-1.5.5.jar
/usr/share/gradle/lib/plugins/plexus-container-default-1.7.1.jar
/usr/share/gradle/lib/plugins/plexus-interpolation-1.14.jar
/usr/share/gradle/lib/plugins/plexus-sec-dispatcher-1.3.jar
/usr/share/gradle/lib/plugins/plexus-utils-3.1.0.jar
/usr/share/gradle/lib/plugins/pmaven-common-0.8-20100325.jar
/usr/share/gradle/lib/plugins/pmaven-groovy-0.8-20100325.jar
/usr/share/gradle/lib/plugins/rhino-1.7.10.jar
/usr/share/gradle/lib/plugins/simple-4.1.21.jar
/usr/share/gradle/lib/plugins/snakeyaml-1.17.jar
/usr/share/gradle/lib/plugins/testng-6.3.1.jar
/usr/share/gradle/lib/plugins/wagon-file-3.0.0.jar
/usr/share/gradle/lib/plugins/wagon-http-3.0.0.jar
/usr/share/gradle/lib/plugins/wagon-http-shared-3.0.0.jar
/usr/share/gradle/lib/plugins/wagon-provider-api-3.0.0.jar
/usr/share/gradle/lib/plugins/xbean-reflect-3.7.jar
/usr/share/gradle/lib/plugins/xercesImpl-2.12.0.jar
/usr/share/gradle/lib/slf4j-api-1.7.25.jar
/usr/share/gradle/lib/trove4j-1.0.20181211.jar
/usr/share/gradle/lib/xml-apis-1.4.01.jar
/usr/share/gradle/media/gradle-icon-128x128.png
/usr/share/gradle/media/gradle-icon-16x16.png
/usr/share/gradle/media/gradle-icon-24x24.png
/usr/share/gradle/media/gradle-icon-256x256.png
/usr/share/gradle/media/gradle-icon-32x32.png
/usr/share/gradle/media/gradle-icon-48x48.png
/usr/share/gradle/media/gradle-icon-512x512.png
/usr/share/gradle/media/gradle-icon-64x64.png
/usr/share/gradle/media/gradle.icns

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gradle/LICENSE
