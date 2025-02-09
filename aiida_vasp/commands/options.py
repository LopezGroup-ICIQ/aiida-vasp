"""
Common click options for verdi.

-------------------------------
Common click options for verdi commands.
"""
import click

try:
    from aiida.cmdline.params.options import DESCRIPTION, FORCE, OverridableOption  # pylint: disable=unused-import
except ImportError:
    # pylint: disable=too-few-public-methods
    class OverridableOption(object):  # pylint: disable=useless-object-inheritance
        """
        Wrapper around click option that increases reusability.

        Click options are reusable already but sometimes it can improve the user interface to for example customize a help message
        for an option on a per-command basis. Sometimes the option should be prompted for if it is not given. On some commands an option
        might take any folder path, while on another the path only has to exist.

        Overridable options store the arguments to click.option and only instanciate the click.Option on call, kwargs given to ``__call__``
        override the stored ones.

        Example::

            FOLDER = OverridableOption('--folder', type=click.Path(file_okay=False), help='A folder')

            @click.command()
            @FOLDER(help='A folder, will be created if it does not exist')
            def ls_or_create(folder):
                click.echo(os.listdir(folder))

            @click.command()
            @FOLDER(help='An existing folder', type=click.Path(exists=True, file_okay=False, readable=True)
            def ls(folder)
                click.echo(os.listdir(folder))
        """

        def __init__(self, *args, **kwargs):
            """Store the defaults."""
            self.args = args
            self.kwargs = kwargs

        def __call__(self, **kwargs):
            """Override kwargs (no name changes) and return option."""
            kw_copy = self.kwargs.copy()
            kw_copy.update(kwargs)
            return click.option(*self.args, **kw_copy)

    FORCE = OverridableOption('-f', '--force', is_flag=True, help='Do not ask for confirmation.')
    DESCRIPTION = OverridableOption('-d', '--description', help='(text) description')

FAMILY_NAME = OverridableOption('-n',
                                '--name',
                                required=True,
                                help='The name you want to give this family of potential(s). '
                                'This is the name you will use in the future when telling which potentials to use '
                                'for a specific calculation or workflow.')
PATH = OverridableOption('-p', '--path', default='.', type=click.Path(exists=True), help='Path to the folder.')

DRY_RUN = OverridableOption('--dry-run', is_flag=True, is_eager=True, help='Do not commit to database or modify configurations.')
