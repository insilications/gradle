Name     : gradle
Version  : 3.5
Release  : 1
URL      : https://services.gradle.org/distributions/gradle-3.5-bin.zip
Source0  : https://services.gradle.org/distributions/gradle-3.5-bin.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 LGPL-2.1

%description
You can add .gradle init scripts to this directory. Each one is executed at the start of the build.

%prep
%setup -q -n gradle-3.5

%build

%install
rm -rf %{buildroot}
rm bin/gradle.bat
mkdir -p %{buildroot}/usr/lib/gradle
cp -R bin %{buildroot}/usr
cp -R lib/* %{buildroot}/usr/lib/gradle

%files
%defattr(-,root,root,-)
/usr/bin/gradle
/usr/lib/gradle/annotations-13.0.jar
/usr/lib/gradle/ant-1.9.6.jar
/usr/lib/gradle/ant-launcher-1.9.6.jar
/usr/lib/gradle/asm-all-5.1.jar
/usr/lib/gradle/commons-collections-3.2.2.jar
/usr/lib/gradle/commons-io-2.2.jar
/usr/lib/gradle/commons-lang-2.6.jar
/usr/lib/gradle/dom4j-1.6.1.jar
/usr/lib/gradle/gradle-base-services-3.5.jar
/usr/lib/gradle/gradle-base-services-groovy-3.5.jar
/usr/lib/gradle/gradle-cli-3.5.jar
/usr/lib/gradle/gradle-core-3.5.jar
/usr/lib/gradle/gradle-docs-3.5.jar
/usr/lib/gradle/gradle-installation-beacon-3.5.jar
/usr/lib/gradle/gradle-jvm-services-3.5.jar
/usr/lib/gradle/gradle-launcher-3.5.jar
/usr/lib/gradle/gradle-logging-3.5.jar
/usr/lib/gradle/gradle-messaging-3.5.jar
/usr/lib/gradle/gradle-model-core-3.5.jar
/usr/lib/gradle/gradle-model-groovy-3.5.jar
/usr/lib/gradle/gradle-native-3.5.jar
/usr/lib/gradle/gradle-open-api-3.5.jar
/usr/lib/gradle/gradle-process-services-3.5.jar
/usr/lib/gradle/gradle-resources-3.5.jar
/usr/lib/gradle/gradle-runtime-api-info-3.5.jar
/usr/lib/gradle/gradle-script-kotlin-0.8.0.jar
/usr/lib/gradle/gradle-tooling-api-3.5.jar
/usr/lib/gradle/gradle-ui-3.5.jar
/usr/lib/gradle/gradle-version-info-3.5.jar
/usr/lib/gradle/gradle-wrapper-3.5.jar
/usr/lib/gradle/groovy-all-2.4.10.jar
/usr/lib/gradle/guava-jdk5-17.0.jar
/usr/lib/gradle/jansi-1.14.jar
/usr/lib/gradle/javax.inject-1.jar
/usr/lib/gradle/jaxen-1.1.jar
/usr/lib/gradle/jcip-annotations-1.0.jar
/usr/lib/gradle/jcl-over-slf4j-1.7.10.jar
/usr/lib/gradle/jul-to-slf4j-1.7.10.jar
/usr/lib/gradle/kotlin-compiler-embeddable-1.1.0.jar
/usr/lib/gradle/kotlin-reflect-1.1.0.jar
/usr/lib/gradle/kotlin-stdlib-1.1.0.jar
/usr/lib/gradle/kryo-2.20.jar
/usr/lib/gradle/log4j-over-slf4j-1.7.10.jar
/usr/lib/gradle/minlog-1.2.jar
/usr/lib/gradle/native-platform-0.14.jar
/usr/lib/gradle/native-platform-freebsd-amd64-libcpp-0.14.jar
/usr/lib/gradle/native-platform-freebsd-amd64-libstdcpp-0.14.jar
/usr/lib/gradle/native-platform-freebsd-i386-libcpp-0.14.jar
/usr/lib/gradle/native-platform-freebsd-i386-libstdcpp-0.14.jar
/usr/lib/gradle/native-platform-linux-amd64-0.14.jar
/usr/lib/gradle/native-platform-linux-amd64-ncurses5-0.14.jar
/usr/lib/gradle/native-platform-linux-amd64-ncurses6-0.14.jar
/usr/lib/gradle/native-platform-linux-i386-0.14.jar
/usr/lib/gradle/native-platform-linux-i386-ncurses5-0.14.jar
/usr/lib/gradle/native-platform-linux-i386-ncurses6-0.14.jar
/usr/lib/gradle/native-platform-osx-amd64-0.14.jar
/usr/lib/gradle/native-platform-osx-i386-0.14.jar
/usr/lib/gradle/native-platform-windows-amd64-0.14.jar
/usr/lib/gradle/native-platform-windows-i386-0.14.jar
/usr/lib/gradle/objenesis-1.2.jar
/usr/lib/gradle/plugins/aether-api-1.13.1.jar
/usr/lib/gradle/plugins/aether-connector-wagon-1.13.1.jar
/usr/lib/gradle/plugins/aether-impl-1.13.1.jar
/usr/lib/gradle/plugins/aether-spi-1.13.1.jar
/usr/lib/gradle/plugins/aether-util-1.13.1.jar
/usr/lib/gradle/plugins/aws-java-sdk-core-1.11.6.jar
/usr/lib/gradle/plugins/aws-java-sdk-kms-1.11.6.jar
/usr/lib/gradle/plugins/aws-java-sdk-s3-1.11.6.jar
/usr/lib/gradle/plugins/bcpg-jdk15on-1.51.jar
/usr/lib/gradle/plugins/bcprov-jdk15on-1.51.jar
/usr/lib/gradle/plugins/biz.aQute.bndlib-3.2.0.jar
/usr/lib/gradle/plugins/bsh-2.0b4.jar
/usr/lib/gradle/plugins/commons-cli-1.2.jar
/usr/lib/gradle/plugins/commons-codec-1.6.jar
/usr/lib/gradle/plugins/core-3.1.1.jar
/usr/lib/gradle/plugins/geronimo-annotation_1.0_spec-1.0.jar
/usr/lib/gradle/plugins/gradle-announce-3.5.jar
/usr/lib/gradle/plugins/gradle-antlr-3.5.jar
/usr/lib/gradle/plugins/gradle-build-cache-http-3.5.jar
/usr/lib/gradle/plugins/gradle-build-comparison-3.5.jar
/usr/lib/gradle/plugins/gradle-build-init-3.5.jar
/usr/lib/gradle/plugins/gradle-code-quality-3.5.jar
/usr/lib/gradle/plugins/gradle-composite-builds-3.5.jar
/usr/lib/gradle/plugins/gradle-dependency-management-3.5.jar
/usr/lib/gradle/plugins/gradle-diagnostics-3.5.jar
/usr/lib/gradle/plugins/gradle-ear-3.5.jar
/usr/lib/gradle/plugins/gradle-ide-3.5.jar
/usr/lib/gradle/plugins/gradle-ide-native-3.5.jar
/usr/lib/gradle/plugins/gradle-ide-play-3.5.jar
/usr/lib/gradle/plugins/gradle-ivy-3.5.jar
/usr/lib/gradle/plugins/gradle-jacoco-3.5.jar
/usr/lib/gradle/plugins/gradle-javascript-3.5.jar
/usr/lib/gradle/plugins/gradle-jetty-3.5.jar
/usr/lib/gradle/plugins/gradle-language-groovy-3.5.jar
/usr/lib/gradle/plugins/gradle-language-java-3.5.jar
/usr/lib/gradle/plugins/gradle-language-jvm-3.5.jar
/usr/lib/gradle/plugins/gradle-language-native-3.5.jar
/usr/lib/gradle/plugins/gradle-language-scala-3.5.jar
/usr/lib/gradle/plugins/gradle-maven-3.5.jar
/usr/lib/gradle/plugins/gradle-osgi-3.5.jar
/usr/lib/gradle/plugins/gradle-platform-base-3.5.jar
/usr/lib/gradle/plugins/gradle-platform-jvm-3.5.jar
/usr/lib/gradle/plugins/gradle-platform-native-3.5.jar
/usr/lib/gradle/plugins/gradle-platform-play-3.5.jar
/usr/lib/gradle/plugins/gradle-plugin-development-3.5.jar
/usr/lib/gradle/plugins/gradle-plugin-use-3.5.jar
/usr/lib/gradle/plugins/gradle-plugins-3.5.jar
/usr/lib/gradle/plugins/gradle-publish-3.5.jar
/usr/lib/gradle/plugins/gradle-reporting-3.5.jar
/usr/lib/gradle/plugins/gradle-resources-http-3.5.jar
/usr/lib/gradle/plugins/gradle-resources-s3-3.5.jar
/usr/lib/gradle/plugins/gradle-resources-sftp-3.5.jar
/usr/lib/gradle/plugins/gradle-scala-3.5.jar
/usr/lib/gradle/plugins/gradle-signing-3.5.jar
/usr/lib/gradle/plugins/gradle-test-kit-3.5.jar
/usr/lib/gradle/plugins/gradle-testing-base-3.5.jar
/usr/lib/gradle/plugins/gradle-testing-jvm-3.5.jar
/usr/lib/gradle/plugins/gradle-testing-native-3.5.jar
/usr/lib/gradle/plugins/gradle-tooling-api-builders-3.5.jar
/usr/lib/gradle/plugins/gradle-workers-3.5.jar
/usr/lib/gradle/plugins/gson-2.7.jar
/usr/lib/gradle/plugins/hamcrest-core-1.3.jar
/usr/lib/gradle/plugins/httpclient-4.4.1.jar
/usr/lib/gradle/plugins/httpcore-4.4.4.jar
/usr/lib/gradle/plugins/ivy-2.2.0.jar
/usr/lib/gradle/plugins/jackson-annotations-2.6.6.jar
/usr/lib/gradle/plugins/jackson-core-2.6.6.jar
/usr/lib/gradle/plugins/jackson-databind-2.6.6.jar
/usr/lib/gradle/plugins/jatl-0.2.2.jar
/usr/lib/gradle/plugins/jcifs-1.3.17.jar
/usr/lib/gradle/plugins/jcommander-1.12.jar
/usr/lib/gradle/plugins/jetty-6.1.26.jar
/usr/lib/gradle/plugins/jetty-annotations-6.1.26.jar
/usr/lib/gradle/plugins/jetty-naming-6.1.26.jar
/usr/lib/gradle/plugins/jetty-plus-6.1.26.jar
/usr/lib/gradle/plugins/jetty-util-6.1.26.jar
/usr/lib/gradle/plugins/joda-time-2.8.2.jar
/usr/lib/gradle/plugins/jsch-0.1.54.jar
/usr/lib/gradle/plugins/jsp-2.1-6.1.14.jar
/usr/lib/gradle/plugins/jsp-api-2.1-6.1.14.jar
/usr/lib/gradle/plugins/junit-4.12.jar
/usr/lib/gradle/plugins/maven-aether-provider-3.0.4.jar
/usr/lib/gradle/plugins/maven-artifact-3.0.4.jar
/usr/lib/gradle/plugins/maven-compat-3.0.4.jar
/usr/lib/gradle/plugins/maven-core-3.0.4.jar
/usr/lib/gradle/plugins/maven-model-3.0.4.jar
/usr/lib/gradle/plugins/maven-model-builder-3.0.4.jar
/usr/lib/gradle/plugins/maven-plugin-api-3.0.4.jar
/usr/lib/gradle/plugins/maven-repository-metadata-3.0.4.jar
/usr/lib/gradle/plugins/maven-settings-3.0.4.jar
/usr/lib/gradle/plugins/maven-settings-builder-3.0.4.jar
/usr/lib/gradle/plugins/nekohtml-1.9.14.jar
/usr/lib/gradle/plugins/plexus-cipher-1.7.jar
/usr/lib/gradle/plugins/plexus-classworlds-2.4.jar
/usr/lib/gradle/plugins/plexus-component-annotations-1.5.5.jar
/usr/lib/gradle/plugins/plexus-container-default-1.5.5.jar
/usr/lib/gradle/plugins/plexus-interpolation-1.14.jar
/usr/lib/gradle/plugins/plexus-sec-dispatcher-1.3.jar
/usr/lib/gradle/plugins/plexus-utils-2.0.6.jar
/usr/lib/gradle/plugins/pmaven-common-0.8-20100325.jar
/usr/lib/gradle/plugins/pmaven-groovy-0.8-20100325.jar
/usr/lib/gradle/plugins/rhino-1.7R3.jar
/usr/lib/gradle/plugins/servlet-api-2.5-20081211.jar
/usr/lib/gradle/plugins/simple-4.1.21.jar
/usr/lib/gradle/plugins/snakeyaml-1.6.jar
/usr/lib/gradle/plugins/testng-6.3.1.jar
/usr/lib/gradle/plugins/wagon-file-2.4.jar
/usr/lib/gradle/plugins/wagon-http-2.4.jar
/usr/lib/gradle/plugins/wagon-http-shared4-2.4.jar
/usr/lib/gradle/plugins/wagon-provider-api-2.4.jar
/usr/lib/gradle/plugins/xbean-reflect-3.4.jar
/usr/lib/gradle/plugins/xercesImpl-2.9.1.jar
/usr/lib/gradle/plugins/xml-apis-1.3.04.jar
/usr/lib/gradle/reflectasm-1.07-shaded.jar
/usr/lib/gradle/slf4j-api-1.7.10.jar
