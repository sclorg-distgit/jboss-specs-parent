%global pkg_name jboss-specs-parent
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global namedreltag .Beta2
%global namedversion %{version}%{?namedreltag}

Name:             %{?scl_prefix}jboss-specs-parent
Version:          1.0.0
Release:          0.7.9%{namedreltag}.5%{?dist}
Summary:          JBoss Specification API Parent POM
Group:            Development/Libraries
# The license is not included because it's not a part of this tag. License file
# was pushed to trunk and no new tag will be created for this change.
# http://anonsvn.jboss.org/repos/jbossas/projects/specs/trunk/jboss-specs-parent/LICENSE-2.0.txt
License:          ASL 2.0
Url:              http://www.jboss.org/

# svn export http://anonsvn.jboss.org/repos/jbossas/projects/specs/tags/jboss-specs-parent-1.0.0.Beta2/
# tar czf jboss-specs-parent-1.0.0.Beta2-src-svn.tar.gz jboss-specs-parent-1.0.0.Beta2
Source0:          %{pkg_name}-%{namedversion}-src-svn.tar.gz

BuildRequires:    %{?scl_prefix_java_common}maven-local

Requires:         %{?scl_prefix}jboss-parent
Requires:         %{?scl_prefix}maven-compiler-plugin
Requires:         %{?scl_prefix}maven-release-plugin
Requires:         %{?scl_prefix_java_common}maven-local
BuildArch:        noarch

%description
Parent POM that allows building all specification projects at once.

%prep
%setup -q -n %{pkg_name}-%{namedversion}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%pom_xpath_remove pom:modules
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/%{pkg_name}

%changelog
* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 1.0.0-0.7.9.Beta2.5
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1.0.0-0.7.9.Beta2.4
- maven33 rebuild

* Thu Jan 15 2015 Michal Srb <msrb@redhat.com> - 1.0.0-0.7.9.Beta2
- Fix directory ownership

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.0.0-0.7.8.Beta2.3
- Mass rebuild 2015-01-13

* Mon Jan 12 2015 Michael Simacek <msimacek@redhat.com> - 1.0.0-0.7.8.Beta2.2
- BR/R on packages from rh-java-common

* Wed Jan 07 2015 Michal Srb <msrb@redhat.com> - 1.0.0-0.7.8.Beta2.1
- Migrate to .mfiles

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.0.0-0.7.7.Beta2.1
- Mass rebuild 2015-01-06

* Mon Jun  2 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.0-0.7.7.Beta2
- Fix dist tag

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.0-0.7.6.Beta2
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.0-0.7.5.Beta2
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.0-0.7.4.Beta2
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.0-0.7.3.Beta2
- Rebuild to fix incorrect auto-requires

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.0-0.7.2.Beta2
- SCL-ize build-requires
- Migrate from mvn-rpmbuild to %%mvn_build

* Thu Feb 13 2014 Michal Srb <msrb@redhat.com> - 1.0.0-0.7.1.Beta2
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0.0-0.7.Beta2
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.6.Beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.5.Beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.4.Beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 10 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.0-0.3.Beta2
- Cleared license status

* Fri Oct 07 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.0-0.2.Beta2
- Updated license

* Thu Aug 11 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.0-0.1.Beta2
- Initial packaging
