from django.db import models
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class Volunteer(models.Model):
    """Volunteers are people who contribute time to Klimaat Helpdesk. The model is similar to those of
    experts, with some minor differences that's why it is not a plain inherited object.
    """

    name = models.CharField(_("name"), max_length=255, null=False, blank=False)
    email = models.EmailField(_("email"), null=True, blank=True)
    bio = models.TextField(verbose_name=_("biography"), null=True, blank=True)
    picture = models.ForeignKey(
        "wagtailimages.Image", null=True, related_name="+", on_delete=models.SET_NULL
    )
    roles = TaggableManager(verbose_name=_("roles"))
    affiliation = models.CharField(_("Affiliation"), blank=True, max_length=128)
    website = models.URLField(_("Website"), blank=True)
    twitter_profile = models.URLField(_("Twitter Profile"), blank=True, null=True)
    linkedin_profile = models.URLField(_("LinkedIn Profile"), blank=True, null=True)
    orcid_profile = models.URLField(_("OrcID Link"), blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    active_since = models.DateTimeField(null=True, auto_now_add=False, default=None)

    panels = [
        FieldPanel("name"),
        ImageChooserPanel(
            "picture", heading="Volunteer's photo, 1:1 aspect ratio (square) works best"
        ),
        FieldPanel("email"),
        FieldPanel("bio"),
        FieldPanel("affiliation"),
        FieldPanel(
            "roles",
            heading="Roles of the volunteer. A maximum of 16 characters per word is recommended for "
            "optimal mobile display",
        ),
        FieldPanel("website"),
        FieldPanel("twitter_profile"),
        FieldPanel("linkedin_profile"),
        FieldPanel("orcid_profile"),
        FieldPanel("active_since"),
    ]

    def __str__(self):
        return f"{self.name}"

    @property
    def twitter_username(self):
        if self.twitter_profile:
            if self.twitter_profile.endswith("/"):
                self.twitter_profile = self.twitter_profile[:-1]
                self.save()
            twitter_username = self.twitter_profile.split("/")[-1]
            return twitter_username

    class Meta:
        ordering = [
            "name",
        ]
