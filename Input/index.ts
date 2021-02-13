import { AzureFunction, Context, HttpRequest } from "@azure/functions"
import { add_key_values, format_datetime } from "./wrangler"
import { Wirepusher } from "./wirepusher"

const httpTrigger: AzureFunction = async function (context: Context, req: HttpRequest): Promise<void> {
    context.log('Input Triggered');
    const wp = new Wirepusher(process.env.WIREPUSHER_ID);

    context.log('Adding Keys');
    add_key_values(req.body);
    context.log('Formatting DateTime');
    format_datetime(req.body);
    context.log('Writing to Table');
    context.bindings.tableOut.push(req.body)
    context.log('Notifying');
    wp.notify("Success", "Record added")

    context.res = {
        body: req.body
    };

};

export default httpTrigger;
