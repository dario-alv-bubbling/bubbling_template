from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    help = 'Renames a Django project'

    def add_arguments(self, parser):
        parser.add_argument('current', type=str, nargs='+',
                            help='The current Django project folder name')
        parser.add_argument('new', type=str, nargs='+',
                            help='The new Django project name')

    def handle(self, *args, **kwargs):
        current_project_name = kwargs['current'][0]
        new_project_name = kwargs['new'][0]

        # replace `-` with `_` as it cause issues

        new_project_name = new_project_name.replace('-', '_')

        # logic for renaming the files

        files_to_rename = [f'{current_project_name}/settings/components/common.py',
                           f'{current_project_name}/settings/components/database.py',
                           f'{current_project_name}/settings/components/storage.py',
                           f'{current_project_name}/settings/.env.template',
                           f'{current_project_name}/asgi.py',
                           f'{current_project_name}/wsgi.py',
                           'manage.py']

        for f in files_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()

            filedata = filedata.replace(current_project_name, new_project_name)

            with open(f, 'w') as file:
                file.write(filedata)

        os.rename(current_project_name, new_project_name)

        self.stdout.write(self.style.SUCCESS(
            'Project has been renamed to %s' % new_project_name))
