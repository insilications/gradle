Name     : gradle
Version  : 4.3
Release  : 15
URL      : https://github.com/gradle/
Source0  : https://services.gradle.org/distributions/gradle-4.3-bin.zip
Source1  : all-released-versions.json
Source2  : gradle-script.sh
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 LGPL-2.1
Requires: openjdk-dev
Requires: ca-certs
Requires: procps-ng

%description
You can add .gradle init scripts to this directory. Each one is executed at the start of the build.

%prep
%setup -q -n gradle-4.3

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/gradle
cp -R ./* %{buildroot}/usr/share/gradle
rm %{buildroot}/usr/share/gradle/bin/gradle.bat

mkdir -p %{buildroot}/usr/bin
ln -s /usr/share/gradle/bin/gradle %{buildroot}/usr/bin/gradle

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
/usr/share/gradle/lib/asm-debug-all-6.0_ALPHA.jar
/usr/share/gradle/lib/commons-collections-3.2.2.jar
/usr/share/gradle/lib/commons-compress-1.14.jar
/usr/share/gradle/lib/commons-io-2.2.jar
/usr/share/gradle/lib/commons-lang-2.6.jar
/usr/share/gradle/lib/gradle-base-services-4.3.jar
/usr/share/gradle/lib/gradle-base-services-groovy-4.3.jar
/usr/share/gradle/lib/gradle-build-cache-4.3.jar
/usr/share/gradle/lib/gradle-build-option-4.3.jar
/usr/share/gradle/lib/gradle-cli-4.3.jar
/usr/share/gradle/lib/gradle-core-4.3.jar
/usr/share/gradle/lib/gradle-core-api-4.3.jar
/usr/share/gradle/lib/gradle-docs-4.3.jar
/usr/share/gradle/lib/gradle-installation-beacon-4.3.jar
/usr/share/gradle/lib/gradle-jvm-services-4.3.jar
/usr/share/gradle/lib/gradle-kotlin-dsl-0.12.3.jar
/usr/share/gradle/lib/gradle-kotlin-dsl-tooling-builders-0.12.3.jar
/usr/share/gradle/lib/gradle-kotlin-dsl-tooling-models-0.12.3.jar
/usr/share/gradle/lib/gradle-launcher-4.3.jar
/usr/share/gradle/lib/gradle-logging-4.3.jar
/usr/share/gradle/lib/gradle-messaging-4.3.jar
/usr/share/gradle/lib/gradle-model-core-4.3.jar
/usr/share/gradle/lib/gradle-model-groovy-4.3.jar
/usr/share/gradle/lib/gradle-native-4.3.jar
/usr/share/gradle/lib/gradle-persistent-cache-4.3.jar
/usr/share/gradle/lib/gradle-process-services-4.3.jar
/usr/share/gradle/lib/gradle-resources-4.3.jar
/usr/share/gradle/lib/gradle-runtime-api-info-4.3.jar
/usr/share/gradle/lib/gradle-tooling-api-4.3.jar
/usr/share/gradle/lib/gradle-wrapper-4.3.jar
/usr/share/gradle/lib/groovy-all-2.4.12.jar
/usr/share/gradle/lib/guava-jdk5-17.0.jar
/usr/share/gradle/lib/jansi-1.14.jar
/usr/share/gradle/lib/javax.inject-1.jar
/usr/share/gradle/lib/jcip-annotations-1.0.jar
/usr/share/gradle/lib/jcl-over-slf4j-1.7.10.jar
/usr/share/gradle/lib/jsr305-1.3.9.jar
/usr/share/gradle/lib/jul-to-slf4j-1.7.10.jar
/usr/share/gradle/lib/kotlin-compiler-embeddable-1.1.51.jar
/usr/share/gradle/lib/kotlin-reflect-1.1.51.jar
/usr/share/gradle/lib/kotlin-sam-with-receiver-compiler-plugin-1.1.51.jar
/usr/share/gradle/lib/kotlin-stdlib-1.1.51.jar
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
/usr/share/gradle/lib/plugins/bcpg-jdk15on-1.57.jar
/usr/share/gradle/lib/plugins/bcprov-jdk15on-1.57.jar
/usr/share/gradle/lib/plugins/biz.aQute.bndlib-3.4.0.jar
/usr/share/gradle/lib/plugins/bsh-2.0b4.jar
/usr/share/gradle/lib/plugins/commons-cli-1.2.jar
/usr/share/gradle/lib/plugins/commons-codec-1.6.jar
/usr/share/gradle/lib/plugins/dd-plist-1.20.jar
/usr/share/gradle/lib/plugins/google-api-client-1.22.0.jar
/usr/share/gradle/lib/plugins/google-api-services-storage-v1-rev78-1.22.0.jar
/usr/share/gradle/lib/plugins/google-http-client-1.22.0.jar
/usr/share/gradle/lib/plugins/google-http-client-jackson2-1.22.0.jar
/usr/share/gradle/lib/plugins/google-oauth-client-1.22.0.jar
/usr/share/gradle/lib/plugins/gradle-announce-4.3.jar
/usr/share/gradle/lib/plugins/gradle-antlr-4.3.jar
/usr/share/gradle/lib/plugins/gradle-build-cache-http-4.3.jar
/usr/share/gradle/lib/plugins/gradle-build-comparison-4.3.jar
/usr/share/gradle/lib/plugins/gradle-build-init-4.3.jar
/usr/share/gradle/lib/plugins/gradle-code-quality-4.3.jar
/usr/share/gradle/lib/plugins/gradle-composite-builds-4.3.jar
/usr/share/gradle/lib/plugins/gradle-dependency-management-4.3.jar
/usr/share/gradle/lib/plugins/gradle-diagnostics-4.3.jar
/usr/share/gradle/lib/plugins/gradle-ear-4.3.jar
/usr/share/gradle/lib/plugins/gradle-ide-4.3.jar
/usr/share/gradle/lib/plugins/gradle-ide-native-4.3.jar
/usr/share/gradle/lib/plugins/gradle-ide-play-4.3.jar
/usr/share/gradle/lib/plugins/gradle-ivy-4.3.jar
/usr/share/gradle/lib/plugins/gradle-jacoco-4.3.jar
/usr/share/gradle/lib/plugins/gradle-javascript-4.3.jar
/usr/share/gradle/lib/plugins/gradle-language-groovy-4.3.jar
/usr/share/gradle/lib/plugins/gradle-language-java-4.3.jar
/usr/share/gradle/lib/plugins/gradle-language-jvm-4.3.jar
/usr/share/gradle/lib/plugins/gradle-language-native-4.3.jar
/usr/share/gradle/lib/plugins/gradle-language-scala-4.3.jar
/usr/share/gradle/lib/plugins/gradle-maven-4.3.jar
/usr/share/gradle/lib/plugins/gradle-osgi-4.3.jar
/usr/share/gradle/lib/plugins/gradle-platform-base-4.3.jar
/usr/share/gradle/lib/plugins/gradle-platform-jvm-4.3.jar
/usr/share/gradle/lib/plugins/gradle-platform-native-4.3.jar
/usr/share/gradle/lib/plugins/gradle-platform-play-4.3.jar
/usr/share/gradle/lib/plugins/gradle-plugin-development-4.3.jar
/usr/share/gradle/lib/plugins/gradle-plugin-use-4.3.jar
/usr/share/gradle/lib/plugins/gradle-plugins-4.3.jar
/usr/share/gradle/lib/plugins/gradle-publish-4.3.jar
/usr/share/gradle/lib/plugins/gradle-reporting-4.3.jar
/usr/share/gradle/lib/plugins/gradle-resources-gcs-4.3.jar
/usr/share/gradle/lib/plugins/gradle-resources-http-4.3.jar
/usr/share/gradle/lib/plugins/gradle-resources-s3-4.3.jar
/usr/share/gradle/lib/plugins/gradle-resources-sftp-4.3.jar
/usr/share/gradle/lib/plugins/gradle-scala-4.3.jar
/usr/share/gradle/lib/plugins/gradle-signing-4.3.jar
/usr/share/gradle/lib/plugins/gradle-test-kit-4.3.jar
/usr/share/gradle/lib/plugins/gradle-testing-base-4.3.jar
/usr/share/gradle/lib/plugins/gradle-testing-jvm-4.3.jar
/usr/share/gradle/lib/plugins/gradle-testing-native-4.3.jar
/usr/share/gradle/lib/plugins/gradle-tooling-api-builders-4.3.jar
/usr/share/gradle/lib/plugins/gradle-version-control-4.3.jar
/usr/share/gradle/lib/plugins/gradle-workers-4.3.jar
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
/usr/share/gradle/lib/plugins/joda-time-2.8.2.jar
/usr/share/gradle/lib/plugins/jsch-0.1.54.jar
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
