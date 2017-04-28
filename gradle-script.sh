#!/bin/sh

# Source system prefs
if [ -f /etc/java/gradle.conf ] ; then
  . /etc/java/gradle.conf
fi

# Source user prefs
if [ -f $HOME/.gradlerc ] ; then
  . $HOME/.gradlerc
fi

export GRADLE_HOME="${GRADLE_HOME:-/usr/share/gradle}"
$GRADLE_HOME/bin/gradle "$@"
