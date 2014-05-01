#!/usr/bin/env python
import optparse
import importlib


def main():
    """A command line interface for creating Dissertate Word templates."""
    p = optparse.OptionParser()
    p.add_option("--school", "-s",
                 action="store", type="string", dest="school")
    p.add_option("--name", "--n",
                 action="store", type="string", dest="name")

    options, arguments = p.parse_args()

    if not options.name:
        options.name = "Firstname M. Lastname"

    if not options.school:
        options.school = "Generic"

    createTemplate(options.school, options.name)


def createTemplate(school, name):
    SchoolPackage = importlib.import_module("schools." + school + ".word")
    template = SchoolPackage.Template()
    template.fill()

    for paragraph in template.document.paragraphs:
        if "Firstname M. Lastname" in paragraph.text:
            style = paragraph.style
            template.clear_paragraph(paragraph)
            paragraph.add_run(name)
            paragraph.style = style

    template.save()


if __name__ == "__main__":
    main()
