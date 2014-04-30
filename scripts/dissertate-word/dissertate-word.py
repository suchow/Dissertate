#!/usr/bin/env python
import optparse
import importlib


def main():
    """A command line interface for creating Dissertate Word templates."""
    p = optparse.OptionParser()
    p.add_option("--school", "-s",
                 action="callback", callback=createTemplate, type="str")

    options, arguments = p.parse_args()


def createTemplate(option, opt_str, schoolName, parser):
    SchoolPackage = importlib.import_module("Schools." + schoolName + ".word")
    template = SchoolPackage.Template()
    template.fill()
    template.save()


if __name__ == "__main__":
    main()
