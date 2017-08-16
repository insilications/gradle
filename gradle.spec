Name     : gradle
Version  : 3.5
Release  : 11
URL      : https://github.com/gradle/
Source0  : https://github.com/gradle/gradle/archive/v3.5.0.tar.gz
Source1  : all-released-versions.json
Source2  : gradle-script.sh
Patch0   : 0001-Change-Gradle-build-to-use-local-Maven-repo.patch
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 LGPL-2.1
BuildRequires: gradle
BuildRequires: gradle-dep
BuildRequires: openjdk-dev
BuildRequires: ca-certs
BuildRequires: procps-ng

Requires: gradle-dep
Requires: openjdk-dev
Requires: ca-certs
Requires: procps-ng

%description
You can add .gradle init scripts to this directory. Each one is executed at the start of the build.

%prep
%setup -q -n gradle-3.5.0
%patch0 -p1

%build
mkdir -p %{buildroot}/.m2
mkdir /builddir/build/BUILD/gradle-3.5.0/build
cp -R /usr/share/gradle/.m2/* %{buildroot}/.m2
ln -s %{buildroot}/.m2 /builddir/.m2
cp %{SOURCE1} /builddir/build/BUILD/gradle-3.5.0/build
gradle -Pgradle_installPath=/tmp/gradle -PfinalRelease=true install

%install
mkdir -p %{buildroot}/usr/share/gradle
cp -R /tmp/gradle/* %{buildroot}/usr/share/gradle
# Add helper script
mkdir -p %{buildroot}/usr/bin
cp %{SOURCE2} %{buildroot}/usr/bin/gradle
chmod 755 %{buildroot}/usr/bin/gradle

# Remove unnecessary bat file
rm %{buildroot}/usr/share/gradle/bin/gradle.bat

%files
%defattr(-,root,root,-)
/usr/bin/gradle
/usr/share/gradle/LICENSE
/usr/share/gradle/NOTICE
/usr/share/gradle/bin/gradle
/usr/share/gradle/getting-started.html
/usr/share/gradle/init.d/readme.txt
/usr/share/gradle/lib/annotations-13.0.jar
/usr/share/gradle/lib/ant-1.9.6.jar
/usr/share/gradle/lib/ant-launcher-1.9.6.jar
/usr/share/gradle/lib/asm-all-5.1.jar
/usr/share/gradle/lib/commons-collections-3.2.2.jar
/usr/share/gradle/lib/commons-io-2.2.jar
/usr/share/gradle/lib/commons-lang-2.6.jar
/usr/share/gradle/lib/dom4j-1.6.1.jar
/usr/share/gradle/lib/gradle-base-services-3.5.jar
/usr/share/gradle/lib/gradle-base-services-groovy-3.5.jar
/usr/share/gradle/lib/gradle-cli-3.5.jar
/usr/share/gradle/lib/gradle-core-3.5.jar
/usr/share/gradle/lib/gradle-docs-3.5.jar
/usr/share/gradle/lib/gradle-installation-beacon-3.5.jar
/usr/share/gradle/lib/gradle-jvm-services-3.5.jar
/usr/share/gradle/lib/gradle-launcher-3.5.jar
/usr/share/gradle/lib/gradle-logging-3.5.jar
/usr/share/gradle/lib/gradle-messaging-3.5.jar
/usr/share/gradle/lib/gradle-model-core-3.5.jar
/usr/share/gradle/lib/gradle-model-groovy-3.5.jar
/usr/share/gradle/lib/gradle-native-3.5.jar
/usr/share/gradle/lib/gradle-open-api-3.5.jar
/usr/share/gradle/lib/gradle-process-services-3.5.jar
/usr/share/gradle/lib/gradle-resources-3.5.jar
/usr/share/gradle/lib/gradle-runtime-api-info-3.5.jar
/usr/share/gradle/lib/gradle-script-kotlin-0.8.0.jar
/usr/share/gradle/lib/gradle-tooling-api-3.5.jar
/usr/share/gradle/lib/gradle-ui-3.5.jar
/usr/share/gradle/lib/gradle-version-info-3.5.jar
/usr/share/gradle/lib/gradle-wrapper-3.5.jar
/usr/share/gradle/lib/groovy-all-2.4.10.jar
/usr/share/gradle/lib/guava-jdk5-17.0.jar
/usr/share/gradle/lib/jansi-1.14.jar
/usr/share/gradle/lib/javax.inject-1.jar
/usr/share/gradle/lib/jaxen-1.1.jar
/usr/share/gradle/lib/jcip-annotations-1.0.jar
/usr/share/gradle/lib/jcl-over-slf4j-1.7.10.jar
/usr/share/gradle/lib/jul-to-slf4j-1.7.10.jar
/usr/share/gradle/lib/kotlin-compiler-embeddable-1.1.0.jar
/usr/share/gradle/lib/kotlin-reflect-1.1.0.jar
/usr/share/gradle/lib/kotlin-stdlib-1.1.0.jar
/usr/share/gradle/lib/kryo-2.20.jar
/usr/share/gradle/lib/log4j-over-slf4j-1.7.10.jar
/usr/share/gradle/lib/minlog-1.2.jar
/usr/share/gradle/lib/native-platform-0.14.jar
/usr/share/gradle/lib/native-platform-freebsd-amd64-libcpp-0.14.jar
/usr/share/gradle/lib/native-platform-freebsd-amd64-libstdcpp-0.14.jar
/usr/share/gradle/lib/native-platform-freebsd-i386-libcpp-0.14.jar
/usr/share/gradle/lib/native-platform-freebsd-i386-libstdcpp-0.14.jar
/usr/share/gradle/lib/native-platform-linux-amd64-0.14.jar
/usr/share/gradle/lib/native-platform-linux-amd64-ncurses5-0.14.jar
/usr/share/gradle/lib/native-platform-linux-amd64-ncurses6-0.14.jar
/usr/share/gradle/lib/native-platform-linux-i386-0.14.jar
/usr/share/gradle/lib/native-platform-linux-i386-ncurses5-0.14.jar
/usr/share/gradle/lib/native-platform-linux-i386-ncurses6-0.14.jar
/usr/share/gradle/lib/native-platform-osx-amd64-0.14.jar
/usr/share/gradle/lib/native-platform-osx-i386-0.14.jar
/usr/share/gradle/lib/native-platform-windows-amd64-0.14.jar
/usr/share/gradle/lib/native-platform-windows-i386-0.14.jar
/usr/share/gradle/lib/objenesis-1.2.jar
/usr/share/gradle/lib/plugins/aether-api-1.13.1.jar
/usr/share/gradle/lib/plugins/aether-connector-wagon-1.13.1.jar
/usr/share/gradle/lib/plugins/aether-impl-1.13.1.jar
/usr/share/gradle/lib/plugins/aether-spi-1.13.1.jar
/usr/share/gradle/lib/plugins/aether-util-1.13.1.jar
/usr/share/gradle/lib/plugins/aws-java-sdk-core-1.11.6.jar
/usr/share/gradle/lib/plugins/aws-java-sdk-kms-1.11.6.jar
/usr/share/gradle/lib/plugins/aws-java-sdk-s3-1.11.6.jar
/usr/share/gradle/lib/plugins/bcpg-jdk15on-1.51.jar
/usr/share/gradle/lib/plugins/bcprov-jdk15on-1.51.jar
/usr/share/gradle/lib/plugins/biz.aQute.bndlib-3.2.0.jar
/usr/share/gradle/lib/plugins/bsh-2.0b4.jar
/usr/share/gradle/lib/plugins/commons-cli-1.2.jar
/usr/share/gradle/lib/plugins/commons-codec-1.6.jar
/usr/share/gradle/lib/plugins/core-3.1.1.jar
/usr/share/gradle/lib/plugins/geronimo-annotation_1.0_spec-1.0.jar
/usr/share/gradle/lib/plugins/gradle-announce-3.5.jar
/usr/share/gradle/lib/plugins/gradle-antlr-3.5.jar
/usr/share/gradle/lib/plugins/gradle-build-cache-http-3.5.jar
/usr/share/gradle/lib/plugins/gradle-build-comparison-3.5.jar
/usr/share/gradle/lib/plugins/gradle-build-init-3.5.jar
/usr/share/gradle/lib/plugins/gradle-code-quality-3.5.jar
/usr/share/gradle/lib/plugins/gradle-composite-builds-3.5.jar
/usr/share/gradle/lib/plugins/gradle-dependency-management-3.5.jar
/usr/share/gradle/lib/plugins/gradle-diagnostics-3.5.jar
/usr/share/gradle/lib/plugins/gradle-ear-3.5.jar
/usr/share/gradle/lib/plugins/gradle-ide-3.5.jar
/usr/share/gradle/lib/plugins/gradle-ide-native-3.5.jar
/usr/share/gradle/lib/plugins/gradle-ide-play-3.5.jar
/usr/share/gradle/lib/plugins/gradle-ivy-3.5.jar
/usr/share/gradle/lib/plugins/gradle-jacoco-3.5.jar
/usr/share/gradle/lib/plugins/gradle-javascript-3.5.jar
/usr/share/gradle/lib/plugins/gradle-jetty-3.5.jar
/usr/share/gradle/lib/plugins/gradle-language-groovy-3.5.jar
/usr/share/gradle/lib/plugins/gradle-language-java-3.5.jar
/usr/share/gradle/lib/plugins/gradle-language-jvm-3.5.jar
/usr/share/gradle/lib/plugins/gradle-language-native-3.5.jar
/usr/share/gradle/lib/plugins/gradle-language-scala-3.5.jar
/usr/share/gradle/lib/plugins/gradle-maven-3.5.jar
/usr/share/gradle/lib/plugins/gradle-osgi-3.5.jar
/usr/share/gradle/lib/plugins/gradle-platform-base-3.5.jar
/usr/share/gradle/lib/plugins/gradle-platform-jvm-3.5.jar
/usr/share/gradle/lib/plugins/gradle-platform-native-3.5.jar
/usr/share/gradle/lib/plugins/gradle-platform-play-3.5.jar
/usr/share/gradle/lib/plugins/gradle-plugin-development-3.5.jar
/usr/share/gradle/lib/plugins/gradle-plugin-use-3.5.jar
/usr/share/gradle/lib/plugins/gradle-plugins-3.5.jar
/usr/share/gradle/lib/plugins/gradle-publish-3.5.jar
/usr/share/gradle/lib/plugins/gradle-reporting-3.5.jar
/usr/share/gradle/lib/plugins/gradle-resources-http-3.5.jar
/usr/share/gradle/lib/plugins/gradle-resources-s3-3.5.jar
/usr/share/gradle/lib/plugins/gradle-resources-sftp-3.5.jar
/usr/share/gradle/lib/plugins/gradle-scala-3.5.jar
/usr/share/gradle/lib/plugins/gradle-signing-3.5.jar
/usr/share/gradle/lib/plugins/gradle-test-kit-3.5.jar
/usr/share/gradle/lib/plugins/gradle-testing-base-3.5.jar
/usr/share/gradle/lib/plugins/gradle-testing-jvm-3.5.jar
/usr/share/gradle/lib/plugins/gradle-testing-native-3.5.jar
/usr/share/gradle/lib/plugins/gradle-tooling-api-builders-3.5.jar
/usr/share/gradle/lib/plugins/gradle-workers-3.5.jar
/usr/share/gradle/lib/plugins/gson-2.7.jar
/usr/share/gradle/lib/plugins/hamcrest-core-1.3.jar
/usr/share/gradle/lib/plugins/httpclient-4.4.1.jar
/usr/share/gradle/lib/plugins/httpcore-4.4.4.jar
/usr/share/gradle/lib/plugins/ivy-2.2.0.jar
/usr/share/gradle/lib/plugins/jackson-annotations-2.6.6.jar
/usr/share/gradle/lib/plugins/jackson-core-2.6.6.jar
/usr/share/gradle/lib/plugins/jackson-databind-2.6.6.jar
/usr/share/gradle/lib/plugins/jatl-0.2.2.jar
/usr/share/gradle/lib/plugins/jcifs-1.3.17.jar
/usr/share/gradle/lib/plugins/jcommander-1.12.jar
/usr/share/gradle/lib/plugins/jetty-6.1.26.jar
/usr/share/gradle/lib/plugins/jetty-annotations-6.1.26.jar
/usr/share/gradle/lib/plugins/jetty-naming-6.1.26.jar
/usr/share/gradle/lib/plugins/jetty-plus-6.1.26.jar
/usr/share/gradle/lib/plugins/jetty-util-6.1.26.jar
/usr/share/gradle/lib/plugins/joda-time-2.8.2.jar
/usr/share/gradle/lib/plugins/jsch-0.1.54.jar
/usr/share/gradle/lib/plugins/jsp-2.1-6.1.14.jar
/usr/share/gradle/lib/plugins/jsp-api-2.1-6.1.14.jar
/usr/share/gradle/lib/plugins/junit-4.12.jar
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
/usr/share/gradle/lib/plugins/nekohtml-1.9.14.jar
/usr/share/gradle/lib/plugins/plexus-cipher-1.7.jar
/usr/share/gradle/lib/plugins/plexus-classworlds-2.4.jar
/usr/share/gradle/lib/plugins/plexus-component-annotations-1.5.5.jar
/usr/share/gradle/lib/plugins/plexus-container-default-1.5.5.jar
/usr/share/gradle/lib/plugins/plexus-interpolation-1.14.jar
/usr/share/gradle/lib/plugins/plexus-sec-dispatcher-1.3.jar
/usr/share/gradle/lib/plugins/plexus-utils-2.0.6.jar
/usr/share/gradle/lib/plugins/pmaven-common-0.8-20100325.jar
/usr/share/gradle/lib/plugins/pmaven-groovy-0.8-20100325.jar
/usr/share/gradle/lib/plugins/rhino-1.7R3.jar
/usr/share/gradle/lib/plugins/servlet-api-2.5-20081211.jar
/usr/share/gradle/lib/plugins/simple-4.1.21.jar
/usr/share/gradle/lib/plugins/snakeyaml-1.6.jar
/usr/share/gradle/lib/plugins/testng-6.3.1.jar
/usr/share/gradle/lib/plugins/wagon-file-2.4.jar
/usr/share/gradle/lib/plugins/wagon-http-2.4.jar
/usr/share/gradle/lib/plugins/wagon-http-shared4-2.4.jar
/usr/share/gradle/lib/plugins/wagon-provider-api-2.4.jar
/usr/share/gradle/lib/plugins/xbean-reflect-3.4.jar
/usr/share/gradle/lib/plugins/xercesImpl-2.9.1.jar
/usr/share/gradle/lib/plugins/xml-apis-1.3.04.jar
/usr/share/gradle/lib/reflectasm-1.07-shaded.jar
/usr/share/gradle/lib/slf4j-api-1.7.10.jar
/usr/share/gradle/media/gradle-icon-128x128.png
/usr/share/gradle/media/gradle-icon-16x16.png
/usr/share/gradle/media/gradle-icon-24x24.png
/usr/share/gradle/media/gradle-icon-256x256.png
/usr/share/gradle/media/gradle-icon-32x32.png
/usr/share/gradle/media/gradle-icon-48x48.png
/usr/share/gradle/media/gradle-icon-512x512.png
/usr/share/gradle/media/gradle-icon-64x64.png
/usr/share/gradle/media/gradle.icns
