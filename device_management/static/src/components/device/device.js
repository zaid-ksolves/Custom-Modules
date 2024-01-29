/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";
import { booleanField, BooleanField } from "@web/views/fields/boolean/boolean_field";
import { standardFieldProps } from "@web/views/fields/standard_field_props";
import { Component, useState,onRendered } from "@odoo/owl";

export class newBooleanToggleField extends BooleanField {
    static template = "device_management.DemoTemplateBooleanToggle";

    static props = {
        ...BooleanField.props,
        autosave: { type: Boolean, optional: true },
    };

  setup(){
  this.props.state = useState({value:this.props.record.data[this.props.name]})
  }

    async onClick(newValue) {
        this.props.state.value = newValue.target.checked
        await this.props.record.update({ [this.props.name]:  newValue.target.checked });
    }
}

export const newbooleanToggleField = {
    ...booleanField,
    component: newBooleanToggleField,
    displayName: _t("Toggle"),
    supportedOptions: [
        {
            label: _t("Autosave"),
            name: "autosave",
            type: "boolean",
            default: true,
            help: _t(
                "If checked, the record will be saved immediately when the field is modified."
            ),
        },
    ],
    extractProps({ options }, dynamicInfo) {
        return {
            autosave: "autosave" in options ? Boolean(options.autosave) : true,
            readonly: dynamicInfo.readonly,
        };
    },
};

registry.category("fields").add("new_boolean_toggle", newbooleanToggleField);