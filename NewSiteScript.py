from extras.scripts import *
from django.utils.text import slugify
from extras.plugins import PluginConfig
from dcim.choices import DeviceStatusChoices, SiteStatusChoices
from dcim.models import Device, DeviceRole, DeviceType, Site

class NewSiteScript(Script):
    class Meta:
        name = "New Branch"
        description = "Provision a new branch site"
    site_name = StringVar(
        description="Name of the new site"
    )

    def run(self, data, commit):

        # Create the new site
        site = Site(
            name=data['site_name'],
            slug=slugify(data['site_name']),
            status=SiteStatusChoices.STATUS_PLANNED
        )
        site.save()
        self.log_success(f"Created new site: {site}")

