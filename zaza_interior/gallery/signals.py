# import os
# import shutil
# from django.db.models.signals import post_delete
# from django.dispatch import receiver
# from filer.models import File
#
#
# @receiver(post_delete, sender=File)
# def delete_image_folder(sender, instance, **kwargs):
#     file_path = instance.file.path
#     third_level_up = os.path.abspath(os.path.join(file_path, "../../../"))
#     shutil.rmtree(third_level_up)
#
#     path_parts = file_path.split(os.sep)
#     filer_index = path_parts.index('filer_public')
#     thumbnail_path_parts = path_parts[:filer_index] + ['filer_public_thumbnails', 'filer_public'] + path_parts[
#                                                                                                     filer_index + 1:]
#     thumbnail_file_path = os.sep.join(thumbnail_path_parts)
#     thumbnail_third_level_up = os.path.abspath(os.path.join(thumbnail_file_path, "../../../"))
#     shutil.rmtree(thumbnail_third_level_up)

