# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext as _

from taggit.forms import TagWidget
from apps.photoalbum.widgets import MultipleImagesInput
from apps.photoalbum.models import Album

from apps.dashboard.widgets import multiple_widget_generator

class AlbumForm(forms.ModelForm):
	class Meta(object):

		model = Album
		fields = [
			'title',
			'tags',
			'photos'
		]

		photos_fields = [('photos', {'id': 'responsive-image-id'})]
		widgetlist = [
			#(MultipleImagesInput, 'photos')
		]

		print("Before widget stuff")
		# Multiple widget generator merges results from regular widget_generator into a single widget dict
		widgets = multiple_widget_generator(widgetlist)
		print("Before widgets update")
		widgets.update({
			'tags': TagWidget(attrs={'placeholder': 'Eksempel: åre, online, kjelleren'}),
			'photos': MultipleImagesInput(attrs={'multiple': True, 'name': 'Bilder'})
			})

		labels = {
					'tags': 'Tags'
		}

"""
class UploadPhotosForm(forms.ModelForm):
	photos = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label=_("Bilder"), required=False)

	class Meta(object):
		model = Album
		fields = ['photos']
"""