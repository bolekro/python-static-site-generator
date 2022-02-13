import typer
from ssg.site import Site


def main(source="content", dest="dist"):
    config = {'source': source, 'dest': dest}
    print(config)
    print(type(config))
    Site(**config).build()


typer.run(main)
