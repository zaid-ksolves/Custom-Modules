/** @odoo-module */
import { ListController } from "@web/views/list/list_controller";
import { registry } from '@web/core/registry';
import { listView } from '@web/views/list/list_view';
const { useState} = owl;
import { useService } from "@web/core/utils/hooks";
export class DeviceListController extends ListController {
   setup() {
       super.setup();
        this.orm = useService("orm")
        this.actionService = useService("action")
   }
   async checkState() {
    const selectedResIds = await this.getSelectedResIds();
    const result = await this.orm.call('person.list', "changeState", [selectedResIds]);
    if(result){
        this.actionService.doAction({
        type:"ir.actions.client",
        tag:"soft_reload",
        });
    }
   }
}

registry.category("views").add("button_in_tree", {
   ...listView,
   Controller: DeviceListController,
//  buttonTemplate: "device_management.ListView.Buttons",
});