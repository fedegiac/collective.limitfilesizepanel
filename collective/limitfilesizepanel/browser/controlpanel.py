# -*- coding: utf-8 -*-

from Products.statusmessages.interfaces import IStatusMessage

from plone.app.registry.browser import controlpanel

from z3c.form import button

from collective.limitfilesizepanel.interfaces import ILimitFileSizePanel
from collective.limitfilesizepanel import messageFactory as _
     
class LimitFileSizeEditForm(controlpanel.RegistryEditForm):
    """Media settings form.
    """
    schema = ILimitFileSizePanel
    id = "LimitFileSizeEditForm"
    label = _(u"Limit file size settings")
    description = _(u"help_limit_file_size_panel",
                    default=u"Set file size for file and image")

    @button.buttonAndHandler(_('Save'), name='save')
    def handleSave(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        changes = self.applyChanges(data)
        IStatusMessage(self.request).addStatusMessage(_(u"Changes saved"),
                                                      "info")
        self.context.REQUEST.RESPONSE.redirect("@@limitfilesize-settings")

    @button.buttonAndHandler(_('Cancel'), name='cancel')
    def handleCancel(self, action):
        IStatusMessage(self.request).addStatusMessage(_(u"Edit cancelled"),
                                                      "info")
        self.request.response.redirect("%s/%s" % (self.context.absolute_url(),
                                                  self.control_panel_view))



class LimitFileSizeControlPanel(controlpanel.ControlPanelFormWrapper):
    """Analytics settings control panel.
    """
    form = LimitFileSizeEditForm